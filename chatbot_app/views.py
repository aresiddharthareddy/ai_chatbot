from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .nlp.intent_detection import detect_intent
from .models import Ticket, Department, UserQuery
from .serializers import TicketSerializer, DepartmentSerializer, UserQuerySerializer
import google.generativeai as genai

from django.db import connection

class ChatbotViewSet(viewsets.ViewSet):

    def create(self, request):
        user_query = request.data.get('query')

        # Use Google Generative AI to generate a query from the user's input
        genai.configure(api_key='AIzaSyCCEqHpyhjZWTzr_oD7BsqKtlL3dWIDNsI')
        model = genai.GenerativeModel()
        prompt = f"""
        You are an assistant that converts natural language requests into SQL queries for a Django backend.

        Database tables:
        1. ticket (id, title, description, status, created_at, updated_at)
        2. department (id, name, description)

        Given the following user request, generate a valid SQL query (as plain text) that matches the intent. Only return the SQL query, nothing else.

        User request: {user_query}
        """
        response = model.generate_content(prompt)
        generated_query = response.text if hasattr(response, 'text') else str(response)

        # Clean up code block markers and language hints from the generated query
        if generated_query.startswith("```"):
            generated_query = generated_query.strip("`").strip()
            if generated_query.startswith("sql"):
                generated_query = generated_query[3:].strip()
        if generated_query.endswith("```"):
            generated_query = generated_query[:-3].strip()
        if generated_query.endswith("`"):
            generated_query = generated_query.rstrip("`").strip()
        if generated_query.endswith("\n"):
            generated_query = generated_query.rstrip("\n").strip()

        # Execute the generated query
        result = []
        try:
            with connection.cursor() as cursor:
                cursor.execute(generated_query)
                if cursor.description:  # If the query returns data
                    columns = [col[0] for col in cursor.description]
                    rows = cursor.fetchall()
                    for row in rows:
                        result.append(dict(zip(columns, row)))
                else:
                    result = {"rows_affected": cursor.rowcount}
        except Exception as e:
            return Response({
                "generated_query": generated_query,
                "error": str(e)
            }, status=400)

        return Response({
            "generated_query": generated_query,
            "result": result
        }, status=200)

    @action(detail=False, methods=['post'])
    def resolve_ticket(self, request):
        # Logic for ticket resolution
        ticket_data = request.data.get('ticket_data')
        serializer = TicketSerializer(data=ticket_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @action(detail=False, methods=['post'])
    def change_department(self, request):
        # Logic for changing department
        department_data = request.data.get('department_data')
        serializer = DepartmentSerializer(data=department_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @action(detail=False, methods=['post'])
    def retrieve_data(self, request):
        # Logic for data retrieval
        query_data = request.data.get('query_data')
        serializer = UserQuerySerializer(data=query_data)
        if serializer.is_valid():
            # Assuming we have a method to process the query
            result = self.process_query(serializer.validated_data)
            return Response(result, status=200)
        return Response(serializer.errors, status=400)

    def process_query(self, query_data):
        # Placeholder for query processing logic
        return {"result": "Data retrieved based on query."}
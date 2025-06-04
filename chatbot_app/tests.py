from django.test import TestCase
from .models import Ticket, Department, UserQuery

class TicketModelTest(TestCase):
    def setUp(self):
        self.ticket = Ticket.objects.create(
            title="Test Ticket",
            description="This is a test ticket.",
            status="Open"
        )

    def test_ticket_creation(self):
        self.assertEqual(self.ticket.title, "Test Ticket")
        self.assertEqual(self.ticket.status, "Open")

class DepartmentModelTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(
            name="IT Support"
        )

    def test_department_creation(self):
        self.assertEqual(self.department.name, "IT Support")

class UserQueryModelTest(TestCase):
    def setUp(self):
        self.query = UserQuery.objects.create(
            query_text="How do I reset my password?"
        )

    def test_user_query_creation(self):
        self.assertEqual(self.query.query_text, "How do I reset my password?")
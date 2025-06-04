def detect_intent(user_input):
    """
    Simple intent detection based on keyword matching.
    This function checks the user input for specific keywords
    related to IT services such as ticket resolution, department changes,
    and data retrieval.
    """
    user_input = user_input.lower()
    
    if "ticket" in user_input and ("resolve" in user_input or "status" in user_input):
        return "ticket_resolution"
    elif "department" in user_input and ("change" in user_input or "transfer" in user_input):
        return "department_change"
    elif "data" in user_input or "retrieve" in user_input:
        return "data_retrieval"
    else:
        return "unknown_intent"

def handle_query(user_input):
    """
    Handles the user query by detecting the intent and returning
    an appropriate response or action.
    """
    intent = detect_intent(user_input)
    
    if intent == "ticket_resolution":
        return "Please provide your ticket ID for resolution."
    elif intent == "department_change":
        return "Which department would you like to change to?"
    elif intent == "data_retrieval":
        return "What data would you like to retrieve?"
    else:
        return "I'm sorry, I didn't understand your request."
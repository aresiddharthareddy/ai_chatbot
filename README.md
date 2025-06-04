# Chatbot IT Services Project

This project is a Django-based chatbot application designed to provide IT services, including ticket resolution, department changes, and data retrieval based on user queries. The application utilizes the Django REST Framework for building APIs and incorporates basic Natural Language Processing (NLP) techniques for intent detection.

## Features

- **Ticket Resolution**: Users can create and manage IT support tickets through the chatbot.
- **Department Changes**: The chatbot can assist users in changing their department-related queries.
- **Data Retrieval**: Users can retrieve information based on their queries using the chatbot.

## Project Structure

```
chatbot_project
├── chatbot_app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── nlp
│   │   ├── __init__.py
│   │   └── intent_detection.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── chatbot_project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd chatbot_project
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Access the chatbot API endpoints through the defined URLs in `chatbot_app/urls.py`.
- Use the chatbot interface to interact with the IT services.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
# Named Entity Recognition as a Flask Service

The NER Flask Service is a comprehensive RESTful API system designed to provide Named Entity Recognition (NER) services. Built on Flask, it integrates spaCy for NER, employs SQLAlchemy for data management, and emphasizes security and efficiency. It caters to a wide range of users, from individuals submitting texts for entity recognition.

Find API docs in 

``API_docs.md``

## Getting Started

You should have python 3.11 and above. Below steps are for macOS/linux
To get started with this project, follow the steps below:

1. Run the `init_setup.sh` script using bash:

   ```
   bash init_setup.sh
   ```
2. Activate the virtual environment:

   ```
   source venv/bin/activate
   ```
3. Start the server:

   ```
   python3 -m src.app
   ```
4. Test the application:
   Run this commad after running 3 in a seperate terminal window

   ```
   python3 -m pytest src
   ```

## Core Functionalities and Technologies

- Flask Framework: Serves as the backbone for creating RESTful API endpoints, managing requests, and routing.
- spaCy NLP Library: A powerful, industry-standard library used for performing NER on submitted texts, capable of identifying various entity types without custom modifications for this application.
- SQLAlchemy: These tools manage the application's data, handling user information, text submissions, and NER results securely and efficiently.
- JWT for Authentication: Facilitates secure user authentication and authorization across the application, with JWT tokens ensuring that endpoints and actions are protected.

## Enhanced Features and Security Measures

- Advanced User Roles and Permissions:
- Admin Rights: Admin users possess the ability to delete any user account and remove any NER submissions across the platform, ensuring they can manage the application's content and user base effectively.
- User Privacy and Security: Regular users can manage their submissions and profile but have restricted access compared to admins.

## Security Practices:

- Password Encryption: Utilizing bcrypt for hashing passwords, thereby enhancing the security of user credentials stored in the database.
- Token Encryption: JWT tokens are encrypted, providing a secure means of user authentication and session management.

## Files

This project contains the following files and directories:

- API_docs.md: Contains all the API documentation, including input and output expectations.
- requirements.txt: Lists all the dependencies required for the project.
- services:
  - jwt_service.py: Used to authorize users, both admins and regular users.
  - NER_service.py: Generates Named Entity Recognition (NER) and analyzes text to identify entity tags using Spacy.
- tests:
  - integration: Contains integration tests for the REST APIs.
  - unit: Contains unit tests for the NER functionality.
- models: Contains SQL database models.
- controllers:
  - auth_controller.py: Handles sign-in and sign-up functionality/APIs.
  - NER_controller.py: Handles NER-related APIs, including update, post, and delete operations.
  - user_controller.py: Handles user information APIs, including update, delete, and get operations.
- config: Contains all the configuration setup.
- src/__init__.py: Provides information and fetches files from here.
- src/routes.py: Registers the Flask blueprints for the user, auth, and NER services.
- src/app.py: Runs the Flask server.

# React + Django Library Management System
This project is a full-stack Library Management System built using React for the frontend and Django for the backend. It allows users to manage library operations seamlessly through a modern web interface.

# Project Structure
    project-root/
    ├── backend/
    │   ├── library_management/      # Django project settings
    │   ├── accounts/                # User authentication and account management
    │   ├── library/                 # Main app for library operations
    │   ├── db.sqlite3               # SQLite database
    │   ├── manage.py                # Django management script
    │   ├── .venv/                   # Python virtual environment (excluded via .gitignore)
    ├── frontend/
    │   ├── node_modules/            # Frontend dependencies
    │   ├── public/                  # Static files for React
    │   ├── src/                     # React source files
    │   ├── package.json             # Frontend dependencies and scripts
    │   ├── tailwind.config.js       # Tailwind CSS configuration
    │   ├── .gitignore               # Excludes unnecessary files (e.g., node_modules)
    │   ├── README.md                # Frontend-specific documentation
    └── README.md                    # Root-level documentation

# Features
    Backend (Django)
    Authentication: User login and registration with Django's built-in authentication system.
    Library Management: Core functionality to manage books, borrowers, and transactions.
    Database: Pre-configured with SQLite for easy setup.

    Frontend (React)
    UI Framework: Built with React and styled using Tailwind CSS.
    Responsive Design: Ensures compatibility across devices.
    State Management: Handles frontend state with React's state mechanisms.

# Installation and Setup
    Backend Setup
    1. Navigate to the backend directory:

    cd backend

    2. Create a virtual environment and activate it:

    python -m venv .venv
    source .venv/bin/activate  # macOS/Linux
    .venv\Scripts\activate     # Windows
    
    3. Install dependencies:

    pip install -r requirements.txt

    4. Run migrations and start the server:

    python manage.py migrate
    python manage.py runserver

    Frontend Setup
    1. Navigate to the frontend directory:

    cd frontend

    2. Install dependencies:

    npm install

    3. Start the development server:

    npm start

# Usage
    1. Start the Django backend to enable API endpoints.
    2. Start the React frontend to view the web application.
    3. Navigate to http://localhost:3000 for the frontend and http://localhost:8000 for the backend.
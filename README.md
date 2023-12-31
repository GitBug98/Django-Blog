# Django-Blog

Project Name

Project Name: Django CRUD Blog with Authentication and SMTP-based Password Reset

Brief Description:
A blog project that allows users to create, read, update, and delete articles. It also includes an authentication system for login and password reset functionality using the Simple Mail Transfer Protocol (SMTP).

Contents

    manage.py: The main Django management script.
    core/: The Django app directory.
        models.py: Contains the blog database models.
        views.py: Contains the views and logic for the blog app.
        urls.py: Contains the URL patterns for the app.
        addmin.py: Contains register post model in admin panel.
        templates/core/: Directory containing bblog app HTML templates.
    accounts/: The Django app directory for authentication.
        models.py: Contains the user authentication models.
        views.py: Contains the views and logic for authentication.
        signals.py: Contains signals to create profile for new users.
        urls.py: Contains the URL patterns for authentication.
        addmin.py: Contains register profile model in admin panel.
        templates/: Directory containing accounts HTML templates for authentication.
    settings.py: Django project settings file.
    manage.py: managing and running project.
    urls.py: Project-level URL configuration.
    static/: Directory containing CSS and JavaScript files.
    media/: Directory media files.
    templates/: Directory containing base HTML templates.
    requirements.txt: List of libraries and dependencies required to run the project.

Requirements

    Python 3.x
    Django framework
    Django django-bootstrap4 forms for managing web forms.
    Django authentication framework for user authentication.
    Django signals for automatically create profile for new users.
    Django SMTP email backend for sending email using SMTP.

Installation

    Download the project from the GitHub repository.
    Create a new virtual environment.
    Install the required libraries using the following command:
    basic

pip install -r requirements.txt

Configure the database settings in the settings.py file.
Run the migrations to create the necessary database tables:

python manage.py migrate

Start the development server using the following command:

python manage.py runserver


# Django--Recipe-


# Recipe Inventory

Welcome to the Recipe Inventory project! This Django-based application allows users to submit and manage their favorite recipes, including the recipe name, description, and image.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Database Models](#database-models)
- [Views and Templates](#views-and-templates)
- [Contributing](#contributing)
- [License](#license)

## Features
- User-friendly interface to add new recipes
- Display recipes with their names, descriptions, and images
- Backend operations for storing and retrieving recipe data

## Technologies Used
- Django
- PostgreSQL (or MySQL, SQLite)
- HTML/CSS
- JavaScript
- Bootstrap (for styling)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/govindtiwari48/recipe-inventory.git
    cd recipe-inventory
    ```

2. **Set up a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**
    - Ensure you have PostgreSQL installed and running.
    - Create a database for the project.
    - Update the `DATABASES` setting in `settings.py` with your database configuration.
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage

1. **Add a new recipe:**
   - Navigate to the add recipe page.
   - Fill in the form with the recipe name, description, and upload an image.
   - Submit the form to save the recipe to the database.

2. **View recipes:**
   - Browse through the list of recipes on the homepage.
   - Click on a recipe to view its details.

## Database Models

Here is an overview of the primary database model used in the project:

```python
from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/')

    def __str__(self):
        return self.name

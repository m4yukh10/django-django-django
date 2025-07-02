# Django Django Django

A practice **Django 5.x project** for learning foundational web development using Django.

## Features

- Blog app with:
  - Post creation (title, content, timestamp)
  - Listing all posts dynamically
- Ready structure for adding:
  - To-do list app
  - User authentication
  - Comments system
  - Search and pagination

## Project Structure

```

django-django-django/
├── blog/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── django\_django\_django/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt

````

## Setup

1. Clone the repository:

    ```
    git clone https://github.com/m4yukh10/django-django-django.git
    cd django-django-django
    ```

2. Create a virtual environment:

    ```
    python -m venv venv
    ```

    Activate:
    - Windows: `venv\Scripts\activate`
    - Mac/Linux: `source venv/bin/activate`

3. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Run the server:

    ```
    python manage.py runserver
    ```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the project.

## License

Open for learning and experimentation.

## Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Corey Schafer Django Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)
````

# Django CRUD Application with Bootstrap

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

A beautiful and functional CRUD (Create, Read, Update, Delete) application built with Django and styled with Bootstrap 5.

## Features

- **Modern UI**: Clean Bootstrap 5 interface with responsive design
- **Full CRUD Operations**:
  - Create new person records
  - Read/list all entries in a sortable table
  - Update existing records
  - Delete entries
- **Real-time counter**: Shows total records
- **User-friendly**: Confirmation for destructive actions

## Technologies Used

- Python 3.x
- Django 5.x
- Bootstrap 5
- Bootstrap Icons

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/doug-oliver/django-crud.git
   cd django-crud

   Set up virtual environment (recommended):

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
pip install -r requirements.txt
Run migrations:

bash
python manage.py migrate
Create superuser (optional for admin access):

bash
python manage.py createsuperuser
Run the development server:

bash
python manage.py runserver


django-crud/
├── core2/
│   ├── migrations/       # Database migrations
│   ├── templates/        # HTML templates
│   │   ├── index.html    # Main interface
│   │   └── update.html   # Edit form
│   ├── admin.py          # Admin configuration
│   ├── apps.py           # App configuration
│   ├── models.py         # Person model
│   ├── urls.py           # App URLs
│   └── views.py          # View functions
├── manage.py             # Django management script
└── requirements.txt      # Dependencies

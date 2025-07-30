# Django CRUD Application with Bootstrap
<img width="854" height="374" alt="image" src="https://github.com/user-attachments/assets/afa6289a-c324-4b86-8171-404527594bb6" />
<img width="638" height="297" alt="image" src="https://github.com/user-attachments/assets/9d61b997-1c48-406c-819d-4edab1134c9e" />




![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

A complete CRUD application with elegant Bootstrap 5 interface.

## Features
- Create, Read, Update, Delete operations
- Responsive Bootstrap 5 design
- Real-time record counter
- Confirmation dialogs for deletions
- Beautiful form validations

## Quick Start

1. Clone repo:
```bash
git clone https://github.com/doug-oliver/django-crud.git
cd django-crud

python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

django-crud/
├── core2/
│   ├── templates/
│   │   ├── index.html    # Main interface
│   │   └── update.html   # Edit form
│   ├── admin.py          # Admin config
│   ├── models.py         # Person model
│   ├── urls.py           # App URLs
│   └── views.py          # View logic
└── manage.py             # Django CLI



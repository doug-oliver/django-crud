# Django CRUD Application with Bootstrap
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

A complete CRUD application with elegant Bootstrap 5 interface.

<img width="857" height="378" alt="image" src="https://github.com/user-attachments/assets/50c5bbd2-d7cf-407e-9d36-dc01df06cb02" />
<img width="638" height="297" alt="image" src="https://github.com/user-attachments/assets/9d61b997-1c48-406c-819d-4edab1134c9e" />
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



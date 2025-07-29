from django.urls import path
from .views import home, save, update, edit, delete

urlpatterns = [
    path('', home, name='home'),
    path('save/', save, name='save'),
    path('update/<int:id>', update, name='update'),
    path('edit/<int:id>', edit, name='edit'),
    path('delete/<int:id>', delete, name='delete'),
]

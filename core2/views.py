from django.shortcuts import render, redirect
from .models import Person
# Create your views here.
def home(request):
    people = Person.objects.all()
    return render(request, 'index.html', {'people': people})

def save(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    Person.objects.create(name=name, age=age)
    people = Person.objects.all()
    return render(request, 'index.html', {'people': people})

def edit(request, id):
    person = Person.objects.get(id=id)
    return render(request, 'update.html', {'person': person})

def update(request, id):
    name = request.POST.get('name')
    age = request.POST.get('age')
    person = Person.objects.get(id=id)
    person.name = name
    person.age = age
    person.save()
    return redirect(home)

def delete(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return redirect(home)
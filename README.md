# Building a Django CRUD(Create, Retrieve, Update and Delete) Project Using Function-Based Views

Django is a powerful Python web framework that simplifies web development by providing a clean and pragmatic design. One of the most common tasks in web development is creating CRUD (Create, Read, Update, Delete) functionality for your application. In this article, we'll explore how to create a Django CRUD project using function-based views.

### Prerequisites

Before we dive into building our CRUD project, make sure you have the following prerequisites in place:

1. Python and Django: Ensure you have Python installed on your system. You can install Django using pip:
```python
pip install django
```

2. Database: Decide on the database you want to use. By default, Django uses SQLite, but you can configure it to use other databases like PostgreSQL, MySQL, or Oracle.

3. Text Editor or IDE: Choose a code editor or integrated development environment (IDE) of your preference. Popular choices include Visual Studio Code, PyCharm, or Sublime Text.

### Setting Up Your Django Project

Let's start by creating a new Django project and a new app within that project. Open your terminal and run the following commands:

```python
django-admin startproject crudproject
cd crudproject
python manage.py startapp crudapp
```

We've created a new project named "crudproject" and an app named "crudapp."

### Application Registration: you need to configure in your settings.py file

Make sure your app (myapp) is included in the INSTALLED_APPS list:

```python
INSTALLED_APPS = [
    # ...
    'myapp',
]
```

### Defining Models

In Django, models are Python classes that define the structure of your database tables. For our CRUD project, let's assume we want to manage a list of orders. Create a model for the orders in `crudapp/models.py`:

```python
from django.db import models

# Create your models here.
class Orders(models.Model):
    oid = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    price = models.FloatField()
    mail = models.EmailField()
    addr = models.CharField(max_length=50)
```

Now, it's time to create the database tables for our models. Run the following commands to create the migrations and apply them:

```python
python manage.py makemigrations
python manage.py migrate
```

###  Creating Forms

We mentioned using a form for creating and updating orders. You can define the form in `crudapp/forms.py`:

```python
from django import forms
from .models import Orders

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'

        labels = {
            'oid': 'Order ID',
            'fname' : 'First Name',
            'lname' : 'Last Name.' ,
            'price' : 'Price' ,
            'mail' : 'Email ID',
            'addr' : 'Address' ,
        }

        widgets  ={
            'oid' : forms.NumberInput(attrs={'placeholder': 'eg. 101'}),
            'fname' : forms.TextInput(attrs={'placeholder': 'eg. Prosenjeet'}),
            'lname' : forms.TextInput(attrs={'placeholder': 'eg. Shil'}),
            'price' : forms.NumberInput(attrs={'placeholder': 'eg. 10000'}),
            'mail' : forms.EmailInput(attrs={'placeholder': 'eg. abc@xyz.com'}),
            'addr' : forms.Textarea(attrs={'placeholder': 'eg. IN'}),
        }
```

### Creating Function-Based Views

Function-based views are a simple and straightforward way to handle CRUD operations in Django. In this example, we'll create views for creating, reading, updating, and deleting orders.

1. Create a Order (Create View)
In `crudapp/views.py`, define a view function for creating a new order:

```python
from django.shortcuts import redirect, render
from .forms import OrderForm
from .models import Orders

# Create your views here.
def orderFormView(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'crudapp/order.html'
    context = {'form': form}
    return render(request, template_name, context)
```

In this view, we handle both GET and POST requests. If it's a GET request, we render a form for creating a new order. If it's a POST request, we validate the form data and save the new order if it's valid.

2. Read Orders (List View)
Now, let's create a view to display a list of all books in `crudapp/views.py`:

```python
def showView(request):
    obj = Orders.objects.all()
    template_name = 'crudapp/show.html'
    context = {'obj': obj}
    return render(request, template_name, context)
```

This view retrieves all orders from the database and renders them using a template.


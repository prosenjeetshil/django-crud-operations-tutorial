# Building a Django CRUD (Create, Retrieve, Update and Delete) Project Using Function-Based Views

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

3. Update a Order (Update View)
To update a order, create a view in `crudapp/views.py`:

```python
def updateView(request, f_oid):
    obj = Orders.objects.get(oid=f_oid)
    form = OrderForm(instance=obj)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'crudapp/order.html'
    context = {'form': form}
    return render(request, template_name, context)
```

4. Delete a Order (Delete View)
Finally, let's create a view to delete a order in `crudapp/views.py`:

```python
def deleteView(request, f_oid):
    obj = Orders.objects.get(oid=f_oid)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    template_name = 'crudapp/confirmation.html'
    context = {'obj': obj}
    return render(request, template_name, context)
```

In this view, we confirm the order deletion with a confirmation page.

### Creating Templates
Now, create HTML templates for the views in the crudproject/templates directory. You'll need templates for the following views:

layout.html: for creating base html file with navbar.

Similarly, create HTML templates for the views in the crudproject/templates/crudapp directory. You'll need templates for the following views:

order.html: For the create and update forms.
show.html: For listing all orders.
confirmation.html: For confirming order deletion.

 Below, are the templates for base file and the three views we discussed earlier: 

`crudproject/templates/layout.html`

 ```html
<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    {% block title %}
    <title>Layout Page</title>
    {% endblock %}
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">CRUD APP</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
      
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
              <a class="nav-link" href="{% url 'order_url' %}">Add Orders<span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'show_url' %}">Show Orders</a>
            </li>
          </ul>
        </div>
      </nav>

    {% block content %}
    {% endblock %}
    
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
</body>
</html>
 ```

`crudproject/templates/crudapp/orders.html`

 ```html
{% extends 'layout.html' %}
{% load crispy_forms_tags %}

{% block title %}
    <title>Add Page</title>
{% endblock %}

{% block content %}
<center><h1>Order Form</h1></center>
<div class="container">
    <form method="post" class="jumbotron">
        {% csrf_token %}
        {{form|crispy}}
        <input type="submit" value="Place Order" class="btn btn-success">
    </form>
</div>
{% endblock %}
 ```

`crudproject/templates/crudapp/show.html`

 ```html
{% extends 'layout.html' %}

{% block title %}
    <title>Show Page</title>
{% endblock %}

{% block content %}
<center><h1>Show Orders</h1></center>
<table class="table">
    <thead>
      <tr>
        <th scope="col">Order ID</th>
        <th scope="col">First Name</th>
        <th scope="col">Last Name</th>
        <th scope="col">Price</th>
        <th scope="col">Email ID</th>
        <th scope="col">Address</th>
        <th scope="col">Actions</th>
      </tr>
    </thead>
    <tbody>
    {% for i in obj %}
      <tr>
        <td>{{i.oid}}</td>
        <td>{{i.fname}}</td>
        <td>{{i.lname}}</td>
        <td>{{i.price}}</td>
        <td>{{i.mail}}</td>
        <td>{{i.addr}}</td>
        <td>
            <button class="btn btn-warning"><a href="{% url 'update_url' i.oid %}">Update</a></button>&nbsp;&nbsp;
            <button class="btn btn-danger"><a href="{% url 'delete_url' i.oid %}">Delete</a></button>
        </td>
      </tr>
    {% endfor %}
    </tbody>
  </table>
{% endblock %}

 ```

 `crudproject/templates/crudapp/confirmation.html`

```html
{% extends 'layout.html' %}

{% block title %}
    <title>Confirmation Page</title>
{% endblock %}

{% block content %}
    <div class="container">
        <form class="jumbotron" method="post">
            {% csrf_token %}
            <h2>Are you sure you want to delete this data? </h2>
            <input type="submit" value="YES" class="btn btn-danger">
            <button class="btn btn-success"><a href="{% url 'show_url' %}">No</a></button>
        </form>
    </div>
{% endblock %}
```

### Add Bootstrap Crispy forms for styling form and navbar

```python
INSTALLED_APPS = [
    # ...
    'crispy_forms',
    'crispy_bootstrap5',
]

CRISPY_TEMPLATE_PACK = 'bootstrap5'
```

### Wiring Up URLs

Finally, configure the URLs for your views. In your project's crudproject/urls.py file, include the URLs for the crudapp app:


```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crudapp.urls'))
]
```

Then, in your app's crudpp/urls.py file, define the URLs for your views:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('ofv/', views.orderFormView, name='order_url'),
    path('sv/', views.showView, name='show_url'),
    path('up/<int:f_oid>', views.updateView, name= 'update_url'),
    path('del/<int:f_oid>', views.deleteView, name= 'delete_url'),
]
```

### Testing Your CRUD Project

With everything set up, you can start your Django development server:

```python
python manage.py runserver
```

Visit http://localhost:8000/ in your browser, and you should be able to create, read, update, and delete orders in your Django CRUD project using function-based views.

In this tutorial, you've learned how to create a Django CRUD project using function-based views. You can further enhance your project by adding features like authentication, pagination, or search functionality. Django's flexibility and extensive ecosystem make it a great choice


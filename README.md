# Getting started with Django

## Install Django:

Install [Django](https://docs.djangoproject.com/en/3.2/topics/install/) via pip:

`pip install Django`

Use pip3 if you are using python3:

`pip3 install Django`

On Windows, you may need to use the Python launcher (py):

`py -m pip install Django`

## Task 1: Create a new project

`django-admin startproject my_project`

This command automatically creates a Django project. It creates a folder with an initial structure that will help us to get started with the process of building a web application.

https://django-project-skeleton.readthedocs.io/en/latest/structure.html 

The newly created project has some helpful files, such as:

*my_project/manage.py*

We do not need to modify this file. Instead, we will use this script to execute commands and perform different activities, such as running the web server.

The *my_project* folder has files relevant to all the project apps, such as:
- settings.py: contains default settings
- urls.py: acts as an index or "table of contents" that controls the content rendered under the URLs served by our applications.

### Task 2: Run the Django server

`python manage.py runserver`

Notice the line that says: *Starting development server at http://127.0.0.1:8000/*

It means, we have now a web server running in our local computer that we can access with the IP address 127.0.0.1 and port 8000. 

## Task 3: Create the hello app

`python manage.py startapp hello`

This command creates a new directory with several files inside.

Edit *my_project/settings.py*:

Add the recently created *hello* app to the INSTALLED_APPS list:

```python
INSTALLED_APPS = [
    'hello',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Edit *my_project/hello/views.py*:

This file contains the configurations that determine what content is rendered to the users. Add the following code:

```python
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hellow, world!")
```

Edit *my_project/hello/urls.py*:

Add the following code:

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index")
]
```

Edit *my_project/my_project/urls.py*:

Update its content with the following code:

```python
...

from django.urls import path, include

urlpatterns = [
    path('hello/', include("hello.urls")),
    path('admin/', admin.site.urls),
]
```

## Task 4: Customize the greet message

Edit *my_project/hello/views.py*:

```python
name = "Jose"

def welcome(request):
    return HttpResponse(f"Welcome to { name }'s page")
```

Edit *my_project/hello/urls.py*:

Add the following code:

```python
urlpatterns = [
    path("", views.index, name="index"),
    path("welcome", views.welcome, name="welcome")   
]
```

## Task 5: Create a template

Note that at at this point, our app generates raw text, not HTML.

Create the following structure that defines a namespace for the templates of our application:

*my_project/hello/templates/hello*

Add a file called *index.html*:

*my_project/hello/templates/hello/index.html*

```html
<!DOCTYPE html>
<html lang="en">
    <head> 
        <title>My Site</title>
    </head>
    <body>
        <h1>Hello world!</h1>
    </body>
</html>
```

We also need to specify the same structure when including the template in the view.

Update *my_project/hello/views.py*:

```python
def index(request):
    return render(request, "hello/index.html")
```

## Task 6: Add context to templates

Add a new view that renders a template including a context parameter.

Update *my_project/hello/views.py*:

```python
def greet(request):
    return render(request, "hello/greet.html", {
        "name": name
    }
)
```

Add the template *greet.html* for the *greet* view under *my_project/hello/templates/hello/*:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>My site</title>
    </head>
    <body>
        <h1>Welcome to {{ name }}'s page</h1>
    </body>
</html>
```

Remember to update the *my_project/hello/urls.py* file contents to add the following code:

```python
urlpatterns = [
    path("", views.index, name="index"),
    path("welcome", views.welcome, name="welcome"),
    path("greet", views.greet, name="greet")
]
```

## Task 7: Add conditional statements to templates

Update *my_project/hello/views.py*: 

```python

...
from datetime import datetime
...

period = f"{datetime.today(): %p}"
def greet(request):
    return render(request, "hello/greet.html", {
        "name": name,
        "period": period
    })
```

Update *my_project/hello/templates/hello/greet.html*:

```html
{% if period == "AM" %}
    How glorious a greeting the sun gives the mountains!        
{% else %}
    Don't tell your friends about your indigestion. 'How are you' is a greeting, not a question.
{% endif %}
```

To make this view work properly, you need to update the TIME_ZONE paramater in the file *my_project/my_project/settings.py*:

```
TIME_ZONE = 'America/Los_Angeles'
```

## Task 8: Add iteration statements to templates

Update *my_project/hello/views.py*: 

```python
tasks = [
    {"class": "CIS 3610-02", "time": "Tue 6:00 - 8:45 PM"},
    {"class": "CIS 3610-03", "time": "Wed 6:00 - 8:45 PM"}
]
def schedule(request):
    return render(request, "hello/schedule.html", {
        "tasks": tasks
    })
```

Add a new template:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
            <title>My site</title>
    </head>
    <body>
        <h1>My Schedule</h1>
        <ul>
            {% for item in tasks %}
            <li>{{ item.class}}: {{ item.time}}</li>
            {% endfor %}
        </ul>
    </body>
</html>
```

Remember to update the *my_project/hello/urls.py* file contents to add the following code:

```python
urlpatterns = [
    path("", views.index, name="index"),
    path("welcome", views.welcome, name="welcome"),
    path("greet", views.greet, name="greet"),
    path("schedule", views.schedule, name="schedule"),
]
```

## Task 9: Add static files

Add the directory structure */static/hello/* under the app folder *my_project/hello/* 

Then, add the *styles.css* stylesheet file under the *my_project/hello/static/hello/* folder:

```css
h1 {
    color: blue;
} 
```

Update *my_project/hello/templates/hello/schedule.html*:

```html
{% load static %}
<!DOCTYPE html>
<html>
    <head>
            <title>My Schedule</title>
            <link href="{% static 'hello/styles.css' %}" rel="stylesheet">
    </head>
    ...
</html>
```

## Task 10: Template Inheritance

Use a common template which other templates will inherit. In this way, I just need to write what differs in each page.

Add a the file *layout.html* to *my_project/hello/templates/hello/*

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>My Site</title>
    </head>
    <body>
        {% block body %}
        {% endblock %}
    </body>
</html>
```

Update *my_project/hello/templates/hello/index.html* and *my_project/hello/templates/hello/greet.html*

For example:

```html
{% extends "hello/layout.html" %}

{% block body %}
    <h1>Hello world!</h1>
{% endblock %}
````

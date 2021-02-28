## Referencias de Github
https://lemoncode.net/lemoncode-blog/2017/12/12/git-y-visual-studio-code

## Para crear venv
python -m venv [nombre ambiente]

## Para activar venv (en windows)
tutorial-env\Scripts\activate.bat


## Django
https://www.djangoproject.com/

MCV --> MTV (Model [Datos], Template [Vista, es el HTML], View [Es el controller, el que orquesta vista y datos])

## Para crear un proyecto en Django
    django-admin startproject [nombre_proyecto]

## Para crear una app
    python manage.py startapp [nombre_app]

## A nivel root del proyecto esta: manage.py

Dentro del folder del proyecto esta urls.py en este archivo se envia al urls.py de la main_app
Dentro de app esta: urls.py y views.py

La view.py es la mas importante que interactua con el Model y con el Template.
Para el Template (que es el html) se pasan datos desde la view usando el context.

El Model se crea en models.py y debe cargar la libreria from django.db import models
Adicionanlmente los modelos que se crean deben heredar de la clase `models.Model`
ejemplo: `class Treasure(models.Model):`
Donde tambien se usan tipos de datos de Django para las variables, así es compatible con `SQL` y `Python`
https://docs.djangoproject.com/en/3.1/ref/models/fields/#field-types

Cada vez que se crea o actualiza un Model se debe hacer

    python manage.py makemigrations
    python manage.py migrate
Se puede hacer un paso intermedio para ver el codigo SQL generado

    python manage.py sqlmigrate <app_name> <migration_number>
    ex: python manage.py sqlmigrate main_app 0001

Para interactuar con la BD una alternativa es usar la consola de Django, a la cual se accede con:

    python manage.py shell

Luego hay que importar en la consola el modelo 
    
    from <app_name>.models import <model_name>
Algunas sentencias de python para operar con la BD

    Treasure.objects.all()  # SELECT * FROM
    Treasure.objects.filter(location='Orlando, FL') # WHERE or LIMIT
    Treasure.objects.get(pk=1) # Para un objeto especifico


## Para iniciar el server local
    python manage.py runserver

## Para Crear un superadmin que se usa en el Admin autogenerado por Django

    python manage.py createsuperuser

Tambien para administrar el Model creado desde la interfaz de administracion se debe registrar en admin.py el modelo

    from .models import Treasure # Importando el modelo
    admin.site.register(Treasure) # Luego registrandolo


user: zondo / pass:1234


# django_Rest

comandos


    django-admin startproject REST .
	python manage.py runserver <3000> cancelar serve contrl+c
    pip install djangorestframework
    python manage.py makemigrations
    python manage.py migrate
    pip freeze > requirements.txt


despliegue


    pip install dj-database-url psycopg2-binary
    pip install whitenoise[brotli]
    chmod a+x build.sh
    pip install gunicorn


info


    creacion de serializer
    creacion de viewset
    render.com https://render.com/docs/deploy-django
        tipo de operacion
        base de datos
        key secretas
        archivos estaticos
        contenido estatico

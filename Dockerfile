FROM edoburu/django-base-images:py37-stretch-build

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD['python', 'manage.py', 'runserver']
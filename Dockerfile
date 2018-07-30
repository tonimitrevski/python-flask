FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN pip install flask-sqlalchemy
RUN pip install Flask-WTF
RUN pip install psycopg2
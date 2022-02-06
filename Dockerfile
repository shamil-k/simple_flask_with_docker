From ubuntu

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install flask
RUN mkdir /opt/app

WORKDIR /opt/app

COPY . /opt/app

# ENTRYPOINT FLASK_APP = app.py flask run --host 127.0.0.1 --port 5000

CMD ["python3", "app.py"]
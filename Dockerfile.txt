FROM ubuntu

RUN apt update
RUN apt-get upgrade
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install Flask
COPY . venv/app

EXPOSE 5000
RUN pip install -r requirements.txt

CMD python3 venv/app/app.py

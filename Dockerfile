FROM ubuntu

RUN apt update
RUN apt-get upgrade -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install Flask
RUN pip3 install nltk
RUN python3 -m nltk.downloader punkt
RUN python3 -m nltk.downloader stopwords
RUN pip3 install textdistance
RUN pip3 install pymorphy2
RUN pip3 install gensim

COPY . /app
WORKDIR /app

EXPOSE 5000
RUN pip freeze > requirements.txt

CMD python3 /app/app.py

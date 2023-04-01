FROM python:3

ADD requirements.txt /

RUN pip install -r requirements.txt

ADD first.py /

CMD [ "python", "./first.py" ]
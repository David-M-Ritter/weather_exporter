FROM python:3.12

RUN pip install requests

ADD metric_import.py .

CMD [ "python", "./metric_import.py" ]
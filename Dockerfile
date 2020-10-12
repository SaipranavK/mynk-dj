FROM python:3.6
ENV PYTHONUNBUFFERED=1
RUN mkdir /mynk-dj
WORKDIR /mynk-dj
COPY requirements.txt /mynk-dj/
RUN pip install -r requirements.txt
COPY . /mynk-dj/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
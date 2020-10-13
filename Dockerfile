FROM python:3.6
ENV PYTHONUNBUFFERED=1
RUN mkdir /mynk
WORKDIR /mynk
COPY requirements.txt /mynk/
RUN pip install -r requirements.txt
COPY . /mynk/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
FROM python:3.6-alpine

LABEL maintainer=PiStevGa

COPY requirements.txt /requirements.txt

#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

COPY db /db

COPY src /src
WORKDIR /src

RUN echo $(pwd)
RUN echo $(ls -al)

CMD ["gunicorn", "-c", "gunicorn.py", "wsgi:application"]

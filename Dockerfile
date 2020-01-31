FROM python:3.6-alpine

MAINTAINER PiStevGa
  
COPY src /src
COPY requirements.txt /requirements.txt

#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

WORKDIR /src

RUN echo $(pwd)
RUN echo $(ls -al)

CMD ["gunicorn", "-c", "gunicorn.py", "wsgi:application"]

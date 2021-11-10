FROM python:3.10-alpine3.14
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1

#requirements for pillow
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev


#install requirements
RUN apk install --upgrade pin
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
WORKDIR /app/onlineshop

ENTRYPOINT ["python", "manage.py"]
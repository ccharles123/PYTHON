#creamos nuestro contenedor que cuando inicie sea con Python 3.8:
FROM python:3.9

#creamos un directorio con el nombre app:
WORKDIR /app

#copiamos el archivo del entorno local al nuestro contenedor, se debe colocar doble, uno es lado local y otro es el contenedor:
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

#para que el contenedor se mantenga encendido y corriendo se digita:
CMD bash -c "while true; do sleep 1; done"
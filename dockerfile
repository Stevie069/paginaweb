# Utilizar una imagen base oficial de Python
FROM python:3.9

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . /app

# Instalar las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 5000 para la aplicación Flask
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]

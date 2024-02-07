# Usar la imagen base oficial de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requisitos e instalar las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar los archivos de tu proyecto FastAPI
COPY ./app /app

# Exponer el puerto que utiliza tu aplicación
EXPOSE 8000

# Ejecutar Uvicorn con live reload para el desarrollo
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

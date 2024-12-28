# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Crea un entorno virtual dentro del contenedor
RUN python -m venv /venv

# Activa el entorno virtual e instala las dependencias
RUN /venv/bin/pip install --no-cache-dir -r requirements.txt

# Copia todo el código de la aplicación al contenedor
COPY . .

# Establece la variable de entorno para usar el venv
ENV PATH="/venv/bin:$PATH"

# Expone el puerto en el que la aplicación Flask correrá
EXPOSE 5000

# Establecer el comando para ejecutar la aplicación
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]


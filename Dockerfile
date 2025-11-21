# 1. Usamos una imagen base oficial de Python ligera (slim)
FROM python:3.10-slim

# 2. Establecemos variables de entorno para optimizar Python en Docker
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3. Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# 4. Copiamos PRIMERO los requirements. 
COPY requirements.txt .

# 5. Instalamos las dependencias
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 6. Copiamos el resto del código de la aplicación
COPY . .

# 7. Creamos un usuario no-root por seguridad
RUN adduser --disabled-password --gecos '' appuser
USER appuser

# 8. Exponemos el puerto donde correrá FastAPI (por defecto 8000)
EXPOSE 8000

# 9. Comando para arrancar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
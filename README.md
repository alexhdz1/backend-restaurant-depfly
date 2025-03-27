# Restaurante y Reviews API

Este proyecto es una API REST desarrollada en Django que permite administrar Restaurantes y sus Reviews, además cuenta con documentación integrada utilizando Swagger.

---

## Requisitos previos:

- Python 3.9 o superior
- Pip
- Virtualenv (opcional pero recomendado)
- Docker y Docker Compose (opcional)

---

## Instalación

### 1. Clonar el repositorio

git clone <url_del_repositorio> cd <nombre_carpeta_proyecto>


---

### 2. Crear y activar entorno virtual

Windows:

python -m venv venv .\venv\Scripts\activate


Linux / macOS:

python3 -m venv venv source venv/bin/activate


---

### 3. Instalar dependencias

pip install -r requirements.txt


---

### 4. Migraciones de base de datos

python manage.py makemigrations python manage.py migrate


---

### 5. Crear usuario administrador (opcional)

python manage.py createsuperuser


---

## 🖥️ Ejecutar Servidor (local)

python manage.py runserver


- **URL del servidor local:**  
http://localhost:8000

---

## 🛠️ Docker (opcional pero recomendado)

### Opción rápida usando script `deploy.sh` ⚡️

Si quieres ejecutar rápidamente todo con Docker, simplemente ejecuta:

chmod +x .deploy.sh ./.deploy.sh


### Alternativa manual

## 🛠️ Docker (opcional pero recomendado)

### 1. Construir la imagen y levantar contenedores

docker-compose build docker-compose up -d


### 2. Acceso usando Docker

- **URL del servidor Docker:**  
http://localhost:8000

---

## 📚 Documentación Swagger (drf-yasg)

Para ver documentación interactiva visita:

- **Swagger UI:**  
http://localhost:8000/swagger/

- **Redoc UI:**  
http://localhost:8000/redoc/

---

## 📂 Estructura del Proyecto

project_root/ │ ├── config/ │ ├── settings.py │ ├── urls.py │ └── ... ├── restaurant/ │ ├── models.py │ ├── serializers.py │ ├── views.py │ └── ... ├── review/ │ ├── models.py │ ├── serializers.py │ ├── views.py │ └── urls.py ├── media/ (imágenes subidas) ├── manage.py ├── requirements.txt ├── Dockerfile ├── docker-compose.yml └── venv/


---

## 📝 Ejemplo de uso:

### Crear un Restaurante (POST)

**URL:**  
POST /api/reviews/restaurant/


**Datos:** (`multipart/form-data`)  

| Campo | Valor Ejemplo                |
|-------|------------------------------|
| name  | Restaurante Alex             |
| url   | https://restaurantealex.com  |
| image | archivo_imagen.png           |

---

## ✅ Listo para empezar

¡Tu proyecto está listo para ejecutarse localmente! 🎉

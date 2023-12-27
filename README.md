# CrudBasico

Crud Básico creado con FastAPI

## Descripción

Este proyecto es una aplicación CRUD básica desarrollada con FastAPI, un marco web moderno y rápido para construir APIs con Python.

## Características

- **CRUD:** Crear, leer, actualizar y eliminar publicaciones.
- **Atributos de Publicación:**
  - Identificador único
  - Título
  - Autor
  - Contenido
  - Fecha de creación
  - Estado de publicación
- **Funcionalidades:**
  - Obtener la lista de todas las publicaciones.
  - Obtener detalles de una publicación por su ID.
  - Agregar nuevas publicaciones.

## Requisitos

- Python 3.7 o superior
- Instalar las dependencias del proyecto: `pip install -r requirements.txt`

## Ejecución

1. Clona el repositorio: `git clone https://github.com/tuusuario/CrudBasico.git`
2. Entra al directorio del proyecto: `cd CrudBasico`
3. Ejecuta la aplicación: `uvicorn main:app --reload`

La aplicación estará disponible en [http://localhost:8000](http://localhost:8000). Puedes explorar la API utilizando herramientas como [Swagger UI](http://localhost:8000/docs) o [ReDoc](http://localhost:8000/redoc).

## Endpoints

- **GET /posts:** Obtiene la lista de todas las publicaciones.
- **GET /post/{id}:** Obtiene detalles de una publicación por su ID.
- **POST /posts:** Agrega una nueva publicación.
- **DELETE /posts/{id}:** Elimina una publicación por su ID.
- **PUT /posts/{id}:** Actualiza una publicación por su ID.

## Ejemplo de Uso

### Agregar Nueva Publicación

```bash
curl -X POST "http://localhost:8000/posts" -H "Content-Type: application/json" -d '{"title":"Nueva Publicacion","author":"Autor","content":"Contenido de la publicacion"}'
```

### Obtener Lista de Publicaciones

```bash
curl "http://localhost:8000/posts"
```

### Obtener Detalles de una Publicación por ID

```bash
curl "http://localhost:8000/post/{id}"
```

### Eliminar Publicación por ID

```bash
curl -X DELETE "http://localhost:8000/posts/{id}"
```

### Actualizar Publicación por ID

```bash
curl -X PUT "http://localhost:8000/posts/{id}" -H "Content-Type: application/json" -d '{"title":"Nuevo Titulo","author":"Nuevo Autor","content":"Nuevo Contenido"}'
```

## Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras algún problema o tienes alguna mejora, no dudes en abrir un [issue](https://github.com/tuusuario/CrudBasico/issues) o enviar un [pull request](https://github.com/tuusuario/CrudBasico/pulls).

## Contacto 📧

- **Desarrollador 🧑‍💻:** Gary Alexander Campusano Paredes
- **LinkedIn: [Gary Alexander Campusano Paredes](https://www.linkedin.com/in/gary-alexander-campusano-paredes-87a28724a/)**
- **Correo Electrónico 📧:** ingcampusano@outlook.com

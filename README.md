# Proyecto Banco Original

Este es un proyecto de ejemplo de una aplicación bancaria simple, desarrollado en Django. El objetivo principal es la gestión de clientes, diferenciando entre Personas Físicas y Personas Jurídicas.

El proyecto ha sido estructurado siguiendo principios de **Arquitectura Limpia** y **SOLID** para garantizar que el código sea mantenible, escalable y profesional.

## Principios Arquitectónicos

El código sigue dos principios fundamentales:

1.  **Capa de Servicios:** La lógica de negocio está aislada en una "capa de servicios" (`gestion_clientes/services`). Las vistas de Django son delgadas y solo orquestan el flujo de datos, delegando la lógica real a los servicios. Esto cumple con el Principio de Responsabilidad Única (SRP) y facilita las pruebas.

2.  **Configuración Desacoplada:** Las configuraciones sensibles (como `SECRET_KEY` y `DEBUG`) se gestionan a través de variables de entorno utilizando `python-decouple`. Los secretos se almacenan en un archivo `.env` que no se incluye en el control de versiones.

## Instalación y Puesta en Marcha

Sigue estos pasos para configurar el entorno de desarrollo local.

### 1. Prerrequisitos

*   Python 3.x
*   Git

### 2. Configuración del Entorno

1.  **Clona el repositorio** (si aún no lo has hecho).

2.  **Crea y activa un entorno virtual**:
    ```bash
    # Navega a la raíz del proyecto (donde está este README)
    python -m venv venv
    # En Windows
    .\venv\Scripts\activate
    ```

3.  **Instala las dependencias**:
    ```bash
    pip install -r banco_original/requirements.txt
    ```

4.  **Crea el archivo de entorno**:
    *   En el directorio `banco_original`, crea un archivo llamado `.env`.
    *   Copia y pega el siguiente contenido en él:
        ```
        SECRET_KEY='tu-clave-secreta-aqui'
        DEBUG=True
        ```
    *   **Importante:** Reemplaza `tu-clave-secreta-aqui` por una nueva clave secreta de Django.

5.  **Aplica las migraciones** de la base de datos:
    ```bash
    # Asegúrate de que tu terminal está en el directorio raíz del proyecto
    python banco_original/manage.py migrate
    ```

### 3. Ejecutar el Servidor de Desarrollo

Una vez completada la configuración, puedes iniciar el servidor de Django:

```bash
python banco_original/manage.py runserver
```

La aplicación estará disponible en `http://127.0.0.1:8000/`.

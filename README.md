# API Rest Inventario (Python Vanilla)

Servidor HTTP construido exclusivamente con la biblioteca estándar de Python (sin frameworks externos como Flask o Django) para la gestión de productos e inventario con persistencia en MySQL.

---

## 📋 Tabla de Contenidos
- [API Rest Inventario (Python Vanilla)](#api-rest-inventario-python-vanilla)
  - [📋 Tabla de Contenidos](#-tabla-de-contenidos)
  - [🚀 Requisitos Previos](#-requisitos-previos)
  - [🛠️ Instalación y Configuración](#️-instalación-y-configuración)
    - [1. Base de Datos](#1-base-de-datos)
    - [2. Entorno Virtual e Instalación](#2-entorno-virtual-e-instalación)
    - [3. Variables de Entorno](#3-variables-de-entorno)
  - [⚙️ Ejecución del Servidor](#️-ejecución-del-servidor)
  - [📡 Endpoints de la API](#-endpoints-de-la-api)
  - [🧪 Pruebas con Postman](#-pruebas-con-postman)

---

## 🚀 Requisitos Previos

Asegúrate de tener instalados los siguientes componentes antes de iniciar:

* **Python 3.8+**
* **Servidor MySQL**
* **Postman** (recomendado para probar las rutas)

---

## 🛠️ Instalación y Configuración

### 1. Base de Datos
Crea la base de datos e importa el esquema inicial ejecutando el archivo SQL provisto:

```bash
mysql -u tu_usuario -p < schema-and-data.sql
```

### 2. Entorno Virtual e Instalación
Se recomienda aislar las dependencias dentro de un entorno virtual de Python:

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Linux / macOS:
source venv/bin/activate
# En Windows:
.\venv\Scripts\activate

# Instalar dependencias requeridas
pip install -r requirements.txt
```

### 3. Variables de Entorno
Crea un archivo `.env` en la raíz del proyecto basándote en la siguiente estructura:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=tu_contraseña
DB_NAME=inventario_db
DB_PORT=3306
```

---

## ⚙️ Ejecución del Servidor

Inicia el servidor con el comando principal de Python:

```bash
python main.py
```

El servidor quedará escuchando peticiones en:
`http://localhost:8000`

---

## 📡 Endpoints de la API

| Método | Ruta | Descripción |
| :--- | :--- | :--- |
| `GET` | `/api/productos` | Obtiene el listado completo de productos |
| `POST` | `/api/productos` | Crea un nuevo producto |
| `PUT` | `/api/productos/{id}` | Actualiza un producto existente por su ID |
| `DELETE` | `/api/productos/{id}` | Elimina un producto por su ID |

---

## 🧪 Pruebas con Postman

Dado que el panel de administración frontend se encuentra en desarrollo, la API se puede testear de manera óptima utilizando Postman:

1. Abre **Postman**.
2. Haz clic en la opción **Import** (esquina superior izquierda).
3. Selecciona el archivo JSON incluido en el repositorio: `postman-export-....json`.
4. Ejecuta las peticiones `GET`, `POST`, `PUT` y `DELETE` directamente.
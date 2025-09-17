# Proyecto Créditos - Herramienta Web en Flask

## Descripción

Aplicación web desarrollada en **Python Flask** para registrar, listar, editar y eliminar créditos, además de visualizar gráficas del total de créditos otorgados.
Usa **SQLite** como base de datos y **HTML/CSS/JavaScript** para la interfaz.

## Características

* Registro de nuevos créditos mediante un formulario.
* Listado de créditos en tabla con opciones de **editar** y **eliminar**.
* Validaciones básicas de campos obligatorios y formatos.
* Visualización de **gráfica de créditos otorgados** por fecha.

## Tecnologías usadas

* Python 3.10+
* Flask
* SQLite
* HTML5 / CSS3 / JavaScript
* Chart.js (para la gráfica)

## Estructura del proyecto

```
proyecto_creditos/
│
├── app.py                 # Archivo principal de Flask
├── creditos.db            # Base de datos SQLite (no subir al repositorio)
├── templates/             # Archivos HTML
│   ├── nuevo.html
│   ├── lista.html
│   ├── editar.html
│   └── grafica.html
├── static/                # Archivos estáticos (CSS, JS, imágenes)
│   └── style.css
└── README.md
```

## Instalación y ejecución

2. Crear y activar un entorno virtual:

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

3. Instalar Flask:

```bash
pip install Flask
```

4. Ejecutar la aplicación:

```bash
python app.py
```

5. Abrir en el navegador:

```
http://127.0.0.1:5000/creditos/nuevo
```

## Uso

1. **Registrar crédito:** Completa el formulario en `/creditos/nuevo`.
2. **Listar créditos:** Ve a `/creditos` para ver la tabla con opciones de editar y eliminar.
3. **Editar crédito:** Haz clic en “Editar” en la tabla.
4. **Eliminar crédito:** Haz clic en “Eliminar” en la tabla.
5. **Ver gráfica:** Ve a `/creditos/grafica` para ver el total de créditos por fecha.


# Clínica Vida Salud

Este proyecto gestiona la base de datos y la lógica para la clínica **Vida Salud** utilizando Python y MySQL.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:
* Python 3.x
* XAMPP (con el servicio de MySQL activo)

## Instalación y Configuración

Sigue estos pasos en tu terminal para configurar el entorno y la base de datos:

### 1. Instalar dependencias
Instala el conector nativo de MySQL para Python (`MySQLdb`):

```
pip install mysqlclient
```

### 2. Preparar la base de datos
Navega al directorio del proyecto e importa los scripts SQL utilizando el cliente de MySQL de XAMPP:

```
# Cambiar al directorio del proyecto
cd downloads\clinica_vida_salud

# Crear la estructura de la base de datos
c:\xampp\mysql\bin\mysql -u root < script_creacion.sql

# Poblar la base de datos con datos de prueba
c:\xampp\mysql\bin\mysql -u root < script_poblado.sql
```

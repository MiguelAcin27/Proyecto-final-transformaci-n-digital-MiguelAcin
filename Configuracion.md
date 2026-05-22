Paso 1: Instalar las dependencias obligatorias
Bash
python -m pip install flask mysql-connector-python


Paso 2: Configurar la Base de Datos
Abre tu servidor MySQL.

Crea la base de datos ejecutando el siguiente script SQL:

SQL
CREATE DATABASE modas_ejea_db;
USE modas_ejea_db;

CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL
);
Edita el archivo database_config.py con las credenciales de tu servidor local.

Paso 3: Ejecutar la aplicación
Bash
python app.py

--Crea la Base de datos de SkyRoute
CREATE DATABASE IF NOT EXISTS skyroute_db;
--Seleccionar base de datos para todas las operaciones subsiguientes
USE skyroute_db;

--Tabla de clientes
CREATE TABLE IF NOT EXISTS clientes (
id_cliente INT AUTO_INCREMENT PRIMARY KEY,
razon_social VARCHAR(255) NOT NULL,
cuit VARCHAR(20) NOT NULL,
correo_electronico VARCHAR(255) NOT NULL
);

--Tabla de Destinos
CREATE TABLE IF NOT EXISTS destinos (
id_destino INT AUTO_INCREMENT PRIMARY KEY,
ciudad VARCHAR(100) NOT NULL,
pais VARCHAR(100) NOT NULL,
costo_base DECIMAL(10, 2) NOT NULL
);

--Tabla de ventas
CREATE TABLE IF NOT EXISTS ventas (
    id_venta INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_destino INT NOT NULL,
    fecha_venta DATETIME NOT NULL,
    estado VARCHAR(50) DEFAULT `Activa`,--`Activa`, `Cancelada`
    fecha_anulacion DATETIME, -- Campo para el de arrepentimiento
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_destino) REFERENCES destinos(id_destino)
);

-- 1. Listar todos los clientes.[cite: 17]
SELECT * FROM clientes;

-- 2. Mostrar las ventas realizadas en una fecha específica (ej: '2025-06-03').[cite: 18]
SELECT * FROM ventas WHERE DATE(fecha_venta) = '2025-06-03';
-- 3. obtener la ultima venta de cada cliente y su fecha.[cite: 19]
SELECT
    c.razon_social,
    MAX(v.fecha_venta) AS ultima_venta_fecha,
    (SELECT costo_total FROM ventas WHERE id_cliente = c.id_cliente ORDER BY fecha_venta DESC LIMIT 1) AS costo_ultima_ venta
 FROM
    clientes c
JOIN
    ventas v ON c.id_cliente = v.id_cliente
GROUP BY
    c.id_cliente, c.razon_social;

-- 4. Listar todos los destinos que empiezan con “S”. [cite: 19]
SELECT * FROM destinos WHERE ciudad LIKE 'S%';

-- 5. Mostrar cuántas ventas se realizaron por país. [cite: 20]
SELECT
    d.pais,
    COUNT(v.id_venta) AS total_ventas
FROM
    ventas v
JOIN
    destinos d ON v.id_destino = d.id_destino
GROUP BY
    d.pais
ORDER BY
    total_ventas DESC;
    
CREATE DATABASE inventario;

USE inventario;


CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL
);

INSERT INTO productos (nombre, categoria, precio, stock) VALUES
('Memoria SD 240gb', 'Almacenamiento', 130.00, 4),
('Teclado mecánico', 'Periféricos', 150.00, 10),
('Mouse inalámbrico', 'Periféricos', 80.50, 15),
('Monitor 24 pulgadas', 'Monitores', 650.00, 5),
('Laptop Lenovo', 'Computadoras', 2500.00, 3),
('Memoria USB 64GB', 'Almacenamiento', 35.90, 20),
('Disco SSD 1TB', 'Almacenamiento', 320.00, 8);


SELECT * FROM productos;


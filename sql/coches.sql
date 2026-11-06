-- Reto 4: base de datos de coches
CREATE DATABASE IF NOT EXISTS bdcoches;
USE bdcoches;

DROP TABLE IF EXISTS coches;
CREATE TABLE coches (
  id     INT AUTO_INCREMENT PRIMARY KEY,
  marca  VARCHAR(50)  NOT NULL,
  modelo VARCHAR(50)  NOT NULL,
  color  VARCHAR(30)  NOT NULL,
  km     INT          NOT NULL,
  precio DECIMAL(10,2) NOT NULL
);

INSERT INTO coches (marca, modelo, color, km, precio) VALUES
('Toyota', 'Corolla', 'Blanco', 45000, 15000.00),
('Honda', 'Civic', 'Negro', 60000, 17000.00),
('Ford', 'Focus', 'Azul', 50000, 14000.00),
('Chevrolet', 'Malibu', 'Rojo', 70000, 16000.00),
('Nissan', 'Sentra', 'Gris', 55000, 15500.00),
('Volkswagen', 'Jetta', 'Blanco', 40000, 16500.00),
('Hyundai', 'Elantra', 'Negro', 45000, 14500.00),
('Kia', 'Rio', 'Azul', 30000, 13500.00),
('Mazda', 'Mazda3', 'Rojo', 48000, 15800.00),
('Subaru', 'Impreza', 'Gris', 53000, 16800.00),
('BMW', 'Serie 3', 'Blanco', 75000, 28000.00),
('Mercedes-Benz', 'Clase C', 'Negro', 82000, 32000.00),
('Audi', 'A4', 'Azul', 69000, 29000.00),
('Lexus', 'IS', 'Rojo', 77000, 31000.00),
('Tesla', 'Model 3', 'Blanco', 25000, 45000.00),
('Jeep', 'Cherokee', 'Verde', 85000, 20000.00),
('Dodge', 'Charger', 'Negro', 62000, 26000.00),
('Ford', 'Mustang', 'Rojo', 54000, 27000.00),
('Chevrolet', 'Camaro', 'Amarillo', 50000, 26500.00),
('Nissan', 'Altima', 'Gris', 72000, 17500.00),
('Hyundai', 'Tucson', 'Azul', 41000, 19000.00),
('Kia', 'Sportage', 'Blanco', 38000, 18500.00),
('Toyota', 'RAV4', 'Negro', 60000, 22500.00),
('Mazda', 'CX-5', 'Rojo', 47000, 23000.00),
('Volkswagen', 'Tiguan', 'Gris', 52000, 24000.00);

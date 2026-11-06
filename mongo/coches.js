// Reto 8: base de datos "concesionario" y colección "coches" en MongoDB
db = db.getSiblingDB("concesionario");
db.coches.drop();

db.coches.insertMany([
  { id: 1,  marca: "Toyota",        modelo: "Corolla",  color: "Blanco",   km: 45000, precio: 15000 },
  { id: 2,  marca: "Honda",         modelo: "Civic",    color: "Negro",    km: 60000, precio: 17000 },
  { id: 3,  marca: "Ford",          modelo: "Focus",    color: "Azul",     km: 50000, precio: 14000 },
  { id: 4,  marca: "Chevrolet",     modelo: "Malibu",   color: "Rojo",     km: 70000, precio: 16000 },
  { id: 5,  marca: "Nissan",        modelo: "Sentra",   color: "Gris",     km: 55000, precio: 15500 },
  { id: 6,  marca: "Volkswagen",    modelo: "Jetta",    color: "Blanco",   km: 40000, precio: 16500 },
  { id: 7,  marca: "Hyundai",       modelo: "Elantra",  color: "Negro",    km: 45000, precio: 14500 },
  { id: 8,  marca: "Kia",           modelo: "Rio",      color: "Azul",     km: 30000, precio: 13500 },
  { id: 9,  marca: "Mazda",         modelo: "Mazda3",   color: "Rojo",     km: 48000, precio: 15800 },
  { id: 10, marca: "Subaru",        modelo: "Impreza",  color: "Gris",     km: 53000, precio: 16800 },
  { id: 11, marca: "BMW",           modelo: "Serie 3",  color: "Blanco",   km: 75000, precio: 28000 },
  { id: 12, marca: "Mercedes-Benz", modelo: "Clase C",  color: "Negro",    km: 82000, precio: 32000 },
  { id: 13, marca: "Audi",          modelo: "A4",       color: "Azul",     km: 69000, precio: 29000 },
  { id: 14, marca: "Lexus",         modelo: "IS",       color: "Rojo",     km: 77000, precio: 31000 },
  { id: 15, marca: "Tesla",         modelo: "Model 3",  color: "Blanco",   km: 25000, precio: 45000 },
  { id: 16, marca: "Jeep",          modelo: "Cherokee", color: "Verde",    km: 85000, precio: 20000 },
  { id: 17, marca: "Dodge",         modelo: "Charger",  color: "Negro",    km: 62000, precio: 26000 },
  { id: 18, marca: "Ford",          modelo: "Mustang",  color: "Rojo",     km: 54000, precio: 27000 },
  { id: 19, marca: "Chevrolet",     modelo: "Camaro",   color: "Amarillo", km: 50000, precio: 26500 },
  { id: 20, marca: "Nissan",        modelo: "Altima",   color: "Gris",     km: 72000, precio: 17500 },
  { id: 21, marca: "Hyundai",       modelo: "Tucson",   color: "Azul",     km: 41000, precio: 19000 },
  { id: 22, marca: "Kia",           modelo: "Sportage", color: "Blanco",   km: 38000, precio: 18500 },
  { id: 23, marca: "Toyota",        modelo: "RAV4",     color: "Negro",    km: 60000, precio: 22500 },
  { id: 24, marca: "Mazda",         modelo: "CX-5",     color: "Rojo",     km: 47000, precio: 23000 },
  { id: 25, marca: "Volkswagen",    modelo: "Tiguan",   color: "Gris",     km: 52000, precio: 24000 }
]);

print("Coches insertados: " + db.coches.countDocuments());

// Reto 8: consultas de comprobación en la base de datos concesionario
db = db.getSiblingDB("concesionario");

print("Bases de datos: " + db.adminCommand({ listDatabases: 1 }).databases.map(d => d.name).join(", "));
print("Colecciones en concesionario: " + db.getCollectionNames().join(", "));
print("Número de coches: " + db.coches.countDocuments());

print("\n> db.coches.find().pretty()   (primeros 2 documentos)");
printjson(db.coches.find().limit(2).toArray());

print("\n> Todos los coches (un documento por línea)");
db.coches.find({}, { _id: 0 }).sort({ id: 1 }).forEach(c => print(EJSON.stringify(c)));

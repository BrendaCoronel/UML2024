import sqlite3

# Conexión a la base de datos SQLite
conn = sqlite3.connect('tienda.db')
cursor = conn.cursor()

# Crear tablas en la base de datos
cursor.execute('''
CREATE TABLE IF NOT EXISTS Cliente (
    id_cliente TEXT PRIMARY KEY,
    nombre TEXT,
    apellido TEXT,
    edad INTEGER,
    genero TEXT,
    email TEXT,
    telefono TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Producto (
    id_producto TEXT PRIMARY KEY,
    nombre_producto TEXT,
    descripcion TEXT,
    precio REAL,
    stock INTEGER,
    tamanio TEXT,
    color TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Categoria (
    id_categoria TEXT PRIMARY KEY,
    nombre_categoria TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Compra (
    id_compra TEXT PRIMARY KEY,
    fecha TEXT,
    id_cliente TEXT,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS DetalleCompra (
    id_detalle TEXT PRIMARY KEY,
    cantidad INTEGER,
    precio_unitario REAL,
    id_compra TEXT,
    id_producto TEXT,
    FOREIGN KEY (id_compra) REFERENCES Compra(id_compra),
    FOREIGN KEY (id_producto) REFERENCES Producto(id_producto)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Empleado (
    id_empleado TEXT PRIMARY KEY,
    nombre_empleado TEXT,
    puesto TEXT,
    telefono TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Gerente (
    id_empleado TEXT PRIMARY KEY,
    area_responsable TEXT,
    FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Vendedor (
    id_empleado TEXT PRIMARY KEY,
    ventas_realizadas INTEGER,
    FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado)
)
''')

# Commit para aplicar los cambios
conn.commit()

# Clases
class Cliente:
    def __init__(self, id_cliente, nombre, apellido, edad, genero, email, telefono):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
        self.email = email
        self.telefono = telefono

    def save(self):
        cursor.execute('''
        INSERT OR REPLACE INTO Cliente (id_cliente, nombre, apellido, edad, genero, email, telefono)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (self.id_cliente, self.nombre, self.apellido, self.edad, self.genero, self.email, self.telefono))
        conn.commit()

class Producto:
    def __init__(self, id_producto, nombre_producto, descripcion, precio, stock, tamanio, color):
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.tamanio = tamanio
        self.color = color

    def save(self):
        cursor.execute('''
        INSERT OR REPLACE INTO Producto (id_producto, nombre_producto, descripcion, precio, stock, tamanio, color)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (self.id_producto, self.nombre_producto, self.descripcion, self.precio, self.stock, self.tamanio, self.color))
        conn.commit()

class Categoria:
    def __init__(self, id_categoria, nombre_categoria):
        self.id_categoria = id_categoria
        self.nombre_categoria = nombre_categoria

    def save(self):
        cursor.execute('''
        INSERT OR REPLACE INTO Categoria (id_categoria, nombre_categoria)
        VALUES (?, ?)
        ''', (self.id_categoria, self.nombre_categoria))
        conn.commit()

class Compra:
    def __init__(self, id_compra, fecha, id_cliente):
        self.id_compra = id_compra
        self.fecha = fecha
        self.id_cliente = id_cliente

    def save(self):
        cursor.execute('''
        INSERT OR REPLACE INTO Compra (id_compra, fecha, id_cliente)
        VALUES (?, ?, ?)
        ''', (self.id_compra, self.fecha, self.id_cliente))
        conn.commit()

class DetalleCompra:
    def __init__(self, id_detalle, cantidad, precio_unitario, id_compra, id_producto):
        self.id_detalle = id_detalle
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.id_compra = id_compra
        self.id_producto = id_producto

    def save(self):
        cursor.execute('''
        INSERT OR REPLACE INTO DetalleCompra (id_detalle, cantidad, precio_unitario, id_compra, id_producto)
        VALUES (?, ?, ?, ?, ?)
        ''', (self.id_detalle, self.cantidad, self.precio_unitario, self.id_compra, self.id_producto))
        conn.commit()

class Empleado:
    def __init__(self, id_empleado, nombre_empleado, puesto, telefono):
        self.id_empleado = id_empleado
        self.nombre_empleado = nombre_empleado
        self.puesto = puesto
        self.telefono = telefono

    def save(self):
        cursor.execute('''
        INSERT OR REPLACE INTO Empleado (id_empleado, nombre_empleado, puesto, telefono)
        VALUES (?, ?, ?, ?)
        ''', (self.id_empleado, self.nombre_empleado, self.puesto, self.telefono))
        conn.commit()

class Gerente(Empleado):
    def __init__(self, id_empleado, nombre_empleado, puesto, telefono, area_responsable):
        super().__init__(id_empleado, nombre_empleado, puesto, telefono)
        self.area_responsable = area_responsable

    def save(self):
        super().save()
        cursor.execute('''
        INSERT OR REPLACE INTO Gerente (id_empleado, area_responsable)
        VALUES (?, ?)
        ''', (self.id_empleado, self.area_responsable))
        conn.commit()

class Vendedor(Empleado):
    def __init__(self, id_empleado, nombre_empleado, puesto, telefono, ventas_realizadas):
        super().__init__(id_empleado, nombre_empleado, puesto, telefono)
        self.ventas_realizadas = ventas_realizadas

    def save(self):
        super().save()
        cursor.execute('''
        INSERT OR REPLACE INTO Vendedor (id_empleado, ventas_realizadas)
        VALUES (?, ?)
        ''', (self.id_empleado, self.ventas_realizadas))
        conn.commit()

# Ejemplo de uso
cliente1 = Cliente("C001", "Juan", "Pérez", 30, "Masculino", "juanperez@email.com", "123456789")
producto1 = Producto("P001", "Smartphone", "Descripción del smartphone", 500.0, 10, "M", "Negro")
categoria1 = Categoria("Cat001", "Electrónica")
compra1 = Compra("Compra001", "2024-11-06", "C001")
detalle_compra1 = DetalleCompra("Detalle001", 2, 500.0, "Compra001", "P001")

empleado1 = Empleado("E001", "Ana", "Gerente", "987654321")
gerente1 = Gerente("E002", "Carlos", "Gerente", "987654322", "Ventas")
vendedor1 = Vendedor("E003", "Luis", "Vendedor", "987654323", 100)

# Guarda en la base de datos
cliente1.save()
producto1.save()
categoria1.save()
compra1.save()
detalle_compra1.save()
empleado1.save()
gerente1.save()
vendedor1.save()

# Cerrar la conexión
conn.close()

print("Datos guardados correctamente en la base de datos.")

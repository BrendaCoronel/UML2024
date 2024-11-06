# Relaciones
Empleado *-- Gerente;    // Un Gerente es un tipo de Empleado (composición)
Empleado *-- Vendedor;   // Un Vendedor es un tipo de Empleado (composición)
Producto *-- Categoria;  // Un Producto pertenece a una Categoria (composición)
Compra *-- Cliente;      // Un Cliente hace una Compra (composición)
Compra *-- Detalle_Compra; // Una Compra tiene varios Detalles de Compra (composición)
Detalle_Compra *-- Producto; // Un Detalle de Compra está relacionado con un Producto (composición)

# Generalizaciones
Empleado <|-- Gerente;    // Gerente es un tipo especializado de Empleado
Empleado <|-- Vendedor;   // Vendedor es un tipo especializado de Empleado
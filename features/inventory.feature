# language: es
@inventory
Característica: Catálogo de productos
  Como comprador
  Quiero explorar y ordenar el catálogo
  Para encontrar productos fácilmente

  Antecedentes:
    Dado que inicié sesión como usuario estándar

  @smoke
  Escenario: El catálogo muestra los 6 productos
    Entonces el catálogo muestra 6 productos

  Escenario: Ordenar productos por precio de menor a mayor
    Cuando ordeno los productos por "lohi"
    Entonces los precios quedan ordenados de menor a mayor

  Escenario: Ordenar productos por nombre de la Z a la A
    Cuando ordeno los productos por "za"
    Entonces los nombres quedan ordenados de la Z a la A

  Escenario: Quitar del carrito un producto recién agregado
    Cuando agrego "Sauce Labs Backpack" al carrito
    Y quito "Sauce Labs Backpack" del carrito
    Entonces el contador del carrito muestra 0

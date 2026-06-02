# language: es
@cart
Característica: Carrito de compras
  Como comprador
  Quiero agregar productos al carrito
  Para luego pagarlos

  Antecedentes:
    Dado que inicié sesión como usuario estándar

  @smoke
  Escenario: Agregar un producto al carrito
    Cuando agrego "Sauce Labs Backpack" al carrito
    Entonces el contador del carrito muestra 1

  Escenario: Agregar varios productos al carrito
    Cuando agrego "Sauce Labs Backpack" al carrito
    Y agrego "Sauce Labs Bike Light" al carrito
    Entonces el contador del carrito muestra 2
    Y el carrito contiene "Sauce Labs Backpack"

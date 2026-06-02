# language: es
@checkout
Característica: Compra de extremo a extremo
  Como comprador
  Quiero completar el proceso de compra
  Para recibir la confirmación de mi pedido

  @smoke
  Escenario: Un usuario estándar completa una compra
    Dado que inicié sesión como usuario estándar
    Cuando agrego "Sauce Labs Backpack" al carrito
    Y voy al carrito
    Y procedo al pago con nombre "Ada" apellido "Lovelace" y código postal "12345"
    Y finalizo la compra
    Entonces veo la confirmación "Thank you for your order!"

  Escenario: El checkout exige el nombre del comprador
    Dado que inicié sesión como usuario estándar
    Cuando agrego "Sauce Labs Backpack" al carrito
    Y voy al carrito
    Y continúo el checkout sin completar el nombre
    Entonces veo el error de checkout "First Name is required"

  Escenario: El resumen del pedido calcula correctamente el total
    Dado que inicié sesión como usuario estándar
    Cuando agrego "Sauce Labs Backpack" al carrito
    Y agrego "Sauce Labs Bike Light" al carrito
    Y voy al carrito
    Y procedo al pago con nombre "Ada" apellido "Lovelace" y código postal "12345"
    Entonces el total del pedido es igual al subtotal más los impuestos

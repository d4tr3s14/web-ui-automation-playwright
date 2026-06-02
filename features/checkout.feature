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

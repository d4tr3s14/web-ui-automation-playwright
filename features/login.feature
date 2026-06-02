# language: es
@login
Característica: Inicio de sesión en SauceDemo
  Como usuario del sitio
  Quiero iniciar sesión con mis credenciales
  Para acceder al catálogo de productos

  @smoke
  Escenario: Inicio de sesión exitoso con usuario estándar
    Dado que estoy en la página de inicio de sesión
    Cuando inicio sesión con el usuario estándar
    Entonces veo la página de productos

  Escenario: El usuario bloqueado no puede iniciar sesión
    Dado que estoy en la página de inicio de sesión
    Cuando inicio sesión con el usuario bloqueado
    Entonces veo el mensaje de error "Sorry, this user has been locked out"

  Esquema del escenario: Las credenciales inválidas son rechazadas
    Dado que estoy en la página de inicio de sesión
    Cuando inicio sesión con usuario "<usuario>" y contraseña "<password>"
    Entonces veo un mensaje de error

    Ejemplos:
      | usuario       | password     |
      | usuario_falso | secret_sauce |
      | standard_user | clave_mala   |

  Escenario: No se puede iniciar sesión sin contraseña
    Dado que estoy en la página de inicio de sesión
    Cuando ingreso el usuario "standard_user" sin contraseña
    Entonces veo el mensaje de error "Password is required"

  Escenario: No se puede iniciar sesión sin credenciales
    Dado que estoy en la página de inicio de sesión
    Cuando intento iniciar sesión sin credenciales
    Entonces veo el mensaje de error "Username is required"

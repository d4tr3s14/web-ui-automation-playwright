# 📘 Guía detallada (para todos los niveles)

Esta guía explica **paso a paso** cómo ejecutar, entender y editar el proyecto
**web-ui-automation-playwright**, desde tu computador hasta lo que ocurre en
GitHub cuando se ejecuta el CI. Pensada para que **alguien junior** pueda hacerlo
sin complicaciones.

> Orden sugerido: **1)** ¿Qué es? → **2)** Glosario → **3)** Frameworks →
> **4)** Requisitos → **5)** Clonar → **6)** Ejecución local → **7)** Evidencia y
> reportes → **8)** Cómo editar → **9)** Qué hace el CI.

---

## 1. ¿Qué es este proyecto?

Es un framework de **automatización de pruebas de interfaz web (UI)**: un robot
que **abre un navegador, hace clic, escribe y verifica** que una página web
funciona, igual que lo haría una persona, pero automáticamente.

Como sitio de práctica usa **[SauceDemo](https://www.saucedemo.com)** (una tienda
de demo pública). Las pruebas están organizadas con el patrón **Page Object
Model**, descritas en lenguaje de negocio con **BDD (Gherkin)**, y cuando algo
falla guardan **screenshot, video y "trace"** como evidencia en **Allure**.

```
Gherkin (.feature) ─► steps (pytest-bdd) ─► Page Objects ─► Playwright ─► navegador
                                                                  └─ evidencia ─► Allure
```

---

## 2. Glosario (términos clave)

| Término | Qué significa, en simple |
|---------|--------------------------|
| **UI testing** | Probar la aplicación a través de su interfaz gráfica (lo que ve el usuario). |
| **Playwright** | La herramienta que controla el navegador (clics, texto, navegación). |
| **Page Object Model (POM)** | Patrón donde cada página web se representa con una clase; las pruebas usan métodos (`login`, `add_to_cart`) en vez de selectores sueltos. |
| **Selector / Locator** | La "dirección" de un elemento en la página (ej. `#user-name`). |
| **BDD / Gherkin** | Escribir pruebas en lenguaje natural (`Dado / Cuando / Entonces`). |
| **pytest-bdd** | Conecta el Gherkin con el código Python (los "steps"). |
| **Fixture** | Una pieza reutilizable que prepara algo para la prueba (aquí, el navegador/página). |
| **Headless** | Ejecutar el navegador **sin ventana visible** (más rápido, ideal para CI). |
| **Screenshot** | Foto de la pantalla en el momento del fallo. |
| **Video** | Grabación de toda la ejecución del navegador durante la prueba. |
| **Trace** (de Playwright) | "Caja negra" que permite reproducir paso a paso lo ocurrido (`playwright show-trace`). |
| **Allure** | Reporte interactivo donde se ven las pruebas y su evidencia. |
| **Escenario / Scenario Outline** | Un caso de prueba; el *outline* lo repite con varios datos (tabla `Ejemplos`). |
| **CI** | Automatización que corre las pruebas en GitHub en cada cambio. |
| **Matriz** | Correr las mismas pruebas en varias configuraciones (aquí, **Chromium y Firefox**). |
| **gh-pages** | Rama donde se publica el reporte Allure como sitio web. |

---

## 3. Frameworks y lenguajes (para qué sirve cada uno)

| Herramienta | Lenguaje | ¿Para qué sirve **en este proyecto**? |
|-------------|----------|----------------------------------------|
| **Python** | — | Lenguaje base del framework. |
| **Playwright** | Python | **Controla el navegador**: navega, hace clic, escribe, verifica, y graba video/trace. |
| **pytest** | Python | El **ejecutor** de pruebas. |
| **pytest-bdd** | Python | Conecta los escenarios **Gherkin** con las funciones Python. |
| **allure-pytest** | Python | Genera el reporte **Allure** y adjunta la evidencia. |
| **GitHub Actions** | YAML | El **CI**: instala el navegador, corre las pruebas y publica el reporte. |

---

## 4. Requisitos previos

1. **Python 3.10+** → https://www.python.org/downloads/ (`python --version`).
2. **Git** → https://git-scm.com/
3. *(Opcional, para el dashboard)* **Allure CLI** → `npm install -g allure-commandline`.
4. Conexión a internet (las pruebas usan el sitio público SauceDemo).

---

## 5. Clonar el proyecto

```bash
git clone https://github.com/d4tr3s14/web-ui-automation-playwright.git
cd web-ui-automation-playwright
```

---

## 6. Ejecución LOCAL paso a paso

### Paso 1 — Entorno virtual e instalación
```bash
python -m venv .venv
```
Actívalo:
- **Windows (PowerShell):** `.\.venv\Scripts\Activate.ps1`
- **Windows (Git Bash):** `source .venv/Scripts/activate`
- **Linux / macOS:** `source .venv/bin/activate`

Instala dependencias **y el navegador** (este segundo paso descarga Chromium):
```bash
pip install -r requirements.txt
playwright install chromium
```

### Paso 2 — Ejecutar las pruebas
```bash
pytest                          # headless (sin ventana), genera allure-results/
```
Para **ver el navegador** mientras corre:
- **Linux/macOS:** `HEADLESS=false pytest`
- **Windows PowerShell:** `$env:HEADLESS="false"; pytest`

Para correr solo un grupo (por etiqueta/marker):
```bash
pytest -m smoke         # solo las pruebas rápidas
pytest -m login         # solo login
```

### Paso 3 — Ver el reporte Allure
```bash
allure serve allure-results
```

---

## 7. Evidencia y reportes

- Cuando un test **pasa**, se adjunta el **video** de la ejecución a Allure.
- Cuando un test **falla**, se adjunta además **screenshot** y **trace**.
- El *trace* es la joya: ábrelo para "viajar en el tiempo" por cada paso:
  ```bash
  playwright show-trace test-results/trace-<nombre_del_test>.zip
  ```

---

## 8. Cómo EDITAR el proyecto (recetas para junior)

### a) Agregar un escenario nuevo (Gherkin)
Edita el `.feature` correspondiente en `features/`, por ejemplo `cart.feature`:
```gherkin
  Escenario: Quitar un producto del carrito
    Cuando agrego "Sauce Labs Backpack" al carrito
    Y quito "Sauce Labs Backpack" del carrito
    Entonces el contador del carrito muestra 0
```
Si usas pasos que ya existen (en `features/steps/`), no necesitas más. Si es un
paso nuevo, defínelo en el archivo de steps correspondiente.

### b) Agregar una acción a una página (Page Object)
Edita la clase en `pages/`. Ejemplo, en `inventory_page.py`:
```python
def open_cart(self) -> None:
    self.click(self.CART_LINK)
```
Las pruebas llaman a estos métodos en vez de tocar selectores directamente.

### c) Cambiar el sitio bajo prueba o credenciales
Edita `config/settings.py` (o pásalo por variable de entorno): `BASE_URL`,
`SAUCE_USER`, `SAUCE_PASSWORD`, `HEADLESS`, `BROWSER` (`chromium`/`firefox`/`webkit`).

### d) Probar en otro navegador localmente
```bash
BROWSER=firefox pytest        # (instala antes: playwright install firefox)
```

---

## 9. ¿Qué hace el CI en GitHub? (paso a paso)

El CI vive en `.github/workflows/ci.yml` y corre en cada `push`/`pull request`:

1. **Matriz de navegadores** — corre todo en **Chromium y Firefox** en paralelo.
2. **Install dependencies** — `pip install -r requirements.txt`.
3. **Install Playwright browser** — descarga el navegador de esa rama de la matriz.
4. **Run UI test suite** — ejecuta las pruebas (headless).
5. **Upload Allure results / evidence** — guarda resultados y la evidencia
   (videos/traces) como **artefactos descargables**.
6. **Job `publish-report` (solo en push)** — **fusiona** los resultados de ambos
   navegadores, genera el reporte **Allure** y lo **publica en GitHub Pages**.

### ¿Dónde veo el resultado?
- GitHub → pestaña **Actions** → el run (✅ / ❌).
- Reporte Allure en vivo: **https://d4tr3s14.github.io/web-ui-automation-playwright/**
  (requiere GitHub Pages activado en *Settings → Pages → rama `gh-pages`*).

---

## 10. Problemas comunes

| Problema | Solución |
|----------|----------|
| `playwright: command not found` | Activa el `.venv` y `pip install -r requirements.txt`. |
| Error "Executable doesn't exist" | Falta el navegador: `playwright install chromium`. |
| Las pruebas no abren el navegador | Es headless por defecto; usa `HEADLESS=false`. |
| Fallan por timeout / red | SauceDemo requiere internet; revisa tu conexión. |
| `allure: command not found` | Instala el CLI: `npm install -g allure-commandline`. |
| El badge de Allure da 404 | Falta activar GitHub Pages (rama `gh-pages`). |

---

## 11. Mapa de archivos

```
features/                escenarios BDD (Gherkin) — el "qué"
  steps/                 step definitions (pytest-bdd) que orquestan los Page Objects
pages/                   Page Object Model — el "cómo" interactuar con la UI
  base_page.py           acciones comunes sobre la página
  login_page.py / inventory_page.py / cart_page.py / checkout_page.py
config/settings.py       URL, credenciales demo, headless, navegador, timeouts
conftest.py              fixtures de Playwright + captura de evidencia + Allure
pytest.ini               configuración de pytest (markers, allure)
.github/workflows/ci.yml el pipeline de CI (matriz Chromium + Firefox)
```

---

¿Dudas? Empieza por la **sección 6** (instalar y `pytest`), y cuando quieras ver
el detalle de un fallo usa el **trace** (sección 7).

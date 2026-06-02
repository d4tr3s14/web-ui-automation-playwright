# Web UI Automation — Playwright + POM + BDD

[![CI](https://github.com/d4tr3s14/web-ui-automation-playwright/actions/workflows/ci.yml/badge.svg)](https://github.com/d4tr3s14/web-ui-automation-playwright/actions/workflows/ci.yml)
[![Allure Report](https://img.shields.io/badge/Allure-live%20report-fa4d56?logo=allure)](https://d4tr3s14.github.io/web-ui-automation-playwright/)
![Python](https://img.shields.io/badge/python-3.10%2B-3776ab?logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-1.48-2ead33?logo=playwright)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

> 📘 ¿Primera vez o perfil junior? Lee la **[Guía detallada paso a paso](docs/GUIA.md)**
> (glosario, para qué sirve cada herramienta, ejecución local y CI).

Framework de **automatización de UI web** con **Playwright + Python**, un
**Page Object Model** bien estructurado y escenarios **BDD (Gherkin + pytest-bdd)**.
Como sitio bajo prueba se usa el demo público **[SauceDemo](https://www.saucedemo.com)**.

En cada fallo captura **screenshot, video y trace de Playwright** y los adjunta
al reporte **Allure**.

---

## ✨ Características

- **Page Object Model** por capas: `BasePage` con acciones robustas (auto-espera
  de Playwright) y páginas concretas (`LoginPage`, `InventoryPage`, `CartPage`,
  `CheckoutPage`).
- **BDD legible**: features en español (`features/*.feature`) + step definitions
  con `pytest-bdd`; los pasos comunes se comparten vía `conftest`.
- **Evidencia automática en fallos**: screenshot (PNG) + video (WEBM) + trace
  (ZIP, abrible con `playwright show-trace`), adjuntos a Allure.
- **Allure**: dashboard navegable con histórico, publicado en GitHub Pages por CI.
- **Sin secretos**: las credenciales de SauceDemo son públicas y de demo,
  configurables por variables de entorno.

## 🏗️ Arquitectura

```
features/                Gherkin (.feature) — el "qué" en lenguaje de negocio
   └── steps/            step definitions (pytest-bdd) — orquestan los Page Objects
pages/                   Page Object Model — el "cómo" interactuar con la UI
   ├── base_page.py      acciones comunes sobre la Page de Playwright
   ├── login_page.py
   ├── inventory_page.py
   ├── cart_page.py
   └── checkout_page.py
config/settings.py       URL base, credenciales demo, headless, timeouts (env)
conftest.py              fixtures Playwright + captura de evidencia + Allure
```

**Por qué POM:** las pruebas (steps) nunca tocan selectores crudos; hablan con
métodos de negocio (`login`, `add_item_to_cart`, `checkout`). Si la UI cambia, se
ajusta una sola página, no decenas de pruebas.

## 🚀 Uso

### Requisitos
- Python 3.10+
- [Allure CLI](https://allurereport.org/docs/install/) (opcional, para ver el reporte)

### Instalación

```bash
python -m venv .venv
source .venv/Scripts/activate          # Windows
# source .venv/bin/activate            # Linux/macOS
pip install -r requirements.txt
playwright install chromium            # descarga el navegador
```

### Ejecutar

```bash
pytest                                 # headless, genera allure-results/
pytest -m smoke                        # solo pruebas de humo
HEADLESS=false pytest                  # ver el navegador (Linux/macOS)
$env:HEADLESS="false"; pytest          # ver el navegador (PowerShell)
```

### Ver el reporte Allure

```bash
allure serve allure-results
```

### Ver un trace de un fallo

```bash
playwright show-trace test-results/trace-<nombre_del_test>.zip
```

## 🧪 Escenarios incluidos

| Feature | Escenarios |
|---------|-----------|
| `login` | login exitoso, usuario bloqueado, credenciales inválidas (outline) |
| `cart` | agregar uno y varios productos; verificación del contador y contenido |
| `checkout` | compra de extremo a extremo hasta la confirmación del pedido |

## ⚙️ Configuración (variables de entorno)

| Variable | Default | Descripción |
|----------|---------|-------------|
| `BASE_URL` | `https://www.saucedemo.com` | Sitio bajo prueba |
| `HEADLESS` | `true` | Ejecutar sin ventana |
| `BROWSER` | `chromium` | `chromium` / `firefox` / `webkit` |
| `SLOW_MO` | `0` | ms entre acciones (debug) |
| `DEFAULT_TIMEOUT` | `10000` | timeout por defecto (ms) |

## 🔄 CI/CD

GitHub Actions instala el navegador, corre la suite, **publica el reporte Allure
en GitHub Pages** y deja como artefactos descargables los `allure-results` y la
evidencia (`test-results`: videos y traces).

## 📝 Licencia

MIT — ver [LICENSE](LICENSE).

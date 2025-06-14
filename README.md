Suite OSINT Vanille

Conjunto modular de scripts Python para automatizar tareas OSINT de forma rápida y eficiente.
Diseñado para uso en entornos locales o móviles como Termux.


---

🧩 Contenido

Cada script es independiente y cumple una función específica en procesos de reconocimiento pasivo:

portscan.py: escaneo básico de puertos en un host objetivo

whois.py: consulta WHOIS detallada de dominios

dnslookup.py: resolución de registros DNS (A, MX, TXT, etc.)

emailcheck.py: verificación sintáctica y MX básica de correos electrónicos

ipinfo.py: obtención de datos públicos sobre una dirección IP



---

📦 Requisitos

Instala las dependencias necesarias con:

pip install -r requirements.txt


---

🚀 Uso básico

Ejecuta cualquier script desde el directorio scripts/. Ejemplo:

python3 scripts/whois.py vanillevault.github.io

Todos los scripts están pensados para ser simples, modificables y directos en su funcionalidad.


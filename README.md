🛰️ Suite OSINT Vanille

Conjunto modular de scripts OSINT en Python para reconocimiento pasivo rápido, ligero y directo.
Diseñado para correr sin complicaciones en entornos locales como Linux, Termux o máquinas discretas.
El enfoque es claro: eficiencia, anonimato y velocidad.


---

🧩 Scripts incluidos

Cada script cumple una función específica. Puedes usarlos por separado según la tarea:

Script	Función

vainilla_dns.py	Resolución de registros DNS (A, MX, TXT, NS, etc.)
vainilla_ipinfo.py	Obtiene información pública sobre una dirección IP
vainilla_robots.py	Extrae y muestra el archivo robots.txt de un sitio web
vainilla_title.py	Extrae el título (<title>) de una página web
vainilla_whois.py	Consulta WHOIS con formato Vanille (limpio y directo)
whois.py	Script base para realizar consultas WHOIS (soporte técnico)



---

📦 Requisitos

Instala las dependencias necesarias con:

pip install -r requirements.txt

Ejemplo de contenido de requirements.txt (puedes adaptarlo):

requests
dnspython
ipwhois
beautifulsoup4
python-whois


---

🚀 Uso básico

Ejecuta cualquier script desde terminal:

python3 vainilla_dns.py ejemplo.com
python3 vainilla_ipinfo.py 8.8.8.8
python3 vainilla_robots.py https://ejemplo.com
python3 vainilla_title.py https://ejemplo.com
python3 vainilla_whois.py ejemplo.com

> ⚠️ Todos los scripts están diseñados para ser simples, sin menú, sin interfaz gráfica. Son herramientas de línea directa, estilo Vanille.




---

🧠 Filosofía Vanille

> “Un script, una misión.
No hay clicks, no hay rastros. Solo info útil, en silencio.”
— Vanille

#!/data/data/com.termux/files/usr/bin/python3
import dns.resolver
import ipinfo
import sys
from colorama import Fore, init

init(autoreset=True)

TOKEN = 'TU_TOKEN_IPINFO_AQUI'  # Cambia esto por tu token ipinfo.io

def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Uso: python vainilla_ipinfo.py <dominio>")
        sys.exit(1)
    domain = sys.argv[1].lower()
    try:
        ip = dns.resolver.resolve(domain, 'A')[0].to_text()
        handler = ipinfo.getHandler(TOKEN)
        details = handler.getDetails(ip)
        print(Fore.YELLOW + f"IP: {ip}")
        print(f"Ciudad: {details.city}")
        print(f"Región: {details.region}")
        print(f"País: {details.country_name}")
        print(f"Org: {details.org}")
    except Exception as e:
        print(Fore.RED + f"Error en IPInfo: {e}")

if __name__ == "__main__":
    main()

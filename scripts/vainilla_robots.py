#!/data/data/com.termux/files/usr/bin/python3
import requests
import sys
from colorama import Fore, init

init(autoreset=True)

def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Uso: python vainilla_robots.py <dominio>")
        sys.exit(1)
    domain = sys.argv[1].lower()
    url = f"https://{domain}/robots.txt"
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            print(r.text)
        else:
            print(Fore.RED + "No encontrado o no accesible")
    except Exception as e:
        print(Fore.RED + f"Error al obtener robots.txt: {e}")

if __name__ == "__main__":
    main()

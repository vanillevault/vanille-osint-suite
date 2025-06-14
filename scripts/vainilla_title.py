#!/data/data/com.termux/files/usr/bin/python3
import requests
import sys
from bs4 import BeautifulSoup
from colorama import Fore, init

init(autoreset=True)

def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Uso: python vainilla_title.py <dominio>")
        sys.exit(1)
    domain = sys.argv[1].lower()
    url = f"https://{domain}"
    try:
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        title = soup.title.string if soup.title else "No title encontrado"
        print(Fore.GREEN + title)
    except Exception as e:
        print(Fore.RED + f"Error al obtener título: {e}")

if __name__ == "__main__":
    main()

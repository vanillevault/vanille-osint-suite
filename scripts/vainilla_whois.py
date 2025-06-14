#!/data/data/com.termux/files/usr/bin/python3
import whois
import sys
from colorama import Fore, init

init(autoreset=True)

def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Uso: python vainilla_whois.py <dominio>")
        sys.exit(1)
    domain = sys.argv[1].lower()
    try:
        w = whois.whois(domain)
        for k, v in w.items():
            print(Fore.GREEN + f"{k}: {v}")
    except Exception as e:
        print(Fore.RED + f"Error en WHOIS: {e}")

if __name__ == "__main__":
    main()

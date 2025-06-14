#!/data/data/com.termux/files/usr/bin/python3
import dns.resolver
import sys
from colorama import Fore, init

init(autoreset=True)

def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Uso: python vainilla_dns.py <dominio>")
        sys.exit(1)
    domain = sys.argv[1].lower()
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME']
    for rtype in record_types:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            print(Fore.YELLOW + f"{rtype} records:")
            for rdata in answers:
                print(f"  {rdata.to_text()}")
        except Exception:
            print(Fore.RED + f"  No hay registros {rtype} o error")

if __name__ == "__main__":
    main()

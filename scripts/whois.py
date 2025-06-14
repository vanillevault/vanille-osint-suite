#!/usr/bin/env python3
import whois
import sys

def main():
    if len(sys.argv) < 2:
        print("Uso: whois.py dominio.com")
        sys.exit(1)
    domain = sys.argv[1]
    w = whois.whois(domain)
    print(w)

if __name__ == "__main__":
    main()

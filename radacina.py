#!/usr/bin/env python3
"""Rădăcina cifrelor: adună cifrele unui număr până rămâne o singură cifră.

Exemple:
    python3 radacina.py 1728        -> 1+7+2+8 = 18 -> 1+8 = 9
    python3 radacina.py 17:28       -> ora e tratată ca 1728
    python3 radacina.py             -> folosește ora curentă
"""
import sys
from datetime import datetime


def radacina(n: int) -> int:
    """Rădăcina cifrelor (digital root) pentru un număr întreg nenegativ."""
    if n == 0:
        return 0
    return 1 + (n - 1) % 9


def pasi(n: int) -> list[int]:
    """Toate sumele intermediare, ca să se vadă calculul."""
    rezultat = [n]
    while n >= 10:
        n = sum(int(c) for c in str(n))
        rezultat.append(n)
    return rezultat


def main() -> None:
    text = sys.argv[1] if len(sys.argv) > 1 else datetime.now().strftime("%H:%M")
    cifre = "".join(c for c in text if c.isdigit())
    if not cifre:
        print("Dă-mi un număr, de exemplu: python3 radacina.py 1728")
        sys.exit(1)
    n = int(cifre)
    r = radacina(n)
    print(f"{text}: " + " -> ".join(str(x) for x in pasi(n)))
    if r in (3, 6, 9):
        print(f"Rădăcina e {r}: număr 3-6-9.")
    else:
        print(f"Rădăcina e {r}.")


if __name__ == "__main__":
    main()

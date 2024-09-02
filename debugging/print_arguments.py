#!/usr/bin/python3
import sys

# Vérifier s'il y a des arguments en ligne de commande
if len(sys.argv) > 1:
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i}: {arg}")
else:
    print("Aucun argument fourni.")

#!/usr/bin/python3
import sys

# Démarrer à l'index 1 pour éviter d'imprimer le nom du fichier
for i in range(1, len(sys.argv)):
    print(sys.argv[i])

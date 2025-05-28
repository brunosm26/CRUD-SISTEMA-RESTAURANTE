import json
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


PRATOS_FILE = os.path.join(BASE_DIR, 'pratos.json')
BEBIDAS_FILE = os.path.join(BASE_DIR, 'bebidas.json')


try:
    with open(PRATOS_FILE, 'r', encoding='utf-8') as f:
        cardapio_pratos = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    cardapio_pratos = []

try:
    with open(BEBIDAS_FILE, 'r', encoding='utf-8') as f:
        cardapio_bebidas = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    cardapio_bebidas = []

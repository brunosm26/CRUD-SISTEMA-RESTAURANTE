import json

PRATOS_FILE = 'pratos.json'
BEBIDAS_FILE = 'bebidas.json'

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

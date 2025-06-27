import os
from datetime import datetime

LOG_FILE_URL = "data/transactions.log"

def log_transaction(message):
    with open(LOG_FILE_URL, 'a') as file:
        file.write(f"[{datetime.now()}] {message}\n")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

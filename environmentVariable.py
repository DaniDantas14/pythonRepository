from dotenv import load_dotenv
import os

load_dotenv()

nome = os.getenv('NOME')
idade = os.getenv('IDADE')
password = os.getenv('PASSWORD')

print(nome, idade, password)
Nome = ""
Nota = 0

Nome = input("Favor entrar com o Nome : ")
Nota = float(input(f"Entrar com Nota entre 0 e 10 de {Nome}: "))
while Nota < 0 or Nota > 10:
    print("A Nota deve ser entre 0 e 10!")
    Nota = float(input(f"Entrar com Nota entre 0 e 10 de {Nome}: "))

print(f"\nA Nota de {Nome} foi {Nota}!")
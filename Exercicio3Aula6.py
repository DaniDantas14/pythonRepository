Nome = ""
Idade = 0
Salario =  0 
Sexo = ""
SexoNome = ""
EstadoCivil = ""
EstadoCivilNome = ""

Nome = input("Favor entrar com o Nome : ")
while len(Nome) <= 3:
    print("O nome deve conter mais que 3 caracteres!")
    Nome = input("Favor entrar com o Nome : ")

Idade = int(input(f"Entrar com a idade de {Nome} : "))
while Idade < 0 or Idade > 150:
    print("A Idade deve ser entre 0 e 150!")
    Idade = int(input(f"Entrar com a idade de {Nome} : "))

Salario = float(input(f"Entrar com o salário de {Nome} : "))
while Salario <= 0:
    print("O salário deve ser maior que 0!")
    Salario = float(input(f"Entrar com o salário de {Nome} : "))

Sexo = input(f"Entrar com o sexo de {Nome}  (m-masculino ou f-feminino): ")
while Sexo != "f" and Sexo != "m":
    print("O sexo deve ser m ou f!")
    Sexo = input(f"Entrar com o sexo de {Nome}  (m-masculino ou f-feminino): ")

EstadoCivil = input(f"Entrar com o estado civil de {Nome}  (s-solteiro, c-casado, d-divorciado ou v-viúvo): ")
while EstadoCivil != "s" and EstadoCivil != "c" and EstadoCivil != "d" and EstadoCivil != "v":
    print("O estado civil deve ser s, c , d ou v!")
    EstadoCivil = input(f"Entrar com o estado civil de {Nome}  (s-solteiro, c-casado, d-divorciado ou v-viúvo): ")

if Sexo == "f":
    SexoNome = "Feminino"
else:
    SexoNome = "Masculino"

if EstadoCivil == "s":
    EstadoCivilNome = "Solteiro(a)"
elif EstadoCivil == "c":
    EstadoCivilNome = "Casado(a)"
elif EstadoCivil == "d":
    EstadoCivilNome = "Divorciado(a)"
else:
    EstadoCivilNome = "Viúvo(a)" 

print(f"\nInformações sobre {Nome} : \nIdade : {Idade} anos \nSalário : {Salario} \nSexo : {SexoNome} \nEstado Civil : {EstadoCivilNome} \n")
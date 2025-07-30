# Solicita a idade do usuário
idade = int(input("Digite sua idade: "))

# Classificação com base na idade
if idade >= 0 and idade <= 12:
    categoria = "Criança"
elif idade >= 13 and idade <= 17:
    categoria = "Adolescente"
elif idade >= 18 and idade <= 59:
    categoria = "Adulto"
elif idade >= 60:
    categoria = "Idoso"
else:
    categoria = "Idade inválida"

# Exibe o resultado
print("Classificação:", categoria)
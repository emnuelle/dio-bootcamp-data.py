# nota. A primeira forma não é atualmente recomendada e seu uso em Python3 é raro!

nome = "Emanuelle"
idade = 20
profissao = "engenheira de software"
linguagem = "python"

#  Old style ("%")
print("Olá, me chamo %s. Eu tenho %d anos de idade, tabalho como %s e estou matriculada no curso de %s." % (nome, idade, profissao, linguagem)) 

#  Método(.format())

print("Olá, me chamo {}. Eu tenho {} anos de idade, tabalho como {} e estou matriculada no curso de {}." .format(nome, idade, profissao, linguagem)) 

#  "f"-string
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, tabalho como {profissao} e estou matriculada no curso de {linguagem}.") 

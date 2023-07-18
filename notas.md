# Notas do bootcamp 

## Ambiente de Desenvolvimento e Primeiros Passos com Python
### **Primero Programa**
"./programas/primeiro-pp.py"
- Foi elaborado um programa simples em python!

## Conhecendo a Linguagem de Programação Python
### **Tipos de dados:** "Os tipos servem para definir as cracterísticas e comportamentos de um valor (Objeto) para o interpretador, e com ele é capaz de realizar ooperações matemáticas"

Tipos Built-ins:
- Texto: str
- Numérico: int (possuem precisão limitada), float (números racionais e sua implementação), complex
- Sequência: list, tuple, range 
- Mapa: dict
- Coleção: set, frozenset
- Booleano: bool (true/false) {Uma subclasse de int}
- Binário: bytes, bytearray, memoryview

*Cada classe possui a sua implementação!*

Existem também outras formas de conseguir o acessar o python, um exemplo é o terminal do computador, escrevendo "pyhton" (Obviamente assim que instalado)

explorando o código no: "./programas/tipos-de-dados.py"

### **Modo interativo** "O interpretador python pode executar em modo que possibilite o desenvolvedor a escrever código, e ver o resultado na hora."

_"um exemplo é o terminal do computador, escrevendo "pyhton" (Obviamente assim que instalado)"_

- _função dir e help_:
  dir: Sem argumentos, retorna a lista de nomes no escopo local atual. Com um argumento, retorna uma lista de atributos válidos para o objeto, ex: 
  
    ```
    dir()
    dir(100)
    ```

  Como Visto em exemplo, ele pode auxiliar de várias formas como "formar" o prgrama.

  help: Invoca o sistema de ajuda integrado. É possível fazer buscas em modo interativo ou informar por parâmetro qual o nome do módulo, função, classe, método ou variável. ex:

    ```
    help()
    help(100)
    ```

### **Variáveis e constantes**

**_Variáveis_**: Em linguagens de programação podemos definir valores que podem sofrer alterações no decorrer da execução do programa. Esses valores recebem o nome de variáveis, pois eles nascem com um valor e não necessáriamente devem permanecer com o mesmo durante a execução do programa. 
nota: Não precisamos definir o tipo de dados da variável, o Python faz isso automaticamente para nós. (Por isso que não é possivel criar uma variavél sem atribuir um valor, para alterar esse valor basta fazer uma atribuição de um valor novo!)

**_Constantes_**: Assim como as vriáveis as constantes são utilizadas para armazenar valores. Uma constante nasce com um valor e permace com ele até o final da execução do programa, ou seja, o valor é imutável.
**O PYHTON NÃO POSSUI CONSTANTES**, nele nós utilizamos a convenção que diz ao programador que a variável é uma constante. Para fazer isso, você deve criar a variável com o nome to em letras maíusculas.

**_Boas Práticas_**: 
- Padrão de nomes "Snake case ( _ )" 
- Escolher nomes sugestivos
- Nome de constantes todo me maiúsculo

explorando o código no: "./programas/var-const.py"

### **Conversão de Tipos**

Convertir o tipo de variáveis para manipular de uma forma diferente, ex:variáveis do tipo String que armazenam números e utiliza-las para fazer alguma operação matemática.

explorando o código no: "./programas/conversao-de-tipos.py"

### **Funções de entrada e saída**

    - input() > O usuário informa um valor 
    - print() > O programa informa um valor

explorando o código no: "./programas/f-in-out.py"

## Tipos de Operadores com Python

### **Operadores Aritméticos** 
Executam operações matemáticas, como adição, subtração com operandos.

    - "+": adição      
    - "-": subtração
    - "*": multiplicação
    - "/": divisão
      
    nota. "//" divide em números inteiros

explorando o código no: "./programas/op-aritmeticos.py"

### **Operadores de Comparação** 
São operadores utilizados para comparar dois valores

    - "> (Maior que)":	Verifica se um valor é maior que outro	
    - "< (Menor que)":	Verifica se um valor é menor que outro	
    - "== (Igual a)":	Verifica se um valor é igual a outro	
    - "!= (Diferente de)":	Verifica se um valor é diferente de outro 
    - ">= (Maior ou igual a)":	Verifica se um valor é maior ou igual a outro
    - "<= (Menor ou igual a)":	Verifica se um valor é menor ou igual a outro	

explorando o código no: "./programas/op-comp.py"

### **Operadores de Atribuição** 
São operadores utilizados para definir o valor inicial ou sobrescrever o valor de uma variável

    - "=":	x = 1	
    - "+=":	x += 1	
    - "-=":	x -= 1	
    - "*=":	x *= 1	
    - "/=":	x /= 1	
    - "%=":	x %= 1	

explorando o código no: "./programas/op-atribuição.py"

### **Operadores de Lógicos** 
São operadores utilizados em consjunto com os operadores de comparação, para montar uma expressão lógica. Quando um operador de comparação é utilizado, o resultado retornado é um booleano, dessa forma podemos combinar operadoresde comparação com os operadores lógicos.

    - "and": Conjunção -> Retorna True se ambos os operandos tiverem o valor True
    - "or": Disjunção  -> Retorna True se um dos operandos tiver o valor True
    - "not": Negação   -> Inverte o resultado lógico

    nota. O tipo do resultado com esses operadores é bool (True ou False)

explorando o código no: "./programas/op-logicos.py"


### **Operadores de Identidade** 
São operadores utilizados para comparar se os dois objetivos testados ocupam a mesmo posição na memória.

    - "is": Retorna True se as variáveis comparadas forem o mesmo objeto
    - "is not":	Retorna True se as variáveis comparadas não forem o mesmo objeto


explorando o código no: "./programas/op-identidade.py"


### **Operadores de Associação** 
São utilizados para verificar se um objetivo está presente em uma sequência.

    - "in": Retorna True caso o valor seja encontrado na sequência
    - "not in": Retorna True caso o valor não seja encontrado na sequência


explorando o código no: "./programas/op-associacao.py"
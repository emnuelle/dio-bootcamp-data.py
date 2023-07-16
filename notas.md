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
   
nota "//" divide em números inteiros

explorando o código no: "./programas/op-aritmeticos.py"

### **Operadores de Comparação** 


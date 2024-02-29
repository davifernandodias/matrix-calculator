class calculadora_matrizes: # dimensoes
    def __init__(self,n_linhas,n_colunas,n_linhas_dois,n_colunas_dois):
        self.matriz_one =[]
        self.matriz_two =[]
        self.n_linhas= n_linhas
        self.n_colunas = n_colunas
        self.n_linhas_dois= n_linhas_dois
        self.n_colunas_dois = n_colunas_dois
        
    

    def criar_matriz(self):
        for i in range(self.n_linhas): # primeira matriz
            lista =[]
            for j in range(self.n_colunas):
                add=int(input("adiciona numero: "))
                lista.append(add)
            self.matriz_one.append(lista)
        print("deu certo")
         
        

        for i in range(self.n_linhas_dois): # segunda matriz
            lista_dois =[]
            for j in range(self.n_colunas_dois):
                add_dois=int(input("adiciona numero: "))
                lista_dois.append(add_dois)
            self.matriz_two.append(lista_dois)
        print("deu certo")
        
    def somar_matriz(self):
        result=[]
        for i in range(len(self.matriz_one)):
            result.append([])
            for j in range(len(self.matriz_one[0])):
                result[i].append(self.matriz_one[i][j] + self.matriz_two[i][j])
        print(result)
                

menu = '''                MATRIZES CAL

        [1] SOMA DE MATRIZES
        [2] SUBTRAÇÃO DE MATRIZES
        [3] MULTIPLICAÇÃO DE MATRIZES
        [4] EXIT
    
    '''

while True:
    print(menu)
    opcao= int(input("digite opção: "))
    if opcao == 1:
        print(f"vc escolheu opção soma das matrizes")
        # ad1,d2,d3,d4 = input("digite as dimensoes: ").split(" ")
        matriz1 = calculadora_matrizes(2,2,2,2)
        matriz1.criar_matriz()
        matriz1.somar_matriz()
        break




        
# TODO INFORMAR MATRIZES DIMENSSOES DA MATRIZES 

    # FUNCÃO PARA CRIAR MATRIZES 
            # DIMENSÃO LINHA X COLUNA
             # INPUT PECORRER VALOR E ADICIONAR A MATRIZ


    # ESTRUTURA IF

    # CONDIÇÃO +

    # CONDIÇÃO -

    # CONDIÇÃO *



class calculadora_matrizes: # PARAMETROS => LINHAS X COLUNAS
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
                lista.append(int(input("adiciona numero: ")))
            self.matriz_one.append(lista)
        print('''
                criado com sucesso''')

        for i in range(self.n_linhas_dois): # segunda matriz
            lista_dois =[]
            for j in range(self.n_colunas_dois):
                add_dois=int(input("adiciona numero: "))
                lista_dois.append(add_dois)
            self.matriz_two.append(lista_dois)
        print('''
                criado com sucesso''')
          


    def somar_matriz(self):
        if self.n_colunas!=self.n_colunas_dois and self.n_linhas != self.n_linhas_dois:
            print('Operação invalida,para soma-las devem ser de mesmo tamanho:')
            while True:
                print('''
                      
                      Deseja inserir a matriz novamente?:[s][n]
                      
                      ''')
                r=input()
                if r.lower()=='s':
                    pass
                else:
                    break
        else:        
            result=[]
            for i in range(len(self.matriz_one)):
                result.append([])
                for j in range(len(self.matriz_one[0])):
                    result[i].append(self.matriz_one[i][j] + self.matriz_two[i][j])
            for k in range(2):        
                print(f"MATRIZ GERADA: {result[k]}")
                #print(result[k])

    def subtrair_matriz(self):
        if self.n_colunas!=self.n_colunas_dois and self.n_linhas != self.n_linhas_dois:
            print('Operação invalida,para soma-las devem ser de mesmo tamanho:')
            while True:
                print('''
                      
                      Deseja inserir a matriz novamente?:[s][n]
                      
                      ''')
                r=input()
                if r.lower()=='s':
                    pass
                else:
                    break
        else:        
            result=[]
            for i in range(len(self.matriz_one)):
                result.append([])
                for j in range(len(self.matriz_one[0])):
                    result[i].append(self.matriz_one[i][j] - self.matriz_two[i][j])
            print(f"MATRIZ GERADA: {result}")

    def multiplicar_matriz(self):
        if self.n_colunas != self.n_linhas_dois:
            print('Operação invalida,para soma-las devem ser de mesmo tamanho:')
            while True:
                print('''
                      
                      Deseja inserir a matriz novamente?:[s][n]
                      
                      ''')
                r=input()
                if r.lower()=='s':
                    pass
                else:
                    break
        else:            
            result=[]
            for i in range(self.n_linhas):
                result.append([])
                for j in range(self.n_colunas_dois):
                    result[i].append(0)
                    for k in range(self.n_colunas):
                        result[i][j] += self.matriz_one[i][k] * self.matriz_two[k][j]
            print(f"MATRIZ GERADA: {result}")
                    

menu = '''                MATRIZES CAL

        [1] SOMA DE MATRIZES
        [2] SUBTRAÇÃO DE MATRIZES
        [3] MULTIPLICAÇÃO DE MATRIZES
        [4] EXIT
    
    '''

while True:                 # WHILE PARA DAR INICIO AO MENU E INICIAR COM SISTEMAS DE CONDICIONAIS
    print(menu) 
    opcao= int(input("digite opção: "))
    if opcao == 1:                                         #PRIMEIRA CONDIÇÃO SOMA
        print(f"vc escolheu opção soma das matrizes")
        # ad1,d2,d3,d4 = input("digite as dimensoes: ").split(" ")
        matriz1 = calculadora_matrizes(2,2,2,2)
        matriz1.criar_matriz()
        matriz1.somar_matriz()
        char = input('''
        
        deseja fazer mais conta?: S/N''')
        if char.lower() == "s":
            pass
        elif char.lower() == "n":
            break
        else:
            print('***  Digite uma opção valida  ***')
            pass

    elif opcao == 2:                                         #SEGUNDA CONDIÇÃO SUBTRAÇÃO
        print(f"vc escolheu opção subtrair as matrizes")
        # ad1,d2,d3,d4 = input("digite as dimensoes: ").split(" ")
        matriz1 = calculadora_matrizes(2,2,2,2)
        matriz1.criar_matriz()
        matriz1.subtrair_matriz()
        char = input('''
        
        deseja fazer mais conta?: S/N''')
        if char.lower() == "s":
            pass
        elif char.lower() == "n":
            break  
        else:
            print('***  Digite uma opção valida  ***')
            pass

    elif opcao == 3:                                            #TECERICA CONDIÇÃO MULTIPLICAÇÃO
        print(f"vc escolheu opção multiplicar as matrizes")
        # ad1,d2,d3,d4 = input("digite as dimensoes: ").split(" ") 
        matriz1 = calculadora_matrizes(2,2,2,2)
        matriz1.criar_matriz()
        matriz1.multiplicar_matriz()
        char = input('''
        
        deseja fazer mais conta?: S/N   ''')
        if char.lower() == "s":
            pass
        elif char.lower() == "n":
            break
        else:
            print('***  Digite uma opção valida  ***')
            pass

    elif opcao == 3:                                        #QUARTA CONDIÇÃO SAIR
        print("VOCE SAIU DA CALCULADORA...BYEE")
        break
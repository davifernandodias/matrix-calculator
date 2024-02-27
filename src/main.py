def menu():
    menu = '''                MATRIZES CAL

            [1] SOMA DE MATRIZES
            [2] SUBTRAÇÃO DE MATRIZES
            [3] MULTIPLICAÇÃO DE MATRIZES
            [4] EXIT
        
        '''

    return menu

def matriz():
    mat = []
    mat2= []
    option = -3
    while option != 4:
        print(menu())
        option = int(input("digite a option: "))
        if option == 4:
            break
        


        elif option == 1:
            order1 = int(input("linhas:"))
            order2 = int(input("colunas:"))
            def order(n_linhas,n_colunas):
                for linhas in range(n_linhas):
                    lista = []
                    for colunas in range(n_colunas):
                        add_number = float(input("digite numero: "))
                        lista.append(add_number)
                    mat.append(lista)
                print(f"MATRIZ CRIADA: \n{mat}")
                # matriz 2
                print(f"MATRIZ TWO")
                n_linhas2 = int(input("linhas:"))
                n_colunas2 = int(input("colunas:"))
                for linhas2 in range(n_linhas2):
                    lista2 = []
                    for colunas2 in range(n_colunas2):
                        add_number2 = float(input("digite numero: "))
                        lista2.append(add_number2)
                    mat2.append(lista2)
                print(f"MATRIZ CRIADA: \n{mat2}")

                def somar_matriz():
                    if n_linhas == n_linhas2 and n_colunas == n_colunas2:
                        for i in mat:
                            print(i)
                            
                            
                somar_matriz()
            order(order1,order2)
            break
            
            
                

print(matriz())
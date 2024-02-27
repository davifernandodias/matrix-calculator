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
                for linhas in range(n_linhas+1):
                    lista = []
                    for n_colunas in range(n_colunas+1):
                        add_number = float(input("digite numero: "))
                        lista.append(add_number)
                    mat.append(lista)
                print(mat)
            order(order1,order2)
            break
            
            
                

print(matriz())
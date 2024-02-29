matriz1= [
    [1,2,3,4]

]

matriz2= [
    [1,4,3,4]
]



# deixar matriz só com um array
ma = []

for valores_matriz_one in matriz1: 
    for valores_matriz_two in matriz2:
        matriz_new =[]
        for valores in range(4):
            new = valores_matriz_one[valores] + valores_matriz_two[valores]
            matriz_new.append(new)
        print(matriz_new)



matriz1= [
    [1,1,1,1],
    [1,1,1,1],

]

matriz2= [
    [1,1,1,1],
    [1,1,1,1]
]



# deixar matriz só com um array
ma = []
for tamanho in range(len(matriz1)):
    for valores_matriz_one in matriz1: 
        for valores_matriz_two in matriz2:
            matriz_new =[]
            for valores in range(4):
                new = valores_matriz_one[valores] + valores_matriz_two[valores]
                matriz_new.append(new)
            
        ma.append(matriz_new)
    print(matriz_new)


# [2,6,6,8],
# [2,4,5,8]
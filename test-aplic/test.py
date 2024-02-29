matriz1= [
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],

]                       #[4,5,6,7]
                        #[2,2,2,2]
                        #[4,5,6,7]
                        #[2,2,2,2]

matriz2= [
    [3,4,5,6],
    [1,1,1,1],
    [3,4,5,6],
    [1,1,1,1]
]



# deixar matriz só com um array
ma = []

for i in range(len(matriz1)):
    ma.append([])
    for j in range(len(matriz1[0])):
        ma[i].append(matriz1[i][j] + matriz2[i][j])
print(ma)

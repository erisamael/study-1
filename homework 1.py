X = [[12,7,3],[4,5,6],[7,8,9]]
Y = [[5,8,1],[6,7,3],[4,5,9]]
Z = [["","","",],["","","",],["","","",]]
for i in range(3):
    for m in range(3):
        Z[i][m] = int(X[i][m]) + int(Y[i][m])
print (Z)

#this is another idea
H =[]
for a in range(3):
    H.append([])
    for b in range(3):
        H[a].append(X[a][b]+Y[a][b])
print(H)

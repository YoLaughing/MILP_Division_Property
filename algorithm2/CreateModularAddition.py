index = 0
for i in range(64):
    for j in range(64):

        #print("------" + str(i)+" sub "+str(j)+":", end=" ")
        #print(str(hex(i))+str(hex(j)))
        sum = (i - j) % 64
        #print(str(sum)+", ", end=" ")
        print(hex(sum)+", ", end=" ")

"""
make this pattern
*
* *
* * *
* * * *
* * * * *
"""
#declare how many rows you want
row = int(5)
#outer loop making how much row from variable row
for i in range(1,row+1):
    #inner loop itarates over the number printed each row
    for j in range(1, i+1):
        #print "*" and "end = "" " is for have the same line
        print("*", end=" ")
    print()

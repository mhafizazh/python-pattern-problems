'''
    *
   ***
  *****
 *******
*********
'''
row = 5
for i in range(1, row + 1):
    for j in range(2 * row - 1):
        if j < row - i or j >= row + i - 1:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()


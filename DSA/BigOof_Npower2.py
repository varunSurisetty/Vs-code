#the executions will be of N * N so
#time complexity will be O(N**2)


def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
print_items(10)
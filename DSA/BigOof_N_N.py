#whether program has 2 or more N executions
#snippets... program will be of O(N)
### Drop the constant for simplification
def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
        
print_items(10)
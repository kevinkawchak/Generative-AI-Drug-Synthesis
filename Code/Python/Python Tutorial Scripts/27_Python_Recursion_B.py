def fibonnaci(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a+b
    return a

print(fibonnaci(3000))

# Recursion error
def fibonacci2(n):
    if n <= 1:
        return n
    else:
        return (fibonacci2(n-1) + fibonacci2(n-2))
    
print(fibonacci2(3000))
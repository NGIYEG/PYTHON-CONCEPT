def calculate_sum(n):
    
    total = 0
    
    for i in range(n+1):
        total += i
    
    return total
    
result = calculate_sum(100)
print(result) 
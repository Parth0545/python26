numbers=[45,21,89,56,76]

largest=numbers[0]
 
for i in numbers:
    if i>largest:
        largest=i
        
print("largest numbers",largest)
string="Information technology"

count=0

for ch in string:
    if ch in "aeiou":
        count=count+1
        
print("total vowels",count)
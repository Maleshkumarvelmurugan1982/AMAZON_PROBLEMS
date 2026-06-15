s = input("Enter the string: ")
sub = ""      
maxi = 0  
for char in s:
    if char in sub:
        sub = sub[sub.index(char) + 1:]
    sub += char  
    maxi = max(maxi, len(sub))
print("Length of longest substring:", maxi)

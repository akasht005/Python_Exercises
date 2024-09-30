
def vowels(n):
    
    n = n.lower()
    result = 0
    for i in n:
        
        if i == "a" or i == "i" or i == "e" or i =="o" or i =="u":
            
            result = result + 1

    return result
      
x = input("Enter a string : ")
y = vowels(x)

if y == 0:

    print("Vowels not found...")
                
else:

    print("Vowels found : ", y)
       

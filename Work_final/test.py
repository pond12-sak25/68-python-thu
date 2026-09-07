try :
    numbers = int(input("กรอก :" ))
    bobp = []
   
    for i in range(1,numbers+1,1):
        
        if numbers % i  ==0   :
           bobp.append(i)
           print(bobp)
    if len(bobp)==2:
        print("prime")
    else:
        print("Noprime")
        
    
    
    
    
    
    
    
except:
    print("ผิดพลาด")
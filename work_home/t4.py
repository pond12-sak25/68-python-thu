def calculate_sum_and_average() -> None:
     
    joyuan = list()
    
    for i in range(5):
        imguan = float(input(f'Enter {i+1} :'))
        joyuan.append(imguan)
   
    
    total = sum(joyuan)
    avarest = total /len(joyuan)
    
    return(total,avarest)
     
    
retum =calculate_sum_and_average()
print(retum)
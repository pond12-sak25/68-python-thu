try:
    sum = 0
    khon = 0
    while True:
       score = int(input("กรอกเลข :" ,))
       
       
       if score ==-1:
        break
    
       sum += score
       khon += 1
       
    if khon > 0:
        average = sum / khon
        print("คะแนนเฉลี่ย =", average)
    else :
     print("ไม่มีคะแนนให้คำนวณ")

       
        
except :
    print("Kuy")
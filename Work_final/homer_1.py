from typing import List

def find_divisors(n: int) -> List[int]:
    divisors = []          # list เก็บตัวประกอบ
    i = 1
    while i <= n:          # วนตรวจตั้งแต่ 1 จนถึง n
        if n % i == 0:     # ถ้า i หาร n ลงตัว
            divisors.append(i)  # เก็บค่า i ลงใน list
        i += 1
    return divisors        # คืนค่าลิสต์ตัวประกอบ

# ทดลองใช้
number = int(input("Enter a number: "))
print("Divisors of", number, ":", find_divisors(number))
    

     




    
       
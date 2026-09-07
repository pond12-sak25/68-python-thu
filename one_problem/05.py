from typing import List

def find_divisors(n: int) -> List[int]:
    pass
    num = 1
    mon = []
    while(num <= n):
        if n % num == 0:
            mon.append(num)
        num += 1
    return(mon)
       



jo = 20
print(find_divisors(jo))




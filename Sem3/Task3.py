# 3.Составить список простых множителей натурального числа N

def facs(n):
   i = 2
   list_factor = []
   while i <= n:
       if n % i == 0:
           list_factor.append(i)
           n /= i
       else:
           i += 1
   return list_factor


print(facs(63))

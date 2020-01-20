# Input
nterms = int(input("Terminalga son kiriting"))
# Fibonacci sonlarinig 1 va 2 sonlari
n1, n2 = 0, 1
count = 0
# kiritilgan soni tog'riligni tekshirish
if nterms <= 0:
   print("Iltimos musbat son kiriting")
elif nterms == 1:
   print("Fibonacci ketma ketligi:")
   print(n1)
else:
   print("Fibonacci ketma ketligi:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # qiymatlarni yengilash
       n1 = n2
       n2 = nth
       count += 1
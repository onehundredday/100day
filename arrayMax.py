#max() build in function

print(max(1,2))

sonlar = [1, 9, 8, 0, 2, 7] #Iterable
print(max(sonlar))

print(max("Mirusmon", "Johon", "Valijon"))

#Eng kattasoni topish 1

sonlar = [1, 9, 8, 2, 7] 

def max_elementni_topish(element):
  eng_katta_son = 0
  for x in element:
    if x > eng_katta_son:
      eng_katta_son = x
  return eng_katta_son

print(max_elementni_topish(sonlar))

#Universal roq katta soni topish

sonlar = [-1, -9, -8, -2, -7] 

def univesalroq_max_elementni_topish(element):
  eng_katta_son = sonlar[0]
  for x in element:
    if x > eng_katta_son:
      eng_katta_son = x
  return eng_katta_son

print(univesalroq_max_elementni_topish(sonlar))


#for i in range(0, 1000000000):
 #   if (i * 3) % 72 == 1:
  #      print(i)

c, n = 0, 0
chet, nechet = [], []
for i in range(0, 786):
    chet.append(i) if i % 2 == 0 else nechet.append(i)
print("Четные числа: ", *chet, "\nНечетные числа: ", *nechet)
print("\nКоличество: ", "\n---Четных: ", len(chet), "\n---Нечетных: ", len(nechet))

print(c.__dir__())
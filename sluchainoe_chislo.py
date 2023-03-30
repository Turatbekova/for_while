import random
target = random.randint(0,100)
popytka = 10

while popytka > 0:
  number = int(input('Vvedite vashe chislo: '))
  popytka -= 1
  if number == target:
    print("vy ugdali")
    break
  elif number >= target:
    print("vashe chislo bolwe zadannoi")
  elif number <= target:
    print("Vashe chislo menwe zadannoi")

  if popytka == 0:
    print(f'vy proigrali, zadannoe chislo bylo {target}')
  
digit = (1,101)
print(digit)

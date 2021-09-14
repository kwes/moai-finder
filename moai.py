import random

blue = '\033[94m'
cyan = '\033[96m'
green = '\033[92m'
end = '\033[0m'
moai = 0
mony = 0
while True:
  found = random.randint(1, 5)

  x = input(f"{green}moai.finder-$ {end}")
  if x == "find" or x == "f":
    if found <= 3:
      print(f"{blue} no moai located{end}")
    elif found == 5:
      print(f"{blue} moai located +1 moai{end}")
      moai = moai + 1
    elif found == 4:
      print(f"{blue} while trying to find a moai, you found a mony{end}")
      mony = mony + 1
  if x == "moais":
    print("moais")
    print(moai)
    print("mony")
    print(mony)
  if x == "help":
    print(f"{cyan} find (or f for spammers) - attempt to find a moai \n moais - shows current amount of moais and mony \n shop - buy some stuff{end}")
  if x == "shop":
    z = input(f"{green}SHOP \n BUY \n  moai|2 mony|type moai to buy -- {end}")
    if z == "moai" and mony >= 2:
      print(f"{blue}bought moai{end}")
      moai = moai + 1
      mony = mony - 2
    elif z == "moai" and mony < 2:
      print(f"{blue}cant buy moai too poor{end}")

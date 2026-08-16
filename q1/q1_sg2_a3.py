yob = int(input("Enter your birth year:"))

if yob < 1900:
  print("Invalid Year, it should not be earlier than 1900")
else:
  zod = (yob - 1900) % 12

  if zod == 0:
    zodiacsign = "Rat (鼠 / Shǔ)"
  elif zod == 1:
    zodiacsign = "Ox (牛 / Niú)"
  elif zod == 2:
    zodiacsign = "Tiger (虎 / Hǔ)"
  elif zod == 3:
    zodiacsign = "Rabbit (兔 / Tù)"
  elif zod == 4:
    zodiacsign = "Dragon (龙 / Lóng)"
  elif zod == 5:
    zodiacsign = "Snake (蛇 / Shé)"
  elif zod == 6:
    zodiacsign = "Horse (马 / Mǎ)"
  elif zod == 7:
    zodiacsign = "Goat (羊 / Yáng)"
  elif zod == 8:
    zodiacsign = "Monkey (猴 / Hóu)"
  elif zod == 9:
    zodiacsign = "Rooster (鸡 / Jī)"
  elif zod == 10:
    zodiacsign = "Dog (狗 / Gǒu)"
  else:
    zodiacsign = "Pig (猪 / Zhū)"

print(f"Your Chinese Zodiac is: {zodiacsign}")

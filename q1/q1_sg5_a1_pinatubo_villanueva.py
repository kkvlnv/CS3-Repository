class Hero:
  def __init__(self, name, hp):
    self.name = name
    self.hp = hp

  def hurt(self, amount):
    self.hp = self.hp - amount

arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)
arthur.hurt(10)

print(f"{arthur.name} HP: {arthur.hp}\n{morgana.name} HP: {morgana.hp}")

class Glassware:
  def __init__(self):
    print("Glassware created")
  def __del__(self):
    print("Glassware is gone")

class Beaker(Glassware):
  def __init__(self):
    super().__init__()
    print("Beaker created")
  def __del__(self):
    print("Beaker is missing")

class Tray:
  def __init__(self):
    print("Tray created")
    self.beakers = [
       Beaker(),
       Beaker(),
       Beaker(),
       Beaker(),
       Beaker()
    ]
  def __del__(self):
    del self.beakers
    print("Tray is missing")

tray = Tray()
del tray

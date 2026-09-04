class Lab:
  def __init__(self, room_number):
    self.room_number = room_number

class Technician:
  def __init__(self, name):
    self.name = name
    self.assigned_lab = None

  def assign_lab(self, lab_object):
    self.assigned_lab = lab_object

chem_lab = Lab("302")
mr_cruz = Technician("Mr. Cruz")
mr_cruz.assign_lab(chem_lab)
print(mr_cruz.assigned_lab.room_number)

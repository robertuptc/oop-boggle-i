from asyncore import file_dispatcher
import string
import random

class BoggleBoard:

  def __init__(self):
    for n in range(4):
      self.first_line = "____"
      print(self.first_line)
      self.dice_dict = {
        1 : "AAEEGN",
        2 : "ELRTTY",
        3 : "AOOTTW",
        4 : "ABBJOO",
        5 : "EHRTVW",
        6 : "CIMOTU",
        7 : "DISTTY",
        8 : "EIOSST",
        9 : "DELRVY",
        10: "ACHOPS",
        11: "HIMNQU",
        12: "EEINSU",
        13: "EEGHNW",
        14: "AFFKPS",
        15: "HLNNRZ",
        16: "DEILRX"
      }
# 
  def shake(self):
      count = 0
      
      for n in range(4):
        line = ""
        for k in range(4):
          count += 1
          filtering_q = ""
          filtering_q += random.choice(self.dice_dict[count])

          if filtering_q == 'Q':
            line += 'Qu '
          else:
            line += filtering_q 
            line += "  "
        print(line)

game = BoggleBoard()
game.shake()

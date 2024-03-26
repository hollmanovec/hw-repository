# Write a function that printsa horizontal or vertical line made out of some symbol. The finction takes the following as a parameter: the line's length. direction, symbol

def function(length, direction, symbol):
  if direction == "vertical":
    for _ in range (length):
      print(symbol)
  if direction == "horizontal":
    print(symbol*length)

function(5, "vertical", "*")
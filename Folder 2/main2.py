#Write a function that takes two numbers as a parameter and displays all odd numbers inbetween

num1 = int(input("zadejte první číslo:"))
num2 = int(input("zadejte druhé číslo:"))

def odd_numbers():
  for i in range(num1, num2):
    if i % 2 == 1:
      print(i, end=" ")

odd_numbers()


def odd_numbers2(start=0, end =10):    #0 a 10 předdefinováno, můžeme to přebít
  for i in range(start, end):          # end a start může být i prohozené v tom definování,
    if i % 2 == 1:                     #protože samotná funkce to má správně
      print(i, end=" ")

odd_numbers2()
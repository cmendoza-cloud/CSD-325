# Carmen Mendoza 
# 10/26/2024 
# Module 1.3 

def beer_song(bottles):
  """
  This function manages the countdown of bottles of beer on the wall
  """
  while bottles > 1:
      print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
      print(f"Take one down and pass it around, {bottles - 1} bottle(s) of beer on the wall.\n")
      bottles -= 1
  if bottles == 1:
      print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
      print(f"Take one down and pass it around, no more bottles of beer on the wall.\n")
  print("Go to the store and buy some more!")

bottles = int(input("Enter number of bottles: "))
beer_song(bottles)

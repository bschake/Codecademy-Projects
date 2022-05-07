'''
python dictionaries exercise
Prompt:
In this project, you will process some data from a group of friends playing scrabble. You will use 
dictionaries to organize players, words, and points.

There are many ways you can extend this project on your own if you finish and want to get more practice!
'''
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letter_to_points = {key:value for key, value in zip(letters,points)}
letter_to_points.update({" ":0})
print(letter_to_points)
def score_word(word):
  point_total = 0
  for item in word:
    point_total += letter_to_points.get(item,0)
  return point_total

brownie_points = score_word("BROWNIE") 
print(brownie_points)

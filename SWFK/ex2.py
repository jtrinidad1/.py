#Exercise 2
#If you have 3 boxes containing 25 chocolates, and 10 bags containing 32 sweets, how
#many sweets and chocolates do you have in total? (Note: you can do this with one
#equation with the Python console)

boxes = 3
chocolates = 25
bags = 10
sweets = 32

#I'm not sure if they mean 3 boxes for 25 chocolates total, or 1 box = 25 chocolates, and #there are 3 boxes total...
#Let's try this:

chocosweets = ((boxes*chocolates) + (bags * sweets))
text = "There are % total sweets and chocolates"
print text % chocosweets
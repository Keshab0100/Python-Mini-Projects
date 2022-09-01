# In this game, we will be using string concatenation
# ex:
# name = "Keshab"

# print("my name is " + name)
# print("my name is {}".format(name))
# print(f"my name is {name}")  #this is an f string, declared by just adding f in the start, best way

word1 = input("enter some word")
word2 = input("enter some word")
word3 = input("enter some word")
word4 = input("enter some word")
word5 = input("enter some word")
madlib = f"I live in a {word1}, with two of my friends who are {word2}. I recently started learning {word3}, and this is my first {word4} handson.\
I am looking forward to make {word5} things in python and use them."
print(madlib)

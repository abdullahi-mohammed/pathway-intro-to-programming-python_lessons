# Author: Abdullahi Mohammed
# Date:   13th, jan. 2024.
# Purpose: Learning how to use strings

# Stretch Challenge: I addded this extra sentence - Before it could reach over to us people have already {verb4} to help us and it became {article} {noun}

# Please enter the following:
print("Please enter the following:")

# adjective: happy
adjective = input("adjective: ")
# animal: zebra
animal = input("animal: ")
# verb: sneeze
verb = input("verb: ")
# exclamation: hooray
exclamation = input("exclamation: ")
# verb: read
verb1 = input("verb: ")
# verb: drive
verb2 = input("verb: ")
verb4 = input("verb: ")
vowels = ("a","e","i","o","u")
noun = input("noun: ")

art = noun.startswith(vowels)

if art:
    article = "an"
else:
    article = "a"

# Your story is:
print("Your story is: ")
print( f"The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb} down the hallway. \"{exclamation}!\" I yelled. But all I could think to do was to {verb1} over and over. Miraculously, that caused it to stop, but not before it tried to {verb2} right in front of my family. Before it could reach over to us people have already {verb4} to help us and it became {article} {noun}.")

# The other day, I was really in trouble. It all started when I saw a very
# [adjective] [animal] [verb] down the hallway. "[exclamation]!" I yelled. But all
# I could think to do was to [verb] over and over. Miraculously,
# that caused it to stop, but not before it tried to [verb]
# right in front of my family.
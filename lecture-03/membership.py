fruits = ["apple", "banana", "cherry"]

# Using 'in' operator
print ("banana" in fruits) # True, since "banana" is in the list 
print ("orange" in fruits) # false, since "orange" is in the list 

# Using 'not in' operator
print("grape" not in fruits) # True, since "grape" is not in the list
print ("apple" not in fruits) # False, since "apple" is in the list

# String example
sentence = "the quick brown fox jump over lazy dog."
print("fox" in sentence) # True, since "fox" is a substring of the sentence
print("cat" not in sentence) # True since "cat" is a substring of the sentence
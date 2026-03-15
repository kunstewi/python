import keyword

# Print all keywords
print(keyword.kwlist)

# Check if a string is a keyword
print(keyword.iskeyword("if"))     # True
print(keyword.iskeyword("gemini")) # False
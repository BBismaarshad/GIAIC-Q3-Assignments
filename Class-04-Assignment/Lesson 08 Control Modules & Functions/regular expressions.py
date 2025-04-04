import re

text = "The rain in Spain"

# Search for pattern
x = re.search("^The.*Spain$", text)
if x:
    print("Match found!")

# Find all matches
print(re.findall("ai", text))  # ['ai', 'ai']

# Split at each match
print(re.split("\s", text))    # ['The', 'rain', 'in', 'Spain']

# Replace matches
print(re.sub("\s", "-", text)) # The-rain-in-Spain
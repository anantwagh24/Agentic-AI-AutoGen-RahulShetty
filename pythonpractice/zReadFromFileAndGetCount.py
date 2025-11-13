
from pathlib import Path

# Step 1: Read file
content = Path("/Users/anantwagh/Documents/anant-test.rtf").read_text()
print(content)

# Step 2: Take user input
search_word = input("Enter any text to search: ").strip()

# Step 3: Count occurrences (case-insensitive)
count = content.lower().count(search_word.lower())

# Step 4: Print result
print(f"'{search_word}' appears {count} times in the file.")

from pathlib import Path

# Step 1: Read file
#/Users/anantwagh/Documents/anant-test.rtf
file = Path("/Users/anantwagh/Documents/anant-test.rtf").read_text()
print(file.strip())

search_input = input("enter input: ").strip()
#strip() removes leading and trailing whitespace from a string.
print(f"entered input is: {search_input}")

count = file.lower().count(search_input.lower())
print(count)

# When to use: ➡️ When you need key-value pairs (like “name → phone”, “roll → marks”).
from openpyxl.worksheet.print_settings import PRINT_AREA_RE

# Creating a dictionary of contacts
contacts = {
    "John": "9876543210",
    "Sara": "9123456789",
    "Mike": "9876543210"  # duplicate value allowed, but keys must be unique
}

print("Phone Directory:", contacts)
print("Sara's number:", contacts["Sara"])

contacts1={
    "ANANT":"92839623",
    "RAHUL":"09483805",
    "SAHCIN":"938492348"
}
print(f"phone numbers:{contacts1}")
print(f"sara's contact: ", contacts1["ANANT"])

# - \d means “digit”
# - {10} means “repeat 10 times”
# - So \d{10} means “find 10 digits in a row”
# - findall() searches the text and returns all matches


# import re

# text = "My number is 9841234567, call me."

# match = re.findall(r"\d{10}", text)

# if match:
#     print("Phone number found:", match[0])
# else:
#     print("No phone number found")
import json
import sqlite3

# # Create a nested dictionary
# person = {
#     "name": "John Doe",
#     "age": 30,
#     "address": {
#         "street": "123 Main St",
#         "city": "Anytown",
#         "state": "CA"
#     }
# }

# # Convert person dictionary to JSON
# json_string = json.dumps(person, indent=4)  
# print(json_string)
con = sqlite3.connect(":memory:")
p = con.execute("PRAGMA database_list").fetchall()
print(p)
con.close()
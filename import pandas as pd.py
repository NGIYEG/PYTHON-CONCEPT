import pandas as pd

# Corrected data dictionary syntax
data = {
    'name': ['Alice', 'George', 'Ali'],
    'location': ['kilifi', 'nrb', 'juja'],
    'age': ['20', '23', '19']
}

# Create a DataFrame from the dictionary
m = pd.DataFrame(data)

# Print the DataFrame
print(m)

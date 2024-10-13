import random

# Function to generate random data
def generate_data(n):
    data = []
    for i in range(1, n + 1):
        data.append((i, random.randint(1, 10)))
    return data

# Function to save data to a file
def save_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item[0]} {item[1]}\n")

# Generate data
data = generate_data(5)

# Save data to file
save_to_file('data.dat', data)

print("Data has been generated and saved to random_data.txt")

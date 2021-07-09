from die import Die

# Create a D6
dice = Die()

# Make some rolls and store results in a list
results = []
for roll_num in range(100):
    result = dice.roll()
    results.append(result)

print(results)
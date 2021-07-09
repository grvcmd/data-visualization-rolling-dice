from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create a D6
dice_1 = Die()
dice_2 = Die()


# Make some rolls and store results in a list
results = []
for roll_num in range(1000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

# Analyze the results
frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of result'}
my_layout = Layout(title="Results of rolling two D6 1000 times",
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
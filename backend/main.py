from gurobipy import *

from field import neighbors, corners
from numbers_propabilities import numbers_probabilities
import gurobipy as gp


(_, hex_numbers, hex_resources) = multidict({
    'hex1': [7, 'desert'],
    'hex2': [8, 'wood'],
    'hex3': [9, 'sheep'],
    'hex4': [12, 'brick'],
    'hex5': [5, 'wheat'],
    'hex6': [10, 'sheep'],
    'hex7': [10, 'wood'],
    'hex8': [9, 'sheep'],
    'hex9': [4, 'wood'],
    'hex10': [6, 'brick'],
    'hex11': [3, 'ore'],
    'hex12': [6, 'wheat'],
    'hex13': [5, 'ore'],
    'hex14': [2, 'wheat'],
    'hex15': [4, 'wood'],
    'hex16': [11, 'ore'],
    'hex17': [11, 'wheat'],
    'hex18': [3, 'brick'],
    'hex19': [8, 'sheep']

})

resource_multipliers = {
    "wood": 0.7,
    "brick": 0.7,
    "wheat": 0.5,
    "ore": 0.5,
    "sheep": 0.5,
    "desert": 0.0
}

number_start_cities = 2

number_different_resources = 4

m = Model('Catan')
y = m.addVars(corners.keys(), vtype=GRB.BINARY, name="y")

m.setObjective(
    sum(y[k] * sum(numbers_probabilities[hex_numbers[hex]] * resource_multipliers[hex_resources[hex]] for hex in corners[k] if hex in hex_numbers) for k in corners),
    GRB.MAXIMIZE
)

m.addConstr(sum(y[k] for k in corners) == number_start_cities, name="max_start_positions")

m.addConstrs((y[corner] + y[neighbor] <= 1 for corner in neighbors for neighbor in neighbors[corner]), name="no_neighbors")


resource_vars = m.addVars(['wood', 'brick', 'wheat', 'ore', 'sheep'], vtype=GRB.BINARY, name="resource")

# Link resource variables to corners
for resource in resource_vars:
    m.addConstr(resource_vars[resource] <= sum(y[k] for k in corners if any(hex_resources[hex] == resource for hex in corners[k])), name=f"resource_{resource}")

# Ensure at least 3 different resources are selected
m.addConstr(gp.quicksum(resource_vars[resource] for resource in resource_vars) >= number_different_resources, name="min_resources")



m.write("test.lp")
m.optimize()


# Result
if m.status == GRB.OPTIMAL:
    print('Optimal solution found')
    for k in corners:
        if y[k].x > 0.5:
            print(f"Startplatz: {k} mit angrenzenden Hexfeldern: {corners[k]}" )
            for hex in corners[k]:
                print(f"Number: {hex_numbers[hex]} Resource: {hex_resources[hex]}")



else:
    print(f"Model not solved to optimality. Status: {m.status}")
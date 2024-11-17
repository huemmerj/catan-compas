import gurobipy as gp

from api.logic.field import neighbors, corners
from gurobipy import *


def solve_optimal_position(hex_data: dict[list[int, str]]):
    numbers_probabilities = {
        2: 0.028,
        3: 0.056,
        4: 0.083,
        5: 0.111,
        6: 0.139,
        7: 0.00,
        8: 0.139,
        9: 0.111,
        10: 0.083,
        11: 0.056,
        12: 0.028,
    }

    (_, hex_numbers, hex_resources) = multidict(hex_data)

    resource_multipliers = {
        "wood": 0.7,
        "brick": 0.7,
        "wheat": 0.5,
        "ore": 0.5,
        "sheep": 0.5,
        "desert": 0.0,
    }

    number_start_cities = 2

    number_different_resources = 4

    m = Model("Catan")
    y = m.addVars(corners.keys(), vtype=GRB.BINARY, name="y")

    m.setObjective(
        sum(
            y[k]
            * sum(
                numbers_probabilities[hex_numbers[hex]]
                * resource_multipliers[hex_resources[hex]]
                for hex in corners[k]
                if hex in hex_numbers
            )
            for k in corners
        ),
        GRB.MAXIMIZE,
    )

    m.addConstr(
        sum(y[k] for k in corners) == number_start_cities, name="max_start_positions"
    )

    m.addConstrs(
        (
            y[corner] + y[neighbor] <= 1
            for corner in neighbors
            for neighbor in neighbors[corner]
        ),
        name="no_neighbors",
    )

    resource_vars = m.addVars(
        ["wood", "brick", "wheat", "ore", "sheep"], vtype=GRB.BINARY, name="resource"
    )

    # Link resource variables to corners
    for resource in resource_vars:
        m.addConstr(
            resource_vars[resource]
            <= sum(
                y[k]
                for k in corners
                if any(hex_resources[hex] == resource for hex in corners[k])
            ),
            name=f"resource_{resource}",
        )

    # Ensure at least 3 different resources are selected
    m.addConstr(
        gp.quicksum(resource_vars[resource] for resource in resource_vars)
        >= number_different_resources,
        name="min_resources",
    )

    m.optimize()

    # Result
    if m.status == GRB.OPTIMAL:
        solution = []
        print("Optimal solution found")
        for k in corners:
            if y[k].x > 0.5:
                solution.append(k)
        return (True, solution)

    else:
        return (False, f"Model not solved to optimality. Status: {m.status}")

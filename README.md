# catan-spotter

## Project Overview

This project aims to find the best starting positions for the game *Settlers of Catan*. It is currently under development and will include several features to help players configure and analyze their optimal strategies in the game. 

### Key Features:
- **Board Configuration**: Users can configure the game board with resource tiles and number tiles.
- **Harbor Configuration**: Users can set the positions of harbors on the board.
- **Resource Importance**: Users can specify how important each resource is to their strategy (e.g., wood, brick, wheat, ore, sheep).
- **Harbor Importance**: Users can define how important harbors are in their strategy.
- **Built Settlements** (Planned Feature): Future versions will allow users to input built settlements (from themselves and other players), which will be considered in the optimal position calculation.

### How It Works:
The tool calculates optimal starting positions using a mathematical model that takes into account the board configuration, resource importance, harbor significance, and other relevant factors determined by the user. The model is designed to be aware of the game's rules, ensuring that:
- The user cannot input invalid configurations, such as incorrect resource distribution or improper number assignments.
- The model only generates valid and rule-conforming positions for settlements on the board, avoiding illegal placements.

Based on these inputs and rules, the tool suggests the best starting positions for the player.

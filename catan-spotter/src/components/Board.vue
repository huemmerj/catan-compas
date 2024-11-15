<template>
  <div class="board">
    <div v-for="(row, rowIndex) in structuredTiles" :key="rowIndex" class="row">
      <div v-for="(tile, tileIndex) in row" :key="tileIndex" class="tile-wrapper">
        <Tile :type="tile.type" :number="tile.number" />
      </div>
    </div>
  </div>
</template>

<script setup>
import Tile from './Tile.vue'

const tiles = [
  { type: 'wood', number: 5 },
  { type: 'brick', number: 8 },
  { type: 'sheep', number: 4 },
  { type: 'desert', number: null },
  { type: 'wheat', number: 9 },
  { type: 'ore', number: 6 },
  { type: 'wood', number: 11 },
  { type: 'brick', number: 3 },
  { type: 'sheep', number: 10 },
  { type: 'wheat', number: 2 },
  { type: 'ore', number: 12 },
  { type: 'brick', number: 6 },
  { type: 'sheep', number: 5 },
  { type: 'wood', number: 8 },
  { type: 'wheat', number: 4 },
  { type: 'ore', number: 3 },
  { type: 'brick', number: 10 },
  { type: 'sheep', number: 9 },
  { type: 'wood', number: 11 },
]

// Define the row pattern
const rowPattern = [3, 4, 5, 4, 3]

// Group tiles into rows based on the pattern
const structuredTiles = []
let tileIndex = 0

for (const rowLength of rowPattern) {
  structuredTiles.push(tiles.slice(tileIndex, tileIndex + rowLength))
  tileIndex += rowLength
}
</script>

<style scoped>
.board {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.row {
  display: flex;
  gap: 0.1em;
}

.tile-wrapper {
  margin-bottom: -1.4em;
}
</style>

<template>
  <div>
    <div class="board">
      <!-- Render rows with settlements and hexes -->
      <div v-for="(row, rowIndex) in structuredTilesWithSettlements" :key="rowIndex" class="row">
        <div v-if="row.type === 'settlement'" class="settlement-row">
          <div
            v-for="(settlement, settlementIndex) in row.tiles"
            :key="settlementIndex"
            class="settlement-wrapper"
          >
            <div class="settlement-placeholder"></div>
          </div>
        </div>
        <div
          v-else-if="row.type"
          v-for="(tile, tileIndex) in row.tiles"
          :key="tileIndex"
          class="tile-wrapper"
        >
          <Tile v-model:type="tile.type" v-model:number.number="tile.number" />
        </div>
      </div>
    </div>

    <button @click="getStartPositions">Find Startpositions</button>
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

// Create a new array that includes settlement rows between hex rows
const structuredTilesWithSettlements = []

for (let i = 0; i < structuredTiles.length; i++) {
  // Add settlement row before the current hex row
  if (i === 0) {
    structuredTilesWithSettlements.push({
      type: 'settlement',
      tiles: Array(rowPattern[i] + 1).fill(null),
    })
  }

  // Add the actual hex row
  structuredTilesWithSettlements.push({
    type: 'hex',
    tiles: structuredTiles[i],
  })

  // Add settlement row after the current hex row
  structuredTilesWithSettlements.push({
    type: 'settlement',
    tiles: Array(rowPattern[i] + 1).fill(null),
  })
}

const getStartPositions = async () => {
  console.log('Finding start positions...')
  console.log(tiles)
  const hexTiles = tiles.reduce((acc, tile, index) => {
    const hexNumber = index + 1 // Hex position starts from hex1

    // Replace null with 7 for desert
    const tileNumber = tile.type === 'desert' ? 7 : tile.number

    acc[`hex${hexNumber}`] = [tileNumber, tile.type]
    return acc
  }, {})

  const requestBody = {
    problem: hexTiles, // Wrap the hexTiles inside the "problem" field
  }
  try {
    const response = await fetch('http://localhost:9999/api/v1/solver/', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(requestBody),
    })

    if (response.ok) {
      const responseDataJson = await response.json()
      console.log(responseDataJson)
    } else {
      console.error('Error:', response.status)
    }
  } catch (error) {
    console.error('Error sending request:', error)
  }
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

.hex-row {
  margin-bottom: -1.4em;
}

.tile-wrapper {
  margin-bottom: -1.4em;
}

.settlement-row {
  display: flex;
  gap: 0.5em;
  justify-content: center;
  margin-bottom: -1em;
}

.settlement-wrapper {
  width: 1.5em;
  height: 1.5em;
  background-color: #ddd;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.settlement-placeholder {
  width: 1em;
  height: 1em;
  background-color: #bbb;
  border-radius: 50%;
}
</style>

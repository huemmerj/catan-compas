<template>
  <div class="board">
    <div v-for="(tile, index) in tiles" :key="index">
      <Tile :type="tile.type" :number="tile.number" />
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
</script>

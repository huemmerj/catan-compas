<template>
  <div class="hex-tile" :class="type">
    <span v-if="number !== null" class="tile-number">{{ number }}</span>
  </div>
</template>

<script setup>
defineProps({
  type: {
    type: String,
    required: true,
  },
  number: {
    type: [Number, null],
    default: null,
  },
})
</script>

<style scoped>
/* Base styling for the hex tile */
.hex-tile {
  width: 80px;
  height: 92px;
  clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
  display: flex;
  justify-content: center;
  align-items: center;
  background: #f0f0f0;
  border: 1px solid #ccc;
  font-size: 16px;
  font-weight: bold;
  color: #333;
  position: relative;
}

/* Styling for the number badge inside the tile */
.tile-number {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: rgba(255, 255, 255, 0.8);
  border-radius: 50%;
  padding: 4px 8px;
  font-size: 14px;
  font-weight: bold;
  color: #000;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

/* Specific type colors for the tiles */
.wood {
  background: #8fbc8f;
}

.brick {
  background: #b22222;
}

.desert {
  background: #f4a460;
}

.sheep {
  background: #98fb98;
}

.wheat {
  background: #ffd700;
}

.ore {
  background: #b0c4de;
}
</style>

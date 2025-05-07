<script setup>
import { ref, watch } from 'vue'
import { updateDentalExamMultiple } from '@/services/DentalService'

// Define props
const props = defineProps({
  layerNo: {
    type: Number,
    required: true
  },
  studentId: {
    type: Number,
    required: true
  },
  layerData: {
    type: Array,
    required: true
  }
})

// Reactive array of 16 arrays for multi-select values
const cells = ref([])

// Initialize `cells` from layerData
watch(
  () => props.layerData,
  (layerData) => {
    if (!Array.isArray(layerData)) return

    const temp = Array.from({ length: 16 }, () => []) // each cell starts as an empty array

    for (const item of layerData) {
      if (item.cell_no >= 0 && item.cell_no < 16) {
        try {
          // Parse stored JSON string if needed, or accept array directly
          temp[item.cell_no] = Array.isArray(item.value)
            ? item.value
            : JSON.parse(item.value)
        } catch {
          temp[item.cell_no] = []
        }
      }
    }

    cells.value = temp
  },
  { immediate: true }
)

// Watch for changes and sync with backend
watch(
  cells,
  async (newCells) => {
    const updates = newCells.map((valueArray, idx) => ({
      cell_no: idx,
      value: valueArray
    }))
    await updateDentalExamMultiple(props.studentId, props.layerNo, updates)
  },
  { deep: true }
)
</script>


<template>
    <tr>
        <td v-for="(value, index) in cells" :key="index">
            <select v-model="cells[index]" multiple size="4">
                <option value="Top">Top</option>
                <option value="Left">Left</option>
                <option value="Right">Right</option>
                <option value="Bottom">Bottom</option>
                <option v-if="index < 6 || index > 11" value="Middle">Middle</option>
                <option value="NA">NA</option>
            </select>
        </td>
    </tr>
</template>

<style scoped>
td {
    border: 1px solid black;
    border-collapse: collapse;
}
select {
    width: 100%;
    height: 100%;
}
</style>

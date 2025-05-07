<script setup>
import { ref, watch } from 'vue'
import { updateDentalExam } from '@/services/DentalService'

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

// Reactive array to hold 16 select values
const cells = ref([])

// Initialize `cells` with layerData when available
watch(
  () => props.layerData,
  (layerData) => {
    if (!Array.isArray(layerData)) return

    const temp = Array(16).fill('NA')

    for (const item of layerData) {
      if (item.cell_no >= 0 && item.cell_no < 16) {
        temp[item.cell_no] = item.value
      }
    }

    cells.value = temp
  },
  { immediate: true }
)
</script>

<template>
    <tr>
        <td v-for="(value, index) in cells" :key="index">
            <select v-model="cells[index]" @change="updateDentalExam(props.studentId, props.layerNo, index, cells[index])">
                <option value="NA">NA</option>
                <option value="F">F</option>
                <option value="X">X</option>
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
}
</style>

<script setup>
import { ref, watch } from 'vue'
import updateDentalExam from '@/services/DentalService'

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

// Optional: Emit changes to parent component
const emit = defineEmits(['update:cells'])

// Initialize `cells` with layerData when available
watch(
    () => props.layerData,
    (newLayerData) => {
        // Ensure it's always 16 items
        cells.value = [...newLayerData]
        while (cells.value.length < 16) {
        cells.value.push('NA')
        }
    },
    { immediate: true } // Run it once on component mount
)

// Emit changes when cells are modified
watch(cells, (newValues) => {
    emit('update:cells', { layerNo: props.layerNo, values: newValues })
},  { deep: true })
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

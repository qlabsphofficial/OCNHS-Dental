<script setup>
import { ref, watch } from 'vue'

// Define props
const props = defineProps({
    layerNo: {
        type: Number,
        required: true
    }
})

// Reactive array to hold 16 select values
const cells = ref(Array(16).fill('NA'))

// Optional: Emit changes to parent component
const emit = defineEmits(['update:cells'])

watch(cells, (newValues) => {
    emit('update:cells', { layerNo: props.layerNo, values: newValues })
}, { deep: true })
</script>

<template>
    <tr>
        <td v-for="(value, index) in cells" :key="index">
            <select v-model="cells[index]">
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

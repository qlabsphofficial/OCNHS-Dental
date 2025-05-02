<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
    layerNo: {
        type: Number,
        required: true
    }
})

const emit = defineEmits(['update:cells'])

// Initialize each cell with an empty array for multi-select
const cells = ref(Array.from({ length: 16 }, () => []))

watch(cells, (newValues) => {
    emit('update:cells', { layerNo: props.layerNo, values: newValues })
},  { deep: true })
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

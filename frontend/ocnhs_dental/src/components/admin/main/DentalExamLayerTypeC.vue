<script setup>
const props = defineProps({
    layerNo: {
        type: Number,
        required: true
    }
})
</script>

<template>
    <tr v-if="props.layerNo == 1">
        <td>18</td>
        <td>17</td>
        <td>16</td>
        <td>15</td>
        <td>14</td>
        <td>13</td>
        <td>12</td>
        <td>11</td>
        <td>21</td>
        <td>22</td>
        <td>23</td>
        <td>24</td>
        <td>25</td>
        <td>26</td>
        <td>27</td>
        <td>28</td>
    </tr>

    <tr v-else-if="props.layerNo == 2">
        <td>48</td>
        <td>47</td>
        <td>46</td>
        <td>45</td>
        <td>44</td>
        <td>43</td>
        <td>42</td>
        <td>41</td>
        <td>31</td>
        <td>32</td>
        <td>33</td>
        <td>34</td>
        <td>35</td>
        <td>36</td>
        <td>37</td>
        <td>38</td>
    </tr>
</template>

<style scoped>
td {
    border: 1px solid black;
    border-collapse: collapse;
}
</style>
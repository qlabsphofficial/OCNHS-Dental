<script setup>
</script>

<template>
    <div>
        <div>
            <h4 class="font-bold">Two-Factor Authentication</h4>
            <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Doloremque molestiae a quo quae voluptas porro distinctio placeat harum, ratione mollitia nobis atque omnis illum, ut eveniet eligendi modi! Ducimus, dolorem?</p>
        </div>

        <hr>
        
        <div class="mt-6">
            <h4>Email</h4>
            <div class="flex flex-row justify-between items-center">
                <input type="email">
                
                <div class="flex flex-row gap-5">
                    <button>Edit</button>
                    <button>Save</button>
                </div>
            </div>
        </div>

        <div class="mt-6">
            <h4>Contact Number</h4>
            <div class="flex flex-row justify-between items-center">
                <input type="text">

                <div class="flex flex-row gap-5">
                    <button>Edit</button>
                    <button>Save</button>
                </div>
            </div>
        </div>

        <div class="mt-6">
            <h4>Password</h4>
            <p class="mb-6">Lorem ipsum dolor sit amet.</p>

            <hr>

            <div class="flex flex-row justify-between items-center mt-6">
                <div>
                    <h4>Current Password</h4>
                    <input type="password">

                    <h4>Current Password</h4>
                    <input type="password">

                    <h4>Current Password</h4>
                    <input type="password">

                    <h4>Current Password</h4>
                    <input type="password">
                </div>

                <div class="flex flex-row gap-5">
                    <h4 class="font-bold text-lg">Password Rules</h4>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>
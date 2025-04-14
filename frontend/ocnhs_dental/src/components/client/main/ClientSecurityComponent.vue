<script setup>
</script>

<template>
    <div>
        <div>
            <h4 class="font-bold">Two-Factor Authentication</h4>
            <p class="mt-5 mb-5 lg:m-0">Two-factor authentication is an extra layer of security for your online accounts. It requires not only a password or username but also something that only you have access to.</p>
        </div>

        <hr>
        
        <div class="mt-6 mb-6">
            <h4 class="font-bold">Email</h4>
            <div class="flex flex-row justify-between items-center">
                <input type="email" class="p-2 border-2 rounded-md">
                
                <div class="flex flex-row gap-5">
                    <button>Edit</button>
                    <button>Save</button>
                </div>
            </div>
        </div>

        <hr>

        <div class="mt-6">
            <h4 class="font-bold">Contact Number</h4>
            <div class="flex flex-row justify-between items-center">
                <input type="text" class="p-2 border-2 rounded-md">

                <div class="flex flex-row gap-5">
                    <button>Edit</button>
                    <button>Save</button>
                </div>
            </div>
        </div>

        <div class="mt-6">
            <h4 class="font-bold">Password</h4>
            <p class="mb-6">Changing password helps maintain security by preventing unauthorized access. Changing password helps protect your personal data.</p>

            <div class="flex flex-col lg:flex-row justify-between items-center">
                <div class="flex-col items-center w-11/12 lg:w-auto">
                    <h4>Current Password</h4>
                    <input type="password" class="w-full lg:w-auto p-2 border-2 rounded-md">

                    <h4 class="mt-4">New Password</h4>
                    <input type="password" class="w-full lg:w-auto p-2 border-2 rounded-md">

                    <h4 class="mt-4">Confirm Password</h4>
                    <input type="password" class="w-full lg:w-auto p-2 border-2 rounded-md">
                </div>

                <div class="flex flex-col gap-5 bg-gray-300 p-10 mt-10 lg:mt-0">
                    <div>
                        <h4 class="font-bold text-lg">Password Rules</h4>
                        <p>To create a new password, you must meet all of the ff. requirements:</p>

                        <ul>
                            <li>Minimum 8 characters</li>
                            <li>Consists of letters and at least one number</li>
                            <li>Can't be the same as previous</li>
                        </ul>
                    </div>
                    <div class="mt-5">
                        <button class="rounded-md border-2 p-2">Change Password</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>
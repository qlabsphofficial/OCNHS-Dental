<script setup>
import { ref } from 'vue';
import { Eye, MenuSquare, Edit, Printer } from 'lucide-vue-next';

</script>

<template>
      <div v-if="!showStudentInfo" class="flex flex-col h-11/12 w-11/12 gap-5 p-10 border-2 rounded-md">
            <div class="flex flex-row items-between justify-between">
                  <h4 v-if="fileType == 'CURRENT'">{{ fileType }} / {{ curriculum }} / {{ gradeLvl }} / {{ section }}</h4>
                  <h4 v-else-if="fileType == 'OLD'">{{ fileType }} / {{ yearGraduated }} / {{ curriculum }}</h4>
                  <h4 v-else></h4>

                  <div class="w-1/4">
                        <div class="flex flex-row justify-between">
                              <div class="flex flex-col gap-4">
                                    <h4>FILE TYPE</h4>
                                    <select class="border-2" v-model="fileType">
                                          <option value="CURRENT">CURRENT</option>
                                          <option value="OLD">OLD</option>
                                    </select>
                              </div>

                              <div v-if="fileType == 'OLD'" class="flex flex-col gap-4">
                                    <h4>YEAR GRADUATED</h4>
                                    <select class="border-2" v-model="yearGraduated">
                                          <option value="2020">2020</option>
                                          <option value="2021">2021</option>
                                          <option value="2022">2022</option>
                                          <option value="2023">2023</option>
                                          <option value="2024">2024</option>
                                    </select>
                              </div>
            
                              <div class="flex flex-col gap-4">
                                    <h4>CURRICULUM</h4>
                                    <select class="border-2" v-model="curriculum">
                                          <option value="BEP">BEP</option>
                                          <option value="STE">STE</option>
                                          <option value="SPA">SPA</option>
                                          <option value="SPS">SPS</option>
                                          <option value="SPFL">SPFL</option>
                                          <option value="SPJ">SPJ</option>
                                          <option value="ICT">ICT</option>
                                          <option value="SPED">SPED</option>
                                          <option value="ALIVE">ALIVE</option>
                                          <option value="OHSP">OHSP</option>
                                          <option value="IPED">IPED</option>
                                    </select>
                              </div>
                              
                              <div v-if="fileType == 'CURRENT'" class="flex flex-col gap-4">
                                    <h4>GRADE LEVEL</h4>
                                    <select class="border-2" v-model="gradeLvl">
                                          <option value="GRADE 7">GRADE 7</option>
                                          <option value="GRADE 8">GRADE 8</option>
                                          <option value="GRADE 9">GRADE 9</option>
                                          <option value="GRADE 10">GRADE 10</option>
                                          <option value="GRADE 11">GRADE 11</option>
                                          <option value="GRADE 12">GRADE 12</option>
                                    </select>
                              </div>
                              
                              <div v-if="fileType == 'CURRENT'" class="flex flex-col gap-4">
                                    <h4>SECTION</h4>
                                    <select class="border-2" v-model="section">
                                          <option value="1">1</option>
                                          <option value="2">2</option>
                                          <option value="3">3</option>
                                          <option value="4">4</option>
                                          <option value="5">5</option>
                                          <option value="6">6</option>
                                          <option value="7">7</option>
                                          <option value="8">8</option>
                                          <option value="9">9</option>
                                          <option value="10">10</option>
                                    </select>
                              </div>
                        </div>
                  </div>
            </div>

            <div class="w-full">
                  <div class="flex w-full items-center justify-center mt-10 mb-5"><h1 class="text-3xl">STUDENT LIST (DENTAL EXAM)</h1></div>
                  <hr>

                  <table class="w-full mt-10">
                        <thead>
                              <tr>
                                    <th>FIRST NAME</th>
                                    <th>MIDDLE NAME</th>
                                    <th>LAST NAME</th>
                                    <th>BIRTHDATE</th>
                                    <th>VIEW</th>
                              </tr>
                        </thead>

                        <!-- TODO -->
                        <tr v-for="student, index of students" :key="student">
                              <td class="text-center p-1"></td>
                              <td class="text-center p-1"></td>
                              <td class="text-center p-1"></td>
                              <td class="text-center p-1"></td>
                              <td class="text-center p-1"><button @click="() => { showStudentInfo = true; }"><Eye /></button></td>
                        </tr>
                  </table>
            </div>
      </div>

      <div v-if="showStudentInfo" class="flex flex-col w-11/12 h-11/12 p-16 border-2 rounded-md">
            
      </div>
</template>

<style scoped>

</style>
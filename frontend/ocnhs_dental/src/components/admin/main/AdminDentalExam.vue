<script setup>
import { ref, watch } from 'vue';
import { Eye, MenuSquare, Edit, Printer } from 'lucide-vue-next';
import { retrieveStudentRecords } from '@/services/StudentRecordService';
import { retrieveMedicalHistory } from '@/services/MedicalHistoryService';

import DentalExamLayerTypeA from './DentalExamLayerTypeA.vue';
import DentalExamLayerTypeB from './DentalExamLayerTypeB.vue';
import DentalExamLayerTypeC from './DentalExamLayerTypeC.vue';

const fileType = ref('')
const yearGraduated = ref('')
const curriculum = ref('')
const gradeLvl = ref('')
const section = ref('')
const students = ref([])

//models
const goodHealth = ref(false);
const underMedicalTreatment = ref(false);
const treatmentCondition = ref('');
const seriousIllness = ref(false);
const illnessOrOperation = ref('');
const hospitalized = ref(false);
const hospitalizationDetails = ref('');
const takingMedications = ref(false);
const medicationsDetails = ref('');
const tobaccoUsage = ref(false);
const drugUse = ref(false);
const womenOnly = ref(false);
const womenCondition = ref('');
const hasToothbrush = ref(false);
const brushingTimes = ref(0);
const toothbrushChange = ref(0);
const useToothpaste = ref(false);
const dentistVisits = ref(0);

const healthConditions = ref([
      'Gingivitis',
      'Periodontal Disease',
      'Malocclussion',
      'Supernumerary Teeth',
      'Retained Deciduous Teeth',
      'Decubital Ulcer',
      'Calculus',
      'Cleft Lip / Palate',
      'Root Fragment',
      'Fluorosis',
      'Others, specify'
])

const dentalProcedures = ref([
      'DATE',
      'Examination',
      'Sealant (G.I.)',
      'Gum Treatment',
      'Permanent Filling',
      'ART',
      'Extraction',
      'Oral Prophylaxis',
      'Referral',
      'Other Oral Treatment',
      '',
      'Examined by'
])

const temporaryTeeth = ref([
      'No. T/decayed',
      'No. T/filled',
      'Total d. f. t.'
])

const permanentTeeth = ref([
      'No. T/decayed',
      'No. T/missing',
      'No. T/filled',
      'Total D. M. F. T.',
      'Total Sound Teeth'
])

// Student Info
const studentInfo = ref({})
const showStudentInfo = ref(false)
const studentOptionsShowing = ref(false)

const actionButton = ref(false)

async function listenToFilterChanges() {
      // Make request to backend, return data afterwards
      if (fileType.value == 'CURRENT' && curriculum.value != '' && gradeLvl.value != '' && section.value != '') {
            students.value = await retrieveStudentRecords(
                  fileType.value,
                  yearGraduated.value,
                  curriculum.value,
                  gradeLvl.value,
                  section.value
            )
      }
      else if (fileType.value == 'OLD' && yearGraduated.value != '' && curriculum.value != ''){
            students.value = await retrieveStudentRecords(
                  fileType.value,
                  yearGraduated.value,
                  curriculum.value,
                  gradeLvl.value,
                  section.value
            )
      }
}

async function retrieveStudentInfo(id) {
      studentInfo.value = await retrieveMedicalHistory(id)
      
      goodHealth.value = studentInfo.value.medicalHistory.good_health
      underMedicalTreatment.value = studentInfo.value.medicalHistory.under_medical_treatment
      treatmentCondition.value = studentInfo.value.medicalHistory.condition_being_treated
      seriousIllness.value = studentInfo.value.medicalHistory.serious_illness

      illnessOrOperation.value = studentInfo.value.medicalHistory.illness_or_operation
      hospitalized.value = studentInfo.value.medicalHistory.hospitalized
      hospitalizationDetails.value = studentInfo.value.medicalHistory.hospitalization_details
      takingMedications.value = studentInfo.value.medicalHistory.taking_medication
      medicationsDetails.value = studentInfo.value.medicalHistory.taking_medication
      tobaccoUsage.value = studentInfo.value.medicalHistory.use_tobacco
      drugUse.value = studentInfo.value.medicalHistory.use_alcohol_or_drugs
      womenOnly.value = studentInfo.value.medicalHistory.pregnant_nursing_birth_control
      womenCondition.value = studentInfo.value.medicalHistory.pregnant_nursing_birth_control_details
      hasToothbrush.value = studentInfo.value.medicalHistory.toothbrush
      brushingTimes.value = studentInfo.value.medicalHistory.brush_times_per_day
      toothbrushChange.value = studentInfo.value.medicalHistory.change_toothbrush_per_year
      useToothpaste.value = studentInfo.value.medicalHistory.use_toothpaste
      dentistVisits.value = studentInfo.value.medicalHistory.dentist_visits_per_year
}

watch([fileType, yearGraduated, curriculum, gradeLvl, section], () => {
      listenToFilterChanges();
});
</script>

<template>
      <div v-if="!showStudentInfo" class="flex flex-col h-11/12 w-11/12 gap-5 p-10 border-2 rounded-md">
            <div class="flex flex-row items-between justify-between">
                  <h4 v-if="fileType == 'CURRENT'">{{ fileType }} / {{ curriculum }} / {{ gradeLvl }} / {{ section }}</h4>
                  <h4 v-else-if="fileType == 'OLD'">{{ fileType }} / {{ yearGraduated }} / {{ curriculum }}</h4>
                  <h4 v-else></h4>

                  <div class="w-5/12">
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
                                          <option value="2025">2025</option>
                                          <option value="2026">2026</option>
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
                                    <th class="p-2">FIRST NAME</th>
                                    <th class="p-2">MIDDLE NAME</th>
                                    <th class="p-2">LAST NAME</th>
                                    <th class="p-2">BIRTHDATE</th>
                                    <th class="p-2">VIEW</th>
                              </tr>
                        </thead>

                        <!-- TODO -->
                        <tr v-for="student, index of students" :key="student">
                              <td class="text-center p-1">{{ student.firstname }}</td>
                              <td class="text-center p-1">{{ student.middlename }}</td>
                              <td class="text-center p-1">{{ student.lastname }}</td>
                              <td class="text-center p-1">{{ student.dateofbirth }}</td>
                              <td class="text-center p-1">
                                    <button 
                                          @click="() => { showStudentInfo = true; retrieveStudentInfo(student.id) }"
                                          class="hover:scale-150 transition duration-300 ease-in-out cursor-pointer"
                                    >
                                          <Eye />
                                    </button>
                              </td>
                        </tr>
                  </table>
            </div>
      </div>

      <div v-if="showStudentInfo" class="flex flex-col w-11/12 h-11/12 p-16 border-2 rounded-md overflow-y-scroll">
            <!-- Personal Info -->
            <div class="flex flex-row justify-between items-between w-full">
                  <div class="flex flex-row items-center w-3/12">
                        <div class="flex flex-col w-3/12">
                              <button @click="() => { studentOptionsShowing = !studentOptionsShowing }" class="flex items-center justify-center hover:scale-150 transition duration-300 ease-in-out cursor-pointer"><MenuSquare /></button>
      
                              <!-- Dropdown -->
                              <div v-if="studentOptionsShowing" class="flex flex-col gap-4 mt-10 rounded-md border-2 p-8 absolute bg-white">
                                    <button class="flex flex-row items-center gap-20 w-full p-4 hover:bg-black hover:text-white transition duration-300 ease-in-out rounded-md cursor-pointer" @click="changeButton('Edit')"><Edit /> EDIT</button>
                              </div>
                        </div>
                        <!-- TODO -->
                        <p class="text-2xl">{{ studentInfo.student.lastname }} {{ studentInfo.student.firstname }}</p>
                  </div>

                  <button @click="() => { showStudentInfo = false; studentOptionsShowing = false }" class="p-2 hover:text-white hover:bg-black rounded-md transition duration-300 ease-out cursor-pointer">Return to Student Records</button>
            </div>
            <hr class="mt-5 mb-20">

            <div class="flex flex-row justify-between w-full mb-20" @click="() => { studentOptionsShowing = false }">
                  <div class="flex flex-col gap-6 w-1/2">
                        <div class="flex flex-row gap-4">
                              <h4>NAME:</h4>
                              <p>{{ studentInfo.student.firstname }} {{ studentInfo.student.middlename }} {{ studentInfo.student.lastname }}</p>
                        </div>

                        <div class="flex flex-row gap-4">
                              <h4>DATE OF BIRTH:</h4>
                              <p>{{ studentInfo.student.dateofbirth }}</p>
                        </div>

                        <div class="flex flex-row gap-4">
                              <h4>BIRTHPLACE:</h4>
                              <p>{{ studentInfo.student.birthplace }}</p>
                        </div>

                        <div class="flex flex-row gap-4">
                              <h4>PARENT / GUARDIAN:</h4>
                              <p>{{ studentInfo.student.parent_guardian_name }}</p>
                        </div>

                        <div class="flex flex-row gap-4">
                              <h4>ADVISER:</h4>
                              <p>{{ studentInfo.student.adviser_name }}</p>
                        </div>
                  </div>

                  <div class="flex flex-col gap-6 w-1/2">
                        <div class="flex flex-row gap-4">
                              <h4>GENDER:</h4>
                              <p>{{ studentInfo.student.gender }}</p>
                        </div>

                        <div class="flex flex-row gap-4">
                              <h4>AGE:</h4>
                              <p>{{ studentInfo.student.age }}</p>
                        </div>

                        <div class="flex flex-row gap-4">
                              <h4>CONTACT NUMBER:</h4>
                              <p>{{ studentInfo.student.contact_no }}</p>
                        </div>

                        <div class="flex flex-row gap-4">
                              <h4>ADDRESS:</h4>
                              <p>{{ studentInfo.student.address }}</p>
                        </div>

                        <div class="flex flex-row gap-4">
                              <h4>CURRICULUM, GRADE LEVEL, SECTION:</h4>
                              <p>{{ studentInfo.student.curriculum }}, {{ studentInfo.student.grade_level }}, {{ studentInfo.student.section }}</p>
                        </div>
                  </div>
            </div>

            <!-- Medical Data -->
            <div class="flex flex-row justify-between w-full" @click="() => { studentOptionsShowing = false }">
                  <div class="flex flex-col gap-2 h-1/2 w-1/2">
                  <div class="flex flex-row gap-5">
                  <input type="checkbox" v-model="goodHealth">
                  <p>ARE YOU IN GOOD HEALTH?</p>
                  </div>
            
                  <div class="flex flex-col">
                  <div class="flex flex-row gap-5">
                        <input type="checkbox" v-model="underMedicalTreatment">
                        <p>ARE YOU UNDER MEDICAL TREATMENT NOW?</p>
                  </div>
            
                  <div class="flex flex-row gap-3 items-center w-3/4 justify-end">
                        <p>IF SO, WHAT IS THE CONDITION BEING TREATED?</p>
                        <input type="text" class="border-b-2 p-1" v-model="treatmentCondition">
                  </div>
                  </div>
            
                  <div class="flex flex-col">
                  <div class="flex flex-row gap-5">
                        <input type="checkbox" v-model="seriousIllness">
                        <p>HAVE YOU EVER HAD SERIOUS ILLNESS OR SURGICAL OPERATION?</p>
                  </div>
            
                  <div class="flex flex-row gap-3 items-center w-3/4 justify-end">
                        <p>IF SO, WHAT ILLNESS OR OPERATION?</p>
                        <input type="text" class="border-b-2 p-1" v-model="illnessOrOperation">
                  </div>
                  </div>
            
                  <div class="flex flex-col">
                  <div class="flex flex-row gap-5">
                        <input type="checkbox" v-model="hospitalized">
                        <p>HAVE YOU EVER BEEN HOSPITALIZED?</p>
                  </div>
            
                  <div class="flex flex-row gap-3 items-center w-3/4 justify-end">
                        <p>IF SO, WHEN AND WHY?</p>
                        <input type="text" class="border-b-2 p-1" v-model="hospitalizationDetails">
                  </div>
                  </div>
            
                  <div class="flex flex-col">
                  <div class="flex flex-row gap-5">
                        <input type="checkbox" v-model="takingMedications">
                        <p>ARE YOU TAKING ANY PRESCRIPTION/ NON-PRESCRIPTION MEDICATION?</p>
                  </div>
            
                  <div class="flex flex-row gap-3 items-center w-3/4 justify-end">
                        <p>IF YES, PLEASE SPECIFY:</p>
                        <input type="text" class="border-b-2 p-1" v-model="medicationsDetails">
                  </div>
                  </div>
            
                  <div class="flex flex-row gap-5">
                  <input type="checkbox" v-model="tobaccoUsage">
                  <p>DO YOU USE TOBACCO PRODUCTS?</p>
                  </div>
            
                  <div class="flex flex-row gap-5">
                  <input type="checkbox" v-model="drugUse">
                  <p>DO YOU USE ALCOHOL, COCAINE, OR OTHER DANGEROUS DRUGS?</p>
                  </div>
            
                  <div class="flex flex-col">
                  <div class="flex flex-row gap-5">
                        <input type="checkbox" v-model="womenOnly">
                        <p>FOR WOMEN ONLY: ARE YOU PREGNANT/ARE YOU NURSING/ARE YOU TAKING BIRTH CONTROL?</p>
                  </div>
            
                  <div class="flex flex-row gap-3 items-center w-3/4 justify-end">
                        <p>IF YES, PLEASE INDICATE:</p>
                        <input type="text" class="border-b-2 p-1" v-model="womenCondition">
                  </div>
                  </div>
                  </div>
            
                  <!-- Guided Questions -->
                  <div class="flex flex-col gap-4 h-1/2 w-1/2">
                        <h2 class="text-2xl mb-2">Guided Questions</h2>
                  
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="hasToothbrush">
                              <p>DO YOU HAVE A TOOTHBRUSH?</p>
                        </div>
                  
                        <div class="flex flex-row gap-4">
                              <input type="number" class="w-20 bg-gray-300 rounded-sm" v-model="brushingTimes">
                              <p>HOW MANY TIMES DO YOU BRUSH YOUR TEETH?</p>
                        </div>
                  
                        <div class="flex flex-row gap-4">
                              <input type="number" class="w-20 bg-gray-300 rounded-sm" v-model="toothbrushChange">
                              <p>HOW MANY TIMES DO YOU CHANGE YOUR TOOTHBRUSH IN A YEAR?</p>
                        </div>
                  
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="useToothpaste">
                              <p>DO YOU USE TOOTHPASTE IN BRUSHING?</p>
                        </div>
                  
                        <div class="flex flex-row gap-4">
                              <input type="number" class="w-20 bg-gray-300 rounded-sm" v-model="dentistVisits">
                              <p>HOW MANY TIMES DO YOU VISIT THE DENTIST IN A YEAR?</p>
                        </div>
                  </div>
            </div>

            <div class="w-full mt-10">
                  <!-- Top Dental -->
                  <div class="flex flex-row justify-between gap-5 h-auto mt-10 mb-20">
                        <div class="flex flex-col items-center justify-center w-8/12">
                              <h4 class="font-bold">DENTAL EXAMINATION</h4>
                              <table class="h-full border w-full">
                                    <tbody>
                                          <DentalExamLayerTypeA :layer-no="1" />
                                          <DentalExamLayerTypeA :layer-no="2" />

                                          <DentalExamLayerTypeC :layer-no="1" />
                                          <DentalExamLayerTypeB :layer-no="3" />
                                          <DentalExamLayerTypeB :layer-no="4" />
                                          <DentalExamLayerTypeC :layer-no="2" />

                                          <DentalExamLayerTypeA :layer-no="5" />
                                          <DentalExamLayerTypeA :layer-no="6" />
                                    </tbody>
                              </table>
                        </div>

                        <div class="flex flex-col items-center justify-center w-4/12">
                              <h4 class="font-bold">ORAL HEALTH CONDITION</h4>
                              <table class="border-2 w-full">
                                    <thead>
                                          <tr>
                                                <th class="p-2"></th>
                                                <th class="p-2"></th>
                                                <th class="p-2">1</th>
                                                <th class="p-2">2</th>
                                                <th class="p-2">3</th>
                                                <th class="p-2">4</th>
                                                <th class="p-2">5</th>
                                                <th class="p-2">6</th>
                                          </tr>
                                    </thead>

                                    <tbody>
                                          <tr v-for="condition of healthConditions" :key="condition">
                                                <td class="p-2">{{ condition }}</td>
                                                <td class="p-2"></td>
                                                <td class="p-2"></td>
                                                <td class="p-2"></td>
                                                <td class="p-2"></td>
                                                <td class="p-2"></td>
                                                <td class="p-2"></td>
                                                <td class="p-2"></td>
                                          </tr>
                                    </tbody>
                              </table>
                        </div>
                  </div>

                  <!-- Middle Half Dental -->
                  <div class="flex flex-row justify-between gap-5 h-11/12 mt-10">
                        <div class="flex flex-col items-center justify-center w-7/12 h-full">
                              <h4 class="font-bold">DENTAL PROCEDURES</h4>
                              <table class="border-2 w-full h-full">
                                    <thead>
                                          <tr>
                                                <th class="p-2"></th>
                                                <th class="p-2">Pre-Schooler</th>
                                                <th class="p-2">1</th>
                                                <th class="p-2">2</th>
                                                <th class="p-2">3</th>
                                                <th class="p-2">4</th>
                                                <th class="p-2">5</th>
                                                <th class="p-2">6</th>
                                                <th class="p-2">Remarks</th>
                                          </tr>
                                    </thead>

                                    <tbody>
                                          <tr v-for="procedure of dentalProcedures" :key="procedure">
                                                <td class="p-2">{{ procedure }}</td>
                                                <td class="p-2"></td>
                                                <td class="p-2"></td>
                                                <td class="p-2"></td>
                                                <td class="p-2"></td>
                                                <td class="p-2"></td>
                                                <td class="p-2"></td>
                                                <td class="p-2"></td>
                                                <td class="p-2"></td>
                                          </tr>
                                    </tbody>
                              </table>
                        </div>

                        <div class="flex flex-col gap-5 w-5/12 h-full">
                              <div class="flex flex-col w-full h-1/2">
                                    <h4 class="font-bold">TEMPORARY TEETH</h4>
                                    <table class="border-2 w-full h-full">
                                          <thead>
                                                <tr>
                                                      <th class="p-2">Index d. f. t.</th>
                                                      <th class="p-2">Pre-Schooler</th>
                                                      <th class="p-2">1</th>
                                                      <th class="p-2">2</th>
                                                      <th class="p-2">3</th>
                                                      <th class="p-2">4</th>
                                                      <th class="p-2">5</th>
                                                      <th class="p-2">6</th>
                                                </tr>
                                          </thead>

                                          <tbody>
                                                <tr v-for="temporaryTooth of temporaryTeeth" :key="temporaryTooth">
                                                      <td class="p-2">{{ temporaryTooth }}</td>
                                                      <td class="p-2"></td>
                                                      <td class="p-2"></td>
                                                      <td class="p-2"></td>
                                                      <td class="p-2"></td>
                                                      <td class="p-2"></td>
                                                      <td class="p-2"></td>
                                                </tr>
                                          </tbody>
                                    </table>
                              </div>

                              <div class="flex flex-col w-full h-1/2">
                                    <h4 class="font-bold">PERMANENT TEETH</h4>
                                    <table class="border-2 w-full h-full">
                                          <thead>
                                                <tr>
                                                      <th class="p-2">Index D. M. F. T.</th>
                                                      <th class="p-2"></th>
                                                      <th class="p-2">7</th>
                                                      <th class="p-2">8</th>
                                                      <th class="p-2">9</th>
                                                      <th class="p-2">10</th>
                                                      <th class="p-2">11</th>
                                                      <th class="p-2">12</th>
                                                </tr>
                                          </thead>

                                          <tbody>
                                                <tr v-for="permanentTooth of permanentTeeth" :key="permanentTooth">
                                                      <td class="p-2">{{ permanentTooth }}</td>
                                                      <td class="p-2"></td>
                                                      <td class="p-2"></td>
                                                      <td class="p-2"></td>
                                                      <td class="p-2"></td>
                                                      <td class="p-2"></td>
                                                      <td class="p-2"></td>
                                                      <td class="p-2"></td>
                                                </tr>
                                          </tbody>
                                    </table>
                              </div>
                        </div>
                  </div>

                  <!-- Bottom Dental -->
                   <div>
                        <div></div>
                        <div></div>
                   </div>
            </div>
            
            <div class="flex flex-row justify-end mt-3">
                  <!-- TODO, Add functionality here -->
                  <button v-if="actionButton == 'Edit'" class="border-2 p-2 text-center w-3/12 rounded-sm">Save Changes</button>
            </div>
      </div>
</template>

<style scoped>
table, th, td {
      border: 1px solid black;
      border-collapse: collapse;
}
</style>

<script setup>
import { ref, watch } from 'vue';
import { Eye, MenuSquare, Edit, Printer } from 'lucide-vue-next';
import { retrieveStudentRecords } from '@/services/StudentRecordService';
import { retrieveMedicalHistory, updateMedicalHistory } from '@/services/MedicalHistoryService';

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
const studentID = ref(0);



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
      medicationsDetails.value = studentInfo.value.medicalHistory.medication_details
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


async function updateMedicalHistoryFunc(id) {
  const medicalHistoryInfo = {
      studentID: id,
      goodHealth: goodHealth.value,
      underMedicalTreatment: underMedicalTreatment.value,
      treatmentCondition: treatmentCondition.value,
      seriousIllness: seriousIllness.value,
      illnessOrOperation: illnessOrOperation.value,
      hospitalized: hospitalized.value,
      hospitalizationDetails: hospitalizationDetails.value,
      takingMedications: takingMedications.value,
      medicationsDetails: medicationsDetails.value,
      tobaccoUsage: tobaccoUsage.value,
      drugUse: drugUse.value,
      womenOnly: womenOnly.value,
      womenCondition: womenCondition.value,
      hasToothbrush: hasToothbrush.value,
      brushingTimes: brushingTimes.value,
      toothbrushChange: toothbrushChange.value,
      useToothpaste: useToothpaste.value,
      dentistVisits: dentistVisits.value,
  };

  let updateResult = await updateMedicalHistory(medicalHistoryInfo);

  if (updateResult) {
      studentOptionsShowing.value = false;
  actionButton.value = false;
  }
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
                  <div class="flex w-full items-center justify-center mt-10 mb-5"><h1 class="text-3xl">STUDENT LIST (STUDENT RECORDS)</h1></div>
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
                              <td class="text-center p-1">{{ student.firstname }}</td>
                              <td class="text-center p-1">{{ student.middlename }}</td>
                              <td class="text-center p-1">{{ student.lastname }}</td>
                              <td class="text-center p-1">{{ student.dateofbirth }}</td>
                              <td class="text-center p-1"><button @click="() => { showStudentInfo = true; retrieveStudentInfo(student.id) }"><Eye /></button></td>
                        </tr>
                  </table>
            </div>
      </div>

      <div v-if="showStudentInfo" class="flex flex-col w-11/12 h-11/12 p-16 border-2 rounded-md overflow-y-scroll">
            <!-- Personal Info -->
            <div class="flex flex-row justify-between items-between w-full">
                  <div class="flex flex-row w-3/12">
                        <div class="flex flex-col w-3/12">
                              <button @click="() => { studentOptionsShowing = !studentOptionsShowing }"><MenuSquare /></button>
      
                              <!-- Dropdown -->
                              <div v-if="studentOptionsShowing" class="flex flex-col gap-4 mt-10 rounded-md border-2 p-8 w-60 absolute bg-white">
                                    <button class="flex flex-row items-center gap-20 w-full" @click="() => { actionButton = 'Edit'; studentOptionsShowing = false; }"><Edit /> EDIT</button>
                                    <button class="flex flex-row items-center gap-20 w-full" @click="() => { actionButton = 'Print'; studentOptionsShowing = false; }"><Printer /> PRINT</button>
                              </div>
                        </div>
                        <!-- TODO -->
                        <p class="text-2xl">{{ studentInfo.student.lastname }}, {{ studentInfo.student.firstname }}</p>      
                  </div>

                  <button @click="() => { showStudentInfo = false; }">Return to Student Records</button>
            </div>
            <hr class="mt-5 mb-20">

            <div class="flex flex-row justify-between w-full mb-20" @click="() => { studentOptionsShowing = false; }">
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
            
            <div class="flex flex-row justify-end mt-3 gap-4" v-if="actionButton == 'Edit'">
                  <!-- TODO, Add functionality here -->
                  
                  <button class="border-2 p-2 text-center w-1/12 rounded-sm" @click="updateMedicalHistoryFunc(studentInfo.student.id)">Save Changes</button>
                  <button class="border-2 p-2 text-center w-1/12 rounded-sm" @click="() => { actionButton = '' }">Cancel</button>
            </div>

            <div class="flex flex-row justify-end mt-3 gap-4" v-if="actionButton == 'Print'">
                  <!-- TODO, Add functionality here -->
                  
                  <button class="border-2 p-2 text-center w-1/12 rounded-sm" @click="updateMedicalHistoryFunc(studentInfo.student.id)">PRINT</button>
                  <button class="border-2 p-2 text-center w-1/12 rounded-sm" @click="() => { actionButton = '' }">Cancel</button>
            </div>
      </div>
</template>

<style scoped>

</style>
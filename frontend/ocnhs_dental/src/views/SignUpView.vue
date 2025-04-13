<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter()

const firstName = ref('');
const middleName = ref('');
const lastName = ref('');
const suffix = ref('');

const birthDate = ref('');
const gender = ref('');
const placeOfBirth = ref('');

const contact = ref('');
const address = ref('');
const email = ref('');

const password = ref('');
const confirmPassword = ref('');

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
const allergy = ref(false);
const emphysema = ref(false);
const bleedingProblems = ref(false);
const bloodDiseases = ref(false);
const headInjuries = ref(false);
const arthritis = ref(false);
const highFever = ref(false);
const diabetes = ref(false);
const chestPain = ref(false);
const stroke = ref(false);
const cancer = ref(false);
const anemia = ref(false);
const angina = ref(false);
const asthma = ref(false);
const highBloodPressure = ref(false);
const lowBloodPressure = ref(false);
const aidsHiv = ref(false);
const std = ref(false);
const stomachTroubles = ref(false);
const faintingSeizure = ref(false);
const rapidWeightLoss = ref(false);
const radiationTherapy = ref(false);
const jointReplacement = ref(false);
const heartSurgery = ref(false);
const thyroidProblem = ref(false);
const heartDisease = ref(false);
const heartMurmur = ref(false);
const hepatitisLiverDisease = ref(false);
const rheumaticSeizure = ref(false);
const respiratoryProblems = ref(false);
const hepatitisJaundice = ref(false);
const tuberculosis = ref(false);
const swollenAnkles = ref(false);
const kidneyDisease = ref(false);
const others = ref('');


</script>

<template>
<div id="container" class="flex items-center justify-center absolute top-0 left-0 w-full h-full">
      <div class="flex flex-col h-11/12 w-11/12 gap-5 p-10 border-2 rounded-md overflow-y-scroll">
            <h1 class="text-4xl font-bold mb-5">OCNHS DENTAL CLINIC SIGN IN FORM</h1>

            <!-- Student Info -->
            <div class="flex flex-row justify-between w-full">
                  <div class="w-1/2 flex flex-col gap-6">
                        <div class="flex flex-row items-center w-full gap-4">
                              <h4>NAME:</h4>
                              <input type="text" class="border-2 rounded-md p-1" placeholder="First Name">
                              <input type="text" class="border-2 rounded-md p-1" placeholder="Middle Name">
                              <input type="text" class="border-2 rounded-md p-1" placeholder="Last Name">
                              <input type="text" class="border-2 rounded-md p-1" placeholder="Suffix">
                        </div>

                        <div class="flex flex-row items-center w-full gap-2">
                              <h4>DATE OF BIRTH:</h4>
                              <input type="date" class="border-2 rounded-md p-1">

                              <h4>BIRTHPLACE:</h4>
                              <input type="text" class="border-2 rounded-md p-1 w-6/12">
                        </div>

                        <div class="flex flex-row items-center w-full gap-2">
                              <h4>PARENT / GUARDIAN:</h4>
                              <input type="text" class="border-2 rounded-md p-1 w-4/12">

                              <h4>ADVISER:</h4>
                              <input type="text" class="border-2 rounded-md p-1 w-4/12">
                        </div>

                        <div class="flex flex-row items-center w-full gap-2">
                              <h4>GENDER:</h4>
                              <select class="border-2">
                                    <option value="MALE">MALE</option>
                                    <option value="FEMALE">FEMALE</option>
                              </select>

                              <h4>AGE:</h4>
                              <input type="text" class="border-2 rounded-md p-1">
                        </div>
                  </div>

                  <div class="w-1/2 flex flex-col gap-6">
                        <div class="flex flex-row items-center w-full gap-4">
                              <h4>ADDRESS:</h4>
                              <input type="email" class="border-2 rounded-md p-1 w-full">
                        </div>

                        <div class="flex flex-row items-center w-full gap-4">
                              <h4>CONTACT NUMBER:</h4>
                              <input type="text" class="border-2 rounded-md p-1 w-4/12">

                              <h4>EMAIL:</h4>
                              <input type="email" class="border-2 rounded-md p-1 w-5/12">
                        </div>

                        <div class="flex flex-row items-center w-full gap-2">
                              <h4>PASSWORD:</h4>
                              <input type="email" class="border-2 rounded-md p-1">

                              <h4>CONFIRM PASSWORD:</h4>
                              <input type="email" class="border-2 rounded-md p-1">
                        </div>

                        <div class="flex flex-row gap-4">
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

                              <h4>GRADE LEVEL</h4>
                              <select class="border-2" v-model="gradeLvl">
                                    <option value="GRADE 7">GRADE 7</option>
                                    <option value="GRADE 8">GRADE 8</option>
                                    <option value="GRADE 9">GRADE 9</option>
                                    <option value="GRADE 10">GRADE 10</option>
                                    <option value="GRADE 11">GRADE 11</option>
                                    <option value="GRADE 12">GRADE 12</option>
                              </select>

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
            
            <!-- Medical Info -->
            <div class="flex flex-row justify-between w-full">
                  <div class="flex flex-col gap-1 h-1/2 w-1/2">
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
                  <div class="flex flex-col gap-2 h-1/2 w-1/2">
                  <h2 class="text-2xl mb-2">Guided Questions</h2>
            
                  <div class="flex flex-row gap-4">
                  <input type="checkbox" v-model="hasToothbrush">
                  <p>DO YOU HAVE A TOOTHBRUSH?</p>
                  </div>
            
                  <div class="flex flex-row gap-4">
                  <input type="number" class="w-14 bg-gray-300 rounded-sm text-center" v-model="brushingTimes">
                  <p>HOW MANY TIMES DO YOU BRUSH YOUR TEETH?</p>
                  </div>
            
                  <div class="flex flex-row gap-4">
                  <input type="number" class="w-14 bg-gray-300 rounded-sm text-center" v-model="toothbrushChange">
                  <p>HOW MANY TIMES DO YOU CHANGE YOUR TOOTHBRUSH IN A YEAR?</p>
                  </div>
            
                  <div class="flex flex-row gap-4">
                  <input type="checkbox" v-model="useToothpaste">
                  <p>DO YOU USE TOOTHPASTE IN BRUSHING?</p>
                  </div>
            
                  <div class="flex flex-row gap-4">
                  <input type="number" class="w-14 bg-gray-300 rounded-sm text-center" v-model="dentistVisits">
                  <p>HOW MANY TIMES DO YOU VISIT THE DENTIST IN A YEAR?</p>
                  </div>
                  </div>
            </div>            
            
                  <p class="mt-8">DO YOU HAVE OR HAVE YOU HAD ANY OF THE FOLLOWING? CHECK WHICH APPLY:</p>
            
                  <div class="flex flex-row justify-between w-full">
                  <div class="flex flex-col gap-1">
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="allergy">
                              <p>ALLERGY</p>
                        </div>
                  
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="emphysema">
                              <p>EMPHYSEMA</p>
                        </div>
                  
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="bleedingProblems">
                              <p>BLEEDING PROBLEMS</p>
                        </div>
                  
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="bloodDiseases">
                              <p>BLOOD DISEASES</p>
                        </div>
                  
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="headInjuries">
                              <p>HEAD INJURIES</p>
                        </div>
                  
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="arthritis">
                              <p>ARTHRITIS/RHEUMATISM</p>
                        </div>
                  
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="highFever">
                              <p>HIGH FEVER</p>
                        </div>
                  
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="diabetes">
                              <p>DIABETES</p>
                        </div>                                  
                  </div>
            
                  <div class="flex flex-col gap-1">
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="chestPain">
                              <p>CHEST PAIN</p>
                        </div>
                  
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="stroke">
                              <p>STROKE</p>
                        </div>
                  
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="cancer">
                              <p>CANCER/TUMORS</p>
                        </div>
                  
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="anemia">
                              <p>ANEMIA</p>
                        </div>
                  
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="angina">
                              <p>ANGINA</p>
                        </div>
                  
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="asthma">
                              <p>ASTHMA</p>
                        </div>
                  
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="highBloodPressure">
                              <p>HIGH BLOOD PRESSURE</p>
                        </div>
                  
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="lowBloodPressure">
                              <p>LOW BLOOD PRESSURE</p>
                        </div>
                  
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="aidsHiv">
                              <p>AIDS OR HIV INFECTION</p>
                        </div>
                  
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="std">
                              <p>SEXUALLY TRANSMITTED DISEASE</p>
                        </div>                            
                  </div>
            
                  <div class="flex flex-col gap-1">
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="stomachTroubles" />
                              <p>STOMACH TROUBLES/ULCERS</p>
                        </div>
                        
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="faintingSeizure" />
                              <p>FAINTING SEIZURE</p>
                        </div>
                        
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="rapidWeightLoss" />
                              <p>RAPID WEIGHT LOSS</p>
                        </div>
                        
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="radiationTherapy" />
                              <p>RADIATION THERAPY</p>
                        </div>
                        
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="jointReplacement" />
                              <p>JOINT REPLACEMENT/ IMPLANT</p>
                        </div>
                        
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="heartSurgery" />
                              <p>HEART SURGERY/HEART ATTACK</p>
                        </div>
                        
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="thyroidProblem" />
                              <p>THYROID PROBLEM</p>
                        </div>
                        
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="heartDisease" />
                              <p>HEART DISEASE</p>
                        </div>
                        
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="heartMurmur" />
                              <p>HEART MURMUR</p>
                        </div>
                        
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="hepatitisLiverDisease" />
                              <p>HEPATITIS/ LIVER DISEASE</p>
                        </div>
                  </div>
      
                  <div class="flex flex-col gap-1">
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="rheumaticSeizure" />
                              <p>RHEUMATIC SEIZURE</p>
                        </div>
                        
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="respiratoryProblems" />
                              <p>RESPIRATORY PROBLEMS</p>
                        </div>
                        
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="hepatitisJaundice" />
                              <p>HEPATITIS/ JAUNDICE</p>
                        </div>
                        
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="tuberculosis" />
                              <p>TUBERCULOSIS</p>
                        </div>
                        
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="swollenAnkles" />
                              <p>SWOLLEN ANKLES</p>
                        </div>
                        
                        <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="kidneyDisease" />
                              <p>KIDNEY DISEASE</p>
                        </div>
            
                        <div class="flex flex-row items-center gap-4">
                              <p>OTHERS:</p>
                              <input type="text" v-model="others" class="border-b-2 p-1" />
                        </div>
                  </div>
            </div>

            <div class="w-full flex justify-end mt-5 gap-2">
                  <button class="bg-green-500 rounded-md p-2 w-1/12 text-white cursor-pointer">Register</button>
                  <button class="bg-red-500 rounded-md p-2 w-1/12 text-white cursor-pointer" @click="() => { router.push('/') }">Cancel</button>
            </div>
      </div>
</div>
</template>
    
<style scoped>
#container {
      font-size: 11pt;
}
</style>
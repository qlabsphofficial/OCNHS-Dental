<script setup>
import { ref, watch } from 'vue';
import { register } from '@/services/RegisterService';
import { useRouter } from 'vue-router';

const router = useRouter()

const firstName = ref('');
const middleName = ref('');
const lastName = ref('');
const suffix = ref('');

const birthDate = ref('');
const gender = ref('');
const age = ref('');

const placeOfBirth = ref('');
const contact = ref('');
const address = ref('');
const email = ref('');
const password = ref('');
const confirmPassword = ref('');

const parentName = ref('');
const adviserName = ref('');

const curriculum = ref('');
const gradeLvl = ref('');
const section = ref('');

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
const rapidWeightLossRadtionTherapy = ref(false);
// const radiationTherapy = ref(false);
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

watch(birthDate, (newBirthDate) => {
  if (newBirthDate) {
    const today = new Date();
    const birth = new Date(newBirthDate);
    let calculatedAge = today.getFullYear() - birth.getFullYear();
    const m = today.getMonth() - birth.getMonth();
    if (m < 0 || (m === 0 && today.getDate() < birth.getDate())) {
      calculatedAge--;
    }
    age.value = calculatedAge;
  } else {
    age.value = '';
  }
});

async function attemptRegister() {
  const registerInfo = {
      firstName: firstName.value,
      middleName: middleName.value,
      lastName: lastName.value,
      suffix: suffix.value,
      birthDate: birthDate.value,
      gender: gender.value,
      age: age.value,
      placeOfBirth: placeOfBirth.value,
      contact: contact.value,
      address: address.value,
      email: email.value,
      password: password.value,
      confirmPassword: confirmPassword.value,
      address: address.value,
      parentName: parentName.value,
      adviserName: adviserName.value,
      curriculum: curriculum.value,
      gradeLvl: gradeLvl.value,
      section: section.value,
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
      allergy: allergy.value,
      //need to add allergy details
      emphysema: emphysema.value,
      bleedingProblems: bleedingProblems.value,
      bloodDiseases: bloodDiseases.value,
      headInjuries: headInjuries.value,
      arthritis: arthritis.value,
      highFever: highFever.value,
      diabetes: diabetes.value,
      chestPain: chestPain.value,
      stroke: stroke.value,
      cancer: cancer.value,
      anemia: anemia.value,
      angina: angina.value,
      asthma: asthma.value,
      highBloodPressure: highBloodPressure.value,
      lowBloodPressure: lowBloodPressure.value,
      aidsHiv: aidsHiv.value,
      std: std.value,
      stomachTroubles: stomachTroubles.value,
      faintingSeizure: faintingSeizure.value,
      rapidWeightLossRadtionTherapy: rapidWeightLossRadtionTherapy.value,
      // radiationTherapy: radiationTherapy.value,
      jointReplacement: jointReplacement.value,
      heartSurgery: heartSurgery.value,
      thyroidProblem: thyroidProblem.value,
      heartDisease: heartDisease.value,
      heartMurmur: heartMurmur.value,
      hepatitisLiverDisease: hepatitisLiverDisease.value,
      rheumaticSeizure: rheumaticSeizure.value,
      respiratoryProblems: respiratoryProblems.value,
      hepatitisJaundice: hepatitisJaundice.value,
      tuberculosis: tuberculosis.value,
      swollenAnkles: swollenAnkles.value,
      kidneyDisease: kidneyDisease.value,
      others: others.value
  };

  let registerResult = await register(registerInfo);

  if (registerResult) {
    router.push('/login');
  }
}


</script>

<template>
<div id="container" class="flex items-center justify-center absolute top-0 left-0 w-full h-full">
      <div class="flex flex-col w-full h-full lg:h-11/12 lg:w-11/12 gap-5 p-10 lg:border-2 rounded-md overflow-y-scroll">
            <h1 class="text-4xl font-bold mb-5">OCNHS DENTAL CLINIC SIGN IN FORM</h1>

            <!-- Student Info -->
            <div class="flex flex-col lg:flex-row justify-between w-full">
                  <div class="w-full lg:w-5/12 flex flex-col gap-6">
                        <div class="flex flex-col w-full gap-4">
                              <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
                                    <h4>FIRST NAME:</h4>
                                    <input type="text" class="border-2 rounded-md p-1 w-3/4" placeholder="First Name" v-model="firstName">
                              </div>

                              <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
                                    <h4>MIDDLE NAME:</h4>
                                    <input type="text" class="border-2 rounded-md p-1 w-3/4" placeholder="Middle Name" v-model="middleName">
                              </div>

                              <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
                                    <h4>LAST NAME:</h4>
                                    <input type="text" class="border-2 rounded-md p-1 w-3/4" placeholder="Last Name" v-model="lastName">
                              </div>

                              <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
                                    <h4>SUFFIX:</h4>
                                    <input type="text" class="border-2 rounded-md p-1 w-3/4" placeholder="Suffix" v-model="suffix">
                              </div>
                        </div>

                        <div class="flex flex-col lg:flex-row lg:items-center w-full gap-2">
                              <h4>DATE OF BIRTH:</h4>
                              <input type="date" class="border-2 rounded-md p-1" v-model="birthDate">

                              <h4>BIRTHPLACE:</h4>
                              <input type="text" class="border-2 rounded-md p-1 w-full lg:w-6/12" v-model="placeOfBirth">
                        </div>

                        <div class="flex flex-col lg:flex-row lg:items-center w-full gap-2">
                              <h4>PARENT / GUARDIAN:</h4>
                              <input type="text" class="border-2 rounded-md p-1 w-full lg:w-4/12" v-model="parentName">

                              <h4>ADVISER:</h4>
                              <input type="text" class="border-2 rounded-md p-1 w-full lg:w-4/12" v-model="adviserName">
                        </div>

                        <div class="flex flex-col lg:flex-row lg:items-center w-full gap-2">
                              <h4>GENDER:</h4>
                              <select class="border-2 w-full lg:w-auto" v-model="gender">
                                    <option value="MALE">MALE</option>
                                    <option value="FEMALE">FEMALE</option>
                              </select>
                              
                              <h4>AGE:</h4>
                              <input type="text" class="border-2 rounded-md p-1" v-model="age">
                        </div>
                  </div>
                  
                  <div class="w-full lg:w-1/2 flex flex-col gap-6 mt-10 lg:mt-0">
                        <div class="flex flex-col lg:flex-row lg:items-center w-full gap-4">
                              <h4>ADDRESS:</h4>
                              <input type="email" class="border-2 rounded-md p-1 w-3/4" v-model="address">
                        </div>

                        <div class="flex flex-col lg:flex-row lg:items-center w-full gap-4">
                              <h4>CONTACT NUMBER:</h4>
                              <input type="text" class="border-2 rounded-md p-1 w-full lg:w-4/12" v-model="contact">
                              
                              <h4>EMAIL:</h4>
                              <input type="email" class="border-2 rounded-md p-1 w-full lg:w-5/12" v-model="email">
                        </div>

                        <div class="flex flex-col lg:flex-row lg:items-center w-full gap-2">
                              <h4>PASSWORD:</h4>
                              <input type="password" class="border-2 rounded-md p-1" v-model="password">

                              <h4>CONFIRM PASSWORD:</h4>
                              <input type="password" class="border-2 rounded-md p-1" v-model="confirmPassword">
                        </div>

                        <div class="flex flex-col lg:flex-row gap-4">
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
            <div class="flex flex-col lg:flex-row justify-between w-full">
                  <div class="flex flex-col gap-1 lg:h-1/2 lg:w-1/2">
                  <div class="flex flex-row gap-5">
                        <input type="checkbox" v-model="goodHealth">
                        <p>ARE YOU IN GOOD HEALTH?</p>
                  </div>
            
                  <div class="flex flex-col">
                        <div class="flex flex-row gap-5">
                              <input type="checkbox" v-model="underMedicalTreatment">
                              <p>ARE YOU UNDER MEDICAL TREATMENT NOW?</p>
                        </div>
                  
                        <div class="flex flex-col lg:flex-row gap-3 items-center w-full lg:w-3/4 justify-end mt-4 lg:mt-0">
                              <p>IF SO, WHAT IS THE CONDITION BEING TREATED?</p>
                              <input type="text" class="w-full lg:w-auto border-b-2 p-1" v-model="treatmentCondition" :disabled="!underMedicalTreatment">
                        </div>
                  </div>
            
                  <div class="flex flex-col">
                  <div class="flex flex-row gap-5">
                        <input type="checkbox" v-model="seriousIllness">
                        <p>HAVE YOU EVER HAD SERIOUS ILLNESS OR SURGICAL OPERATION?</p>
                  </div>
            
                  <div class="flex flex-col lg:flex-row gap-3 items-center w-full lg:w-3/4 justify-end mt-4 lg:mt-0">
                        <p>IF SO, WHAT ILLNESS OR OPERATION?</p>
                        <input type="text" class="w-full lg:w-auto border-b-2 p-1" v-model="illnessOrOperation" :disabled="!seriousIllness">
                  </div>
                  </div>
            
                  <div class="flex flex-col">
                  <div class="flex flex-row gap-5">
                        <input type="checkbox" v-model="hospitalized">
                        <p>HAVE YOU EVER BEEN HOSPITALIZED?</p>
                  </div>
            
                  <div class="flex flex-col lg:flex-row gap-3 items-center w-full lg:w-3/4 justify-end mt-4 lg:mt-0">
                        <p>IF SO, WHEN AND WHY?</p>
                        <input type="text" class="w-full lg:w-auto border-b-2 p-1" v-model="hospitalizationDetails" :disabled="!hospitalized">
                  </div>
                  </div>
            
                  <div class="flex flex-col">
                  <div class="flex flex-row gap-5">
                        <input type="checkbox" v-model="takingMedications">
                        <p>ARE YOU TAKING ANY PRESCRIPTION/ NON-PRESCRIPTION MEDICATION?</p>
                  </div>
            
                  <div class="flex flex-col lg:flex-row gap-3 items-center w-full lg:w-3/4 justify-end mt-4 lg:mt-0">
                        <p>IF YES, PLEASE SPECIFY:</p>
                        <input type="text" class="w-full lg:w-auto border-b-2 p-1" v-model="medicationsDetails" :disabled="!takingMedications">
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
            
                  <div class="flex flex-col lg:flex-row gap-3 items-center w-full lg:w-3/4 justify-end mt-4 lg:mt-0">
                        <p>IF YES, PLEASE INDICATE:</p>
                        <input type="text" class="w-full lg:w-auto border-b-2 p-1" v-model="womenCondition" :disabled="!womenOnly">
                  </div>
                  </div>
                  </div>
            
                  <!-- Guided Questions -->
                  <div class="flex flex-col gap-2 lg:h-1/2 lg:w-1/2 mt-10 mb-10 lg:mt-0 lg:mb-0">
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
            
                  <div class="flex flex-col lg:flex-row justify-between w-full">
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
                              <input type="checkbox" v-model="rapidWeightLossRadtionTherapy" />
                              <p>RAPID WEIGHT LOSS RADIATION THERAPY</p>
                        </div>
                        
                        <!-- <div class="flex flex-row gap-4">
                              <input type="checkbox" v-model="radiationTherapy" />
                              <p>RADIATION THERAPY</p>
                        </div> -->
                        
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

            <div class="w-full flex flex-row items-center justify-center lg:justify-end mt-5 gap-2">
                  <button class="cursor-pointer bg-green-500 hover:bg-transparent hover:border-green-500 hover:text-green-500 border transition duration-300 ease-in-out rounded-md p-2 w-4/12 lg:w-1/12 text-white cursor-pointer" @click="attemptRegister()">Register</button>
                  <button class="cursor-pointer bg-red-500 hover:bg-transparent hover:border-red-500 hover:text-red-500 border transition duration-300 ease-in-out rounded-md p-2 w-4/12 lg:w-1/12 text-white cursor-pointer" @click="() => { router.push('/') }">Cancel</button>
            </div>
      </div>
</div>
</template>
    
<style scoped>
#container {
      font-size: 14pt;
}
</style>
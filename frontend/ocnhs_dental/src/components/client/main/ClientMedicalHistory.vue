<script setup>
import { ref } from 'vue';

const medical_history = JSON.parse(sessionStorage.getItem('medical_history'))

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

goodHealth.value = medical_history.good_health
underMedicalTreatment.value = medical_history.under_medical_treatment
treatmentCondition.value = medical_history.condition_being_treated
seriousIllness.value = medical_history.serious_illness
illnessOrOperation.value = medical_history.illness_or_operation
hospitalized.value = medical_history.hospitalized
hospitalizationDetails.value = medical_history.hospitalization_details
takingMedications.value = medical_history.taking_medication
medicationsDetails.value = medical_history.medication_details
tobaccoUsage.value = medical_history.use_tobacco
drugUse.value = medical_history.use_alcohol_or_drugs
womenOnly.value = medical_history.pregnant_nursing_birth_control
womenCondition.value = medical_history.pregnant_nursing_birth_control_details
hasToothbrush.value = medical_history.toothbrush
brushingTimes.value = medical_history.brush_times_per_day
toothbrushChange.value = medical_history.change_toothbrush_per_year
useToothpaste.value = medical_history.use_toothpaste
dentistVisits.value = medical_history.dentist_visits_per_year
allergy.value = medical_history.allergy
emphysema.value = medical_history.emphysema
bleedingProblems.value = medical_history.bleeding_problems
bloodDiseases.value = medical_history.blood_diseases
headInjuries.value = medical_history.head_injuries
arthritis.value = medical_history.arthritis_rheumatism
highFever.value = medical_history.high_fever
diabetes.value = medical_history.diabetes
chestPain.value = medical_history.chest_pain
stroke.value = medical_history.stroke
cancer.value = medical_history.cancer_tumors
anemia.value = medical_history.anemia
angina.value = medical_history.angina
asthma.value = medical_history.asthma
highBloodPressure.value = medical_history.high_blood_pressure
lowBloodPressure.value = medical_history.low_blood_pressure
aidsHiv.value = medical_history.aids_hiv_infection
std.value = medical_history.sexually_transmitted_disease
stomachTroubles.value = medical_history.stomach_troubles_ulcers
faintingSeizure.value = medical_history.fainting_seizure
rapidWeightLoss.value = medical_history.rapid_weight_loss_radiation_therapy
jointReplacement.value = medical_history.joint_replacement_implant
heartSurgery.value = medical_history.heart_surgery_heart_attack
thyroidProblem.value = medical_history.thyroid_problem
heartDisease.value = medical_history.heart_disease
heartMurmur.value = medical_history.heart_murmur
hepatitisLiverDisease.value = medical_history.hepatitis_liver_disease
rheumaticSeizure.value = medical_history.rheumatic_seizure
respiratoryProblems.value = medical_history.respiratory_problems
hepatitisJaundice.value = medical_history.hepatitis_jaundice
tuberculosis.value = medical_history.tuberculosis
swollenAnkles.value = medical_history.swollen_ankles
kidneyDisease.value = medical_history.kidney_disease
others.value = medical_history.other_diseases

</script>

<template>
  <div class="flex flex-col w-full h-full lg:h-11/12 lg:w-11/12 gap-5 p-10 lg:border-2 rounded-md overflow-y-scroll">
    <h1 class="text-4xl mb-5 font-bold">MEDICAL HISTORY</h1>
  
    <div class="flex flex-col lg:flex-row justify-between w-full">
      <div class="flex flex-col gap-2 h-1/2 lg:w-1/2">
        <div class="flex flex-row gap-5">
          <input type="checkbox" v-model="goodHealth">
          <p>ARE YOU IN GOOD HEALTH?</p>
        </div>
  
        <div class="flex flex-col mt-2 lg:mt-0">
          <div class="flex flex-row gap-5">
            <input type="checkbox" v-model="underMedicalTreatment">
            <p>ARE YOU UNDER MEDICAL TREATMENT NOW?</p>
          </div>
  
          <div class="flex flex-col lg:flex-row gap-3 items-center lg:w-3/4 justify-end mt-4">
            <p>IF SO, WHAT IS THE CONDITION BEING TREATED?</p>
            <input type="text" class="w-full lg:w-auto border-b-2 p-1" v-model="treatmentCondition">
          </div>
        </div>
  
        <div class="flex flex-col">
          <div class="flex flex-row gap-5">
            <input type="checkbox" v-model="seriousIllness">
            <p>HAVE YOU EVER HAD SERIOUS ILLNESS OR SURGICAL OPERATION?</p>
          </div>
  
          <div class="flex flex-col lg:flex-row gap-3 items-center lg:w-3/4 justify-end mt-4">
            <p>IF SO, WHAT ILLNESS OR OPERATION?</p>
            <input type="text" class="w-full lg:w-auto border-b-2 p-1" v-model="illnessOrOperation">
          </div>
        </div>
  
        <div class="flex flex-col">
          <div class="flex flex-row gap-5">
            <input type="checkbox" v-model="hospitalized">
            <p>HAVE YOU EVER BEEN HOSPITALIZED?</p>
          </div>
  
          <div class="flex flex-col lg:flex-row gap-3 items-center lg:w-3/4 justify-end mt-4">
            <p>IF SO, WHEN AND WHY?</p>
            <input type="text" class="w-full lg:w-auto border-b-2 p-1" v-model="hospitalizationDetails">
          </div>
        </div>
  
        <div class="flex flex-col">
          <div class="flex flex-row gap-5">
            <input type="checkbox" v-model="takingMedications">
            <p>ARE YOU TAKING ANY PRESCRIPTION/ NON-PRESCRIPTION MEDICATION?</p>
          </div>
  
          <div class="flex flex-col lg:flex-row gap-3 items-center lg:w-3/4 justify-end mt-4">
            <p>IF YES, PLEASE SPECIFY:</p>
            <input type="text" class="w-full lg:w-auto border-b-2 p-1" v-model="medicationsDetails">
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
  
          <div class="flex flex-col lg:flex-row gap-3 items-center lg:w-3/4 justify-end mt-4">
            <p>IF YES, PLEASE INDICATE:</p>
            <input type="text" class="w-full lg:w-auto border-b-2 p-1" v-model="womenCondition">
          </div>
        </div>
      </div>
  
      <!-- Guided Questions -->
      <div class="flex flex-col gap-4 lg:h-1/2 w-full lg:w-1/2 mt-10 mb-10 lg:m-0">
        <h2 class="text-2xl mb-2">Guided Questions</h2>
  
        <div class="flex flex-row w-full gap-4">
          <input type="checkbox" v-model="hasToothbrush">
          <p>DO YOU HAVE A TOOTHBRUSH?</p>
        </div>
  
        <div class="flex flex-row w-full gap-4">
          <input type="number" class="w-14 bg-gray-300 rounded-sm text-center" v-model="brushingTimes">
          <p>HOW MANY TIMES DO YOU BRUSH YOUR TEETH?</p>
        </div>
  
        <div class="flex flex-row w-full gap-4">
          <input type="number" class="w-14 bg-gray-300 rounded-sm text-center" v-model="toothbrushChange">
          <p>HOW MANY TIMES DO YOU CHANGE YOUR TOOTHBRUSH IN A YEAR?</p>
        </div>
  
        <div class="flex flex-row w-full gap-4">
          <input type="checkbox" v-model="useToothpaste">
          <p>DO YOU USE TOOTHPASTE IN BRUSHING?</p>
        </div>
  
        <div class="flex flex-row w-full gap-4">
          <input type="number" class="w-14 bg-gray-300 rounded-sm text-center" v-model="dentistVisits">
          <p>HOW MANY TIMES DO YOU VISIT THE DENTIST IN A YEAR?</p>
        </div>
      </div>
    </div>
  
    <p class="mt-8">DO YOU HAVE OR HAVE YOU HAD ANY OF THE FOLLOWING? CHECK WHICH APPLY:</p>
  
    <div class="flex flex-col lg:flex-row justify-between w-full">
      <div class="flex flex-col gap-3">
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
  
      <div class="flex flex-col gap-3">
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
  
      <div class="flex flex-col gap-3">
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
  
      <div class="flex flex-col gap-3">
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
  </div>  
</template>

<!-- <template>
      <div class="flex flex-col w-full h-full lg:h-11/12 lg:w-11/12 gap-5 p-10 lg:border-2 rounded-md overflow-y-scroll">
      <h1 class="text-4xl mb-5 font-bold">MEDICAL HISTORY</h1>

      <div class="flex flex-col lg:flex-row justify-between w-full">
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
      
            <Guided Questions
            <div class="flex flex-col gap-4 h-1/2 w-1/2">
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
          <div class="flex flex-col gap-3">
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
    
          <div class="flex flex-col gap-3">
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
    
          <div class="flex flex-col gap-3">
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
        
            ??? <div class="flex flex-row gap-4">
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

          <div class="flex flex-col gap-3">
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
      </div>
</template> -->
    
<style scoped>
</style>
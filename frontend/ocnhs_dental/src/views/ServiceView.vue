<script setup>
import HomeComponent from '@/components/client/homepage/HomeComponent.vue';
import { useRouter } from 'vue-router';
import { ref, defineProps } from 'vue';
import { useServiceStore } from '@/stores/services';


const router = useRouter()
const serviceStore = useServiceStore()
</script>

<template>
<div class="absolute top-0 left-0 w-full">
  <!-- Header -->
  <div id="home" class="flex flex-row justify-between w-full h-20 p-16 main-color">
    <div class="flex flex-row gap-5 h-full items-center">
      <img src="@/assets/Clinic Assets/Dental Clinic images/image/logo1.png" height="120px" width="100px">
      <h3 class="text-white font-bold text-lg">OLONGAPO CITY NATIONAL HIGH SCHOOL DENTAL CLINIC</h3>
    </div>

    <div class="flex h-full items-center">
      <img src="@/assets/Clinic Assets/Dental Clinic images/image/logo2.png" height="120px" width="100px">
    </div>
  </div>

  <!-- Blogs -->
  <div class="flex flex-col p-10 h-full w-full items-center justify-center">
      <div class="flex flex-col h-8/12 w-8/12 gap-5 p-10 border-2 rounded-md">
            <div v-if="serviceStore.currentService == 1">
                  <div class="flex flex-row gap-10 border-4 w-6/12 rounded-md p-6 items-center overlay-color-2">
                        <img src="@/assets/Clinic Assets/Dental Clinic images/image/flouride.png" height="180px" width="180px" class="rounded-full">
                        <div class="flex flex-col items-center justify-center">
                              <h1 class="text-4xl">FLOURIDE APPLICATION</h1>
                              <a href="https://www.youtube.com/watch?v=_LmwPQWfoUw&ab_channel=OCNHSDENTALCLINIC">CLICK HERE TO WATCH VIDEO</a>
                        </div>
                  </div>

                  <div class="flex flex-col gap-4 mt-10">
                        <p>Fluoride application is like giving your teeth a protective shield to keep them strong and healthy. It's a preventive dental treatment that helps to fortify your tooth enamel, making it more resistant to decay and cavities.</p>
                        <p>When you go for a fluoride application at the dentist, it's like getting a special treatment that strengthens your teeth from the outside in. The fluoride gel or varnish they apply acts as a barrier, guarding your teeth against harmful acids and bacteria that can cause damage.</p>
                        <p>Just like how you might apply sunscreen to protect your skin from the sun's rays, fluoride application shields your teeth from the harmful effects of acids and sugars in the mouth. It's a simple yet effective way to maintain good oral health and prevent dental issues down the road.</p>
                        <p>Whether it's done at the dentist's office or through daily use of fluoride toothpaste at home, incorporating fluoride into your oral care routine is like giving your teeth an extra layer of defense to keep them healthy and strong.</p>
                        <p>So, think of fluoride application as a little extra boost to help keep your smile bright, your teeth strong, and your visits to the dentist free from cavities. If you have more questions or need further details, feel free to ask or visit our dental clinic!</p>
                  </div>

                  <div class="w-full flex justify-end mt-12">
                        <button @click="() => { router.push('/') }">Return to Homepage</button>
                  </div>
            </div>

            <div v-if="serviceStore.currentService == 2">
                  <div class="flex flex-row gap-10 border-4 w-6/12 rounded-md p-6 items-center overlay-color-2">
                        <img src="@/assets/Clinic Assets/Dental Clinic images/image/cleaning.jpg" height="180px" width="180px" class="rounded-full">
                        <div class="flex flex-col items-center justify-center">
                              <h1 class="text-4xl">ORAL PROPHYLAXIS/CLEANING</h1>
                              <a href="https://www.youtube.com/watch?v=TmeibD-xb8k&ab_channel=OCNHSDENTALCLINIC">CLICK HERE TO WATCH VIDEO</a>
                        </div>
                  </div>

                  <div class="flex flex-col gap-4 mt-10">
                        <p>Getting an oral prophylaxis, also known as a dental cleaning, is like giving your teeth a spa day! It's a professional dental procedure that aims to clean your teeth thoroughly, remove plaque buildup, and keep your mouth healthy.</p>
                        <p>Think of oral prophylaxis as a refreshing treatment for your teeth and gums. Just like how you might deep clean your house to remove dirt and grime, a dental cleaning clears away plaque, tartar, and stains from your teeth to prevent cavities and gum disease.</p>
                        <p>During an oral prophylaxis, the dental hygienist uses special tools to scrape away plaque and tartar that can't be removed by regular brushing alone. They also polish your teeth to make them smooth and shiny, leaving you with a fresh, clean feeling.</p>
                        <p>It's like pressing the reset button for your oral health, giving your smile a fresh start and helping you maintain a bright, healthy mouth. Regular dental cleanings are essential for preventing oral problems and keeping your teeth and gums in top shape.</p>
                        <p>So, the next time you schedule an oral prophylaxis, think of it as a pampering session for your teeth – a little TLC to keep your smile sparkling and your oral health in check. If you have more questions about oral prophylaxis or dental cleanings, feel free to ask for more information or visit our dental clinic!</p>                        
                  </div>

                  <div class="w-full flex justify-end mt-12">
                        <button @click="() => { router.push('/') }">Return to Homepage</button>
                  </div>
            </div>

            <div v-if="serviceStore.currentService == 3">
                  <div class="flex flex-row gap-10 border-4 w-6/12 rounded-md p-6 items-center overlay-color-2">
                        <img src="@/assets/Clinic Assets/Dental Clinic images/image/restoration.png" height="180px" width="180px" class="rounded-full">
                        <div class="flex flex-col items-center justify-center">
                              <h1 class="text-4xl">RESTORATION/PASTA</h1>
                              <a href="https://www.youtube.com/watch?v=WrY5gW7quCk&ab_channel=OCNHSDENTALCLINIC">CLICK HERE TO WATCH VIDEO</a>
                        </div>
                  </div>

                  <div class="flex flex-col gap-4 mt-10">
                        <p>Restoration, also known as "pasta" in colloquial terms, is like giving your tooth a makeover to restore its strength and appearance. It's like patching up a worn-out piece of clothing to make it look and function like new again.</p>
                        <p>When a tooth is damaged by decay, fracture, or wear, a dental restoration is needed to repair it and prevent further problems. It's similar to fixing a broken piece of a puzzle to complete the picture and ensure everything fits together seamlessly.</p>
                        <p>During a dental restoration, the dentist uses special materials like composite resin or amalgam to fill cavities, repair cracks, or restore missing parts of a tooth. It's like using the right tools and materials to mend a broken item so it can regain its functionality and aesthetics.</p>
                        <p>The restoration process not only strengthens the tooth but also improves its appearance, helping you smile confidently and chew comfortably. It's like adding a fresh coat of paint to revitalize a faded wall, giving your tooth a new lease on life.</p>
                        <p>Just like how a skilled craftsman carefully restores a valuable piece of art, your dentist skillfully performs a restoration to preserve the health and beauty of your smile. It's a blend of art and science, ensuring that your tooth is both structurally sound and visually pleasing.</p>
                        <p>So, think of dental restoration as a personalized touch-up for your tooth, restoring its strength, function, and beauty. If you have more questions about dental restorations or "pasta," feel free to ask for further information or visit our dental clinic!</p>                        
                  </div>

                  <div class="w-full flex justify-end mt-12">
                        <button @click="() => { router.push('/') }">Return to Homepage</button>
                  </div>
            </div>

            <div v-if="serviceStore.currentService == 4">
                  <div class="flex flex-row gap-10 border-4 w-6/12 rounded-md p-6 items-center overlay-color-2">
                        <img src="@/assets/Clinic Assets/Dental Clinic images/image/extraction.jpg" height="180px" width="180px" class="rounded-full">
                        <div class="flex flex-col items-center justify-center">
                              <h1 class="text-4xl">EXTRACTION/BUNOT</h1>
                              <a href="https://www.youtube.com/watch?v=n_05qNsB6So&ab_channel=OCNHSDENTALCLINIC">CLICK HERE TO WATCH VIDEO</a>
                        </div>
                  </div>

                  <div class="flex flex-col gap-4 mt-10">
                        <p>Imagine tooth extraction or "bunot" as a necessary but gentle farewell to a troublesome tooth that just can't stay in your mouth any longer. It's like saying goodbye to a troublesome houseguest who has overstayed their welcome.</p>
                        <p>During a tooth extraction, the dentist carefully and skillfully removes the problematic tooth from its place in your mouth to alleviate pain, prevent infection, or make room for other teeth. It's like removing a troublesome piece from a puzzle to help the whole picture come together more smoothly.</p>
                        <p>Although the idea of having a tooth extracted may sound daunting, the procedure is carried out with care to ensure minimal discomfort. Just like plucking a weed from a garden to help the other plants thrive, tooth extraction aims to improve your oral health and prevent further issues.</p>
                        <p>After the extraction, your mouth is given time to heal, much like how a wound heals after a cut. It's a temporary inconvenience for long-term benefits, helping you maintain a healthy smile and prevent complications down the road.</p>
                        <p>So, think of tooth extraction as a necessary step in your oral health journey, clearing the way for a healthier, happier mouth. If you have any more questions about tooth extraction or "bunot," feel free to ask for more details or visit our dental clinic!</p>                        
                  </div>

                  <div class="w-full flex justify-end mt-12">
                        <button @click="() => { router.push('/') }">Return to Homepage</button>
                  </div>
            </div>
      </div>
  </div>

  <!-- Footer -->
  <div class="flex flex-row justify-evenly items-center h-full w-full overlay-color-2 p-10">
    <div>
      <img src="@/assets/Clinic Assets/Dental Clinic images/image/logo2.png" height="240px" width="240px">
    </div>

    <div>
      <h4>OLONGAPO CITY NATIONAL HIGH SCHOOL</h4>
      <p>Address:</p>
      <p>Rizal Av. Cor 14th St. East  Tapinac, Olongapo City</p>
      <p>Contact Details: </p>
      <p>(047) 222-2568/(047) 603-0570/ (+63) 920-905-8815</p>
      <p>Email Address:</p>
      <p>olongapo.city@deped.gov.ph</p>
      <p>ocnhsdentalpage@gmail.com</p>
    </div>

    <div class="flex flex-col footer-links-2">
      <p>DEPED QUICK LINKS</p>
      <a>DepEd Central Office</a>
      <a>DepEd Regional Office III</a>
      <a>Civil Service Commission</a>
      <a>Department of Budget & Management</a>
      <a>Commission on Audit</a>
      <a>PAGASA</a>
    </div>

    <div class="flex flex-col footer-links-2">
      <p>DEPED PORTALS</p>
      <a>Enhanced Basic Education</a>
      <a>Information System (EBEIS)</a>
      <a>Learner Information System (LIS)</a>
      <a>Learning Resources Management</a>
      <a>and Development System (LRMDS)</a>
      <a>Program Management Information</a>
      <a>System (PMIS)</a>
      <a>Enterprise Human Resources</a>
      <a>Information System (EHRIS)</a>
      <a>WASH in School System (WINS)</a>
    </div>

    <div>
      <img src="@/assets/Clinic Assets/Dental Clinic images/image/logo1.png" height="240px" width="240px">
    </div>
  </div>

  <!-- Footer 2 -->
  <div class="flex flex-row justify-evenly items-evenly h-full w-full overlay-color p-10">
    <div class="flex flex-col justify-center 3/12">
      <img src="@/assets/Clinic Assets/Dental Clinic images/image/logo3.png" height="240px" width="240px">
    </div>

    <div class="flex flex-col justify-center 3/12 text-white">
      <h4>REPUBLIC OF THE PHILIPPINES</h4>
      <p>All content is in the public domain unless otherwise stated.</p>
    </div>

    <div class="flex flex-col justify-center 3/12 text-white">
      <p>ABOUT GOVPH</p>
      <p>
        Learn more about the Philippine
        government, its structure, how
        government works and the people
        behind it.
      </p>
      <p>GOV.PH</p>
      <p>Open Data Portal</p>
      <p>Official Gazette</p>
    </div>

    <div class="flex flex-col w-3/12 footer-links-1">
      <a>Office of the President</a>
      <a>Office of the Vice President</a>
      <a>Senate of the Philippines</a>
      <a>House of Representatives</a>
      <a>Supreme Court</a>
      <a>Court of Appeals</a>
      <a>Sandiganbayan</a>
    </div>
  </div>

  <div class="flex justify-center items-center w-full main-color">
    <p class="text-white">2025 All Rights Reserved.</p>
  </div>
</div>
</template>

<style scoped>
.main-color {
  background-color: #3B6364;
}

.secondary-color {
  background-color: #E7E8FF;
}

.overlay-color {
  background-color: #80B1B1;
}

.overlay-color-2 {
  background-color: #9cc7be;
}

a {
  cursor: pointer;
}

.negative-marg {
  margin-top: -40%;
}

#about-1 {
  background-image: url('@/assets/Clinic Assets/Dental Clinic images/image/dentist-mod.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

#about-2 {
  background-image: url('@/assets/Clinic Assets/Dental Clinic images/image/assistant-mod.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

#blog-1 {
  background-image: url('@/assets/Clinic Assets/Dental Clinic images/blog/1.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

#blog-2 {
  background-image: url('@/assets/Clinic Assets/Dental Clinic images/blog/2.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

#blog-3 {
  background-image: url('@/assets/Clinic Assets/Dental Clinic images/blog/3.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

#blog-4 {
  background-image: url('@/assets/Clinic Assets/Dental Clinic images/blog/4.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

#blog-5 {
  background-image: url('@/assets/Clinic Assets/Dental Clinic images/blog/5.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

#blog-6 {
  background-image: url('@/assets/Clinic Assets/Dental Clinic images/blog/6.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

#blog-7 {
  background-image: url('@/assets/Clinic Assets/Dental Clinic images/blog/7.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

#blog-8 {
  background-image: url('@/assets/Clinic Assets/Dental Clinic images/blog/8.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

.footer-links-1 a {
  color: white;
}

.footer-links-2 a {
  color: black;
}
</style>
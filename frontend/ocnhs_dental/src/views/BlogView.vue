<script setup>
import HomeComponent from '@/components/client/homepage/HomeComponent.vue';
import { useRouter } from 'vue-router';
import { ref, defineProps } from 'vue';
import { useBlogStore } from '@/stores/blogs';

const router = useRouter()
const blogStore = useBlogStore()
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
  <div class="flex flex-col lg:p-10 h-full w-full items-center justify-center">
      <div class="flex flex-col w-full lg:h-8/12 lg:w-8/12 gap-5 p-10 border-2 rounded-md">
            <div v-if="blogStore.blog == 1">
                  <div class="flex flex-row gap-10 border-4 lg:w-6/12 rounded-md p-3 lg:p-6 items-center overlay-color-2">
                        <img src="@/assets/Clinic Assets/Dental Clinic images/blogcontent/1.png" height="180px" width="180px" class="hidden lg:block">
                        <h1 class="text-4xl">The Proper Way to Brush Your Teeth</h1>
                  </div>

                  <div class="flex flex-col gap-4 mt-10">
                    <p>THE PROPER WAY TO BRUSH YOUR TEETH</p>
                    <p>1. Choose the Right Toothbrush: Use a soft-bristled toothbrush that is comfortable to hold and can reach all areas of your mouth easily.</p>
                    <p>2. Use Fluoride Toothpaste: Apply a pea-sized amount of fluoride toothpaste to your toothbrush. Fluoride helps strengthen tooth enamel and prevent tooth decay.</p>
                    <p>3. Brushing Technique:</p>
                    <ul>
                          <li>Position Your Toothbrush: Hold your toothbrush at a 45-degree angle to your gums.</li>
                          <li>Brushing Motion: Use gentle circular motions to clean the outer surfaces of your teeth. Pay extra attention to the gumline where plaque tends to accumulate.</li>
                          <li>Inner Surfaces: Brush the inner surfaces of your teeth using the same circular motion.</li>
                          <li>Chewing Surfaces: For the chewing surfaces of your molars, use a back-and-forth motion.</li>
                          <li>Brush Your Tongue: Don’t forget to gently brush your tongue to remove bacteria and freshen your breath.</li>
                    </ul>
                    <p>Duration: Brush your teeth for at least two minutes. You can divide your mouth into four quadrants and spend 30 seconds on each section.</p>
                    <p>Rinse Thoroughly: After brushing, rinse your mouth with water to remove any remaining toothpaste and debris.</p>
                    <p>Replace Your Toothbrush: Replace your toothbrush with a new one every 3-4 months or sooner if the bristles are frayed.</p>
                    <p>Frequency: Brush your teeth at least twice a day, preferably in the morning and before bed. You can also brush after meals if possible.</p>
                    <p>Floss Regularly: While brushing is crucial, don’t forget to floss daily to clean between your teeth and along the gumline.</p>
                    <p>Regular Dental Check-ups: Visit your dentist regularly for professional cleanings and check-ups to maintain optimal oral health.</p>
                  </div>
            </div>

            <div v-else-if="blogStore.blog == 2">
              <div class="flex flex-row gap-10 border-4 lg:w-6/12 rounded-md p-3 lg:p-6 items-center overlay-color-2">
                    <img src="@/assets/Clinic Assets/Dental Clinic images/blogcontent/2.png" height="180px" width="180px" class="hidden lg:block">
                    <h1 class="text-4xl">Surprising causes of bad breath</h1>
              </div>
              
              <div class="flex flex-col gap-4 mt-10">
                <p>Dry Mouth: Reduced saliva flow, whether due to medications, mouth breathing habits, or dehydration, creates an environment where bacteria flourish in the mouth. These bacteria produce volatile sulfur compounds that contribute to bad breath. To combat dry mouth-related halitosis, staying hydrated, using saliva-stimulating products like sugar-free gum, and addressing underlying medical conditions are crucial. Regular dental visits can also help manage and mitigate dry mouth symptoms to prevent bad breath.</p>
                <p>Sinus Issues: Sinus infections or allergies can cause post-nasal drip, where excess mucus drips down the throat and into the mouth. This mucus can harbor bacteria and emit foul odors, contributing to bad breath. Treating the underlying sinus condition with medications, nasal irrigation, or allergy management can reduce post-nasal drip and alleviate associated bad breath. Maintaining good oral hygiene alongside managing sinus issues can further help control halitosis.</p>
                <p>Digestive Problems: Conditions like gastroesophageal reflux disease (GERD) or stomach ulcers can cause acid reflux, where stomach acids flow back into the esophagus and sometimes into the mouth. These acids can create an acidic environment in the mouth, leading to bad breath. Managing digestive issues through dietary changes, medications, and lifestyle modifications recommended by a healthcare provider can help reduce acid reflux and improve breath odor.</p>
                <p>Certain Foods: Foods like garlic, onions, spices, and certain oils contain strong-smelling compounds that can linger in the mouth and be absorbed into the bloodstream, affecting breath odor. These compounds are then released when exhaling, contributing to temporary bad breath. Practicing good oral hygiene, using mouthwash or chewing sugar-free gum after meals, and choosing foods less likely to cause strong odors can help mitigate food-related halitosis.</p>
                <p>Tobacco Products: Smoking and chewing tobacco contribute to bad breath by drying out the mouth and reducing saliva production, which normally helps cleanse the mouth of odor-causing bacteria. Additionally, tobacco contains chemicals that linger in the mouth, throat, and lungs, producing a distinct and persistent odor that is difficult to mask. Long-term tobacco use can also lead to gum disease, which further exacerbates bad breath. Quitting smoking or using tobacco products is crucial for improving breath odor and overall oral health. Seeking assistance from healthcare professionals or support groups can aid in successful cessation.</p>
                <p>Medical Conditions: Conditions such as diabetes, liver disease, and respiratory infections can alter breath odor due to metabolic changes or bacterial overgrowth. In diabetes, for instance, poorly controlled blood sugar levels can lead to a fruity or acetone-like odor on the breath due to the presence of ketones. Liver disease can cause a musty or ammonia-like smell as the liver fails to effectively process toxins. Respiratory infections can introduce bacteria or mucus into the mouth and throat, contributing to foul breath. Managing these medical conditions through proper treatment and monitoring can help improve breath odor.</p>
                <p>Dental Issues: Cavities, gum disease (gingivitis or periodontitis), and ill-fitting dental appliances can trap food particles and bacteria in the mouth, leading to bad breath. Cavities provide a haven for bacteria to thrive and produce odor-causing compounds. Gum disease causes inflammation and can result in pockets around the teeth where bacteria accumulate, emitting foul odors. Poorly fitting dentures or dental appliances can harbor bacteria and food debris, contributing to persistent bad breath. Regular dental visits for cleanings, treatments for cavities or gum disease, and adjustments to dental appliances can help manage and reduce halitosis.</p>
                <p>Crash Dieting: Rapid weight loss diets often lead to the body breaking down fats for energy, producing ketones. These ketones can be detected on the breath, causing a fruity or acetone-like odor. Additionally, crash diets can lead to dehydration and reduced saliva production, creating an environment where bacteria thrive and contribute to bad breath. Gradual and sustainable weight loss methods, combined with adequate hydration and maintaining good oral hygiene practices, can help mitigate diet-related halitosis.</p>
                <p>Stress: Stress can contribute to bad breath by increasing dry mouth and altering digestive processes. When stressed, saliva production may decrease, allowing bacteria to proliferate and produce odor-causing compounds. Stress can also affect digestive functions, leading to conditions like acid reflux or poor digestion, which can further contribute to bad breath. Managing stress through relaxation techniques, adequate hydration, regular meals, and practicing good oral hygiene can help reduce stress-related halitosis.</p>
              </div>          
            </div>

            <div v-else-if="blogStore.blog == 3">
              <div class="flex flex-row gap-10 border-4 lg:w-6/12 rounded-md p-3 lg:p-6 items-center overlay-color-2">
                    <img src="@/assets/Clinic Assets/Dental Clinic images/blogcontent/3.png" height="180px" width="180px" class="hidden lg:block">
                    <h1 class="text-4xl">How bad oral hygiene can lead to oral cancer?</h1>
              </div>
              
              <div class="flex flex-col gap-4 mt-10">
                <p>
                  The relationship between bad oral hygiene and oral cancer is complex and involves several contributing factors. It's important to note that while poor oral hygiene is a risk factor for oral cancer, it does not directly cause cancer. Rather, it contributes to an environment where other risk factors can have a greater impact on oral health. Practicing good oral hygiene—regular brushing, flossing, and dental check-ups—plays a crucial role in preventing gum disease and reducing the overall risk of oral cancer. 
                  Early detection through regular dental visits can also aid in identifying potential oral health issues before they progress to cancerous conditions.
                </p>
                <p>Plaque and Bacteria Build-Up: Poor oral hygiene, such as irregular brushing and flossing, allows plaque—a sticky film of bacteria—to accumulate on teeth and gums. This plaque can harden into tartar, which harbors more bacteria and irritates the gums.</p>
                <p>Gum Disease (Periodontitis): If left unchecked, plaque buildup can lead to gum disease. Periodontitis is a severe form of gum disease where the gums pull away from the teeth, creating pockets that accumulate more bacteria. Chronic inflammation in the gums can damage the soft tissue and bone that support the teeth.</p>
                <p>Chronic Inflammation and Cell Damage: Inflamed gums and chronic irritation from bacteria and toxins can damage cells in the oral cavity over time. This constant irritation and inflammation create an environment where normal cellular processes can be disrupted, potentially leading to mutations in DNA—changes that are characteristic of cancer development.</p>
                <p>HPV (Human Papillomavirus) Infection: HPV, particularly HPV-16, has been linked to some cases of oral cancer. Poor oral hygiene and periodontal disease can create an environment where viral infections like HPV can thrive and potentially increase the risk of oral cancer development.</p>
                <p>Tobacco and Alcohol Use: Bad oral hygiene often coexists with other risk factors for oral cancer, such as smoking tobacco or heavy alcohol use. These substances further irritate the oral tissues and increase the likelihood of cellular damage and mutation.</p>
                <p>Weakened Immune Response: Chronic inflammation from poor oral hygiene can weaken the immune system's ability to defend against infections and repair damaged cells. A compromised immune response may allow abnormal cells to proliferate unchecked, contributing to the development of oral cancer.</p>
                <p>Oral Lesions and Poor Detection: Poor oral hygiene may mask or delay the detection of early signs of oral cancer, such as oral lesions or sores. Regular dental check-ups are essential for detecting these abnormalities early when they are more treatable.</p>                
              </div>          
            </div>

            <div v-else-if="blogStore.blog == 4">
              <div class="flex flex-row gap-10 border-4 lg:w-6/12 rounded-md p-3 lg:p-6 items-center overlay-color-2">
                    <img src="@/assets/Clinic Assets/Dental Clinic images/blogcontent/4.png" height="180px" width="180px" class="hidden lg:block">
                    <h1 class="text-4xl">The relationship between diet and oral health explained</h1>
              </div>
              
              <div class="flex flex-col gap-4 mt-10">
                <p>The connection between diet and oral health is intricate and profound, influencing not only the condition of teeth and gums but also overall systemic health. A balanced diet plays a crucial role in maintaining healthy teeth and gums, while poor dietary choices can lead to various oral health problems. This essay will explore in detail how different aspects of diet impact oral health, the nutrients essential for maintaining oral health, common dietary factors that contribute to oral diseases, and practical dietary guidelines for promoting optimal oral health.</p>

                <p><strong>Nutrients Essential for Oral Health</strong></p>

                <p>Several key nutrients play vital roles in maintaining oral health:</p>

                <p><strong>Calcium and Phosphorus:</strong> These minerals are essential for the formation and remineralization of tooth enamel, the protective outer layer of teeth. Calcium helps strengthen teeth and bones, while phosphorus aids in maintaining tooth structure and enamel integrity.</p>

                <p><strong>Vitamin D:</strong> Necessary for the absorption of calcium and phosphorus from the intestines, vitamin D supports bone density in the jaw and helps prevent tooth decay and gum disease.</p>

                <p><strong>Vitamin A:</strong> Important for maintaining healthy mucous membranes and saliva production, which help protect teeth and gums from infections.</p>

                <p><strong>Vitamin C:</strong> Essential for collagen production, vitamin C is crucial for maintaining healthy gums and supporting the healing of gum tissues.</p>

                <p><strong>Antioxidants:</strong> Including vitamins E and C, as well as phytonutrients like flavonoids and polyphenols, antioxidants help reduce inflammation and protect gum tissues from damage caused by oxidative stress.</p>

                <p><strong>Omega-3 Fatty Acids:</strong> Found in fish, flaxseeds, and walnuts, omega-3 fatty acids have anti-inflammatory properties that can help reduce the risk of gum disease.</p>

                <p><strong>Impact of Diet on Oral Health</strong></p>

                <p><strong>Sugar and Carbohydrates</strong><br>
                The most significant dietary factor contributing to dental caries (cavities) is the consumption of sugars and refined carbohydrates. Sugars, including sucrose (table sugar), fructose, and glucose, are fermentable carbohydrates that bacteria in dental plaque metabolize to produce acids. These acids lower the pH level in the mouth, leading to demineralization of tooth enamel and eventual decay if left untreated. The frequency of sugar consumption and the form of sugar (solid vs. liquid) also influence the risk of cavities. Sticky candies and sugary drinks that linger in the mouth increase the exposure of teeth to acids, whereas consuming sugars with meals and rinsing with water afterward can mitigate their harmful effects.</p>

                <p><strong>Acidic Foods and Beverages</strong><br>
                Acidic foods and beverages, such as citrus fruits, tomatoes, vinegar, and carbonated drinks, can erode tooth enamel over time. Acidic erosion weakens the protective layer of teeth, making them more susceptible to decay and sensitivity. It's essential to consume acidic foods in moderation and rinse with water afterward to neutralize acids and minimize their impact on teeth.</p>

                <p><strong>Texture and Consistency of Foods</strong><br>
                The texture and consistency of foods also influence oral health. Sticky and chewy foods, such as dried fruits, caramels, and soft candies, can adhere to teeth and stay in the mouth longer, increasing the risk of cavities. On the other hand, crunchy fruits and vegetables (like apples, carrots, and celery) have a natural abrasive effect that helps clean teeth and stimulate saliva production. Saliva plays a crucial role in neutralizing acids, remineralizing enamel, and washing away food particles and bacteria.</p>

                <p><strong>Systemic Health Conditions and Oral Health</strong></p>

                <p>Certain systemic health conditions can impact oral health and vice versa:</p>

                <p><strong>Diabetes:</strong> Poorly controlled diabetes can increase the risk of gum disease due to elevated blood sugar levels compromising the body's ability to fight infections, including those in the gums.</p>

                <p><strong>Osteoporosis:</strong> Affects bone density, including the jawbone, which can increase the likelihood of tooth loss and other dental issues.</p>

                <p><strong>Nutritional Deficiencies:</strong> Inadequate intake of essential nutrients like vitamins and minerals can compromise oral health, leading to weakened teeth, gum disease, and delayed wound healing.</p>

                <p><strong>Practical Dietary Guidelines for Optimal Oral Health</strong></p>

                <p>To promote optimal oral health through diet, consider the following guidelines:</p>

                <p><strong>Eat a Balanced Diet:</strong> Include a variety of nutrient-rich foods such as fruits, vegetables, whole grains, lean proteins, and dairy products to ensure adequate intake of essential vitamins and minerals.</p>

                <p><strong>Limit Sugary Foods and Beverages:</strong> Reduce consumption of sugary snacks, candies, sodas, and desserts. When consuming sugary foods, do so with meals rather than as snacks, and rinse with water afterward.</p>

                <p><strong>Choose Tooth-Friendly Snacks:</strong> Opt for snacks that are low in sugar and acid, such as cheese, yogurt, raw vegetables, and nuts.</p>

                <p><strong>Drink Plenty of Water:</strong> Water helps rinse away food particles and neutralize acids in the mouth. Fluoridated water also helps protect teeth against decay.</p>

                <p><strong>Practice Good Oral Hygiene:</strong> Brush your teeth at least twice a day with fluoride toothpaste, floss daily, and visit your dentist regularly for professional cleanings and check-ups.</p>

                <p><strong>Consider Nutritional Supplements:</strong> If your diet is deficient in essential nutrients, consider supplements under the guidance of a healthcare professional.</p>

                <p>The relationship between diet and oral health is profound and multifaceted. A balanced diet rich in essential nutrients supports healthy teeth and gums, while poor dietary choices, particularly high consumption of sugars and acidic foods, can lead to dental caries, gum disease, and other oral health problems. By understanding how different aspects of diet impact oral health and following practical dietary guidelines, individuals can effectively maintain optimal oral health throughout their lives. Combined with good oral hygiene practices and regular dental care, a nutritious diet plays a pivotal role in promoting not only a healthy smile but also overall well-being.</p>
              </div>          
            </div>

            <div v-else-if="blogStore.blog == 5">
              <div class="flex flex-row gap-10 border-4 lg:w-6/12 rounded-md p-3 lg:p-6 items-center overlay-color-2">
                    <img src="@/assets/Clinic Assets/Dental Clinic images/blogcontent/5.png" height="180px" width="180px" class="hidden lg:block">
                    <h1 class="text-4xl">8 ways poor oral hygiene can impact your life</h1>
              </div>
              
              <div class="flex flex-col gap-4 mt-10">
                <p><strong>Poor oral hygiene</strong> can have significant impacts on overall health and quality of life. Maintaining good oral hygiene through regular brushing, flossing, and dental check-ups is crucial not only for oral health but also for overall well-being and quality of life. Here are <strong>8 ways</strong> it can affect you:</p>
                <p><strong>1. Tooth Decay:</strong> Neglecting oral hygiene leads to plaque buildup, which produces acids that erode tooth enamel, causing cavities. Untreated cavities can progress to tooth infections or abscesses, resulting in pain, tooth loss, and the need for costly dental treatments.</p>
                <p><strong>2. Gum Disease:</strong> Gingivitis is the early stage of gum disease characterized by inflammation and bleeding gums. Without proper care, it can progress to periodontitis, where gums pull away from teeth, forming pockets that accumulate bacteria and debris. This can lead to bone loss around teeth, loosening of teeth, and eventual tooth loss.</p>
                <p><strong>3. Bad Breath:</strong> Bacteria in the mouth feed on food particles left behind after eating, releasing foul-smelling gases. Persistent bad breath (halitosis) is often a sign of poor oral hygiene, indicating the presence of bacteria and potential dental problems like gum disease or tooth decay.</p>
                <p><strong>4. Systemic Health Issues:</strong> Poor oral health has been linked to systemic health problems such as cardiovascular disease, diabetes, and respiratory infections. Bacteria from the mouth can enter the bloodstream, causing inflammation and potentially contributing to these conditions.</p>
                <p><strong>5. Impact on Nutrition:</strong> Painful or missing teeth can make chewing difficult, leading to dietary changes and inadequate nutrition. This can affect overall health, weakening the immune system and slowing down the body's ability to heal.</p>
                <p><strong>6. Social and Psychological Effects:</strong> Chronic bad breath, visible decayed teeth, or tooth loss can impact self-esteem and social interactions. Individuals may avoid smiling or speaking openly, affecting relationships and confidence.</p>
                <p><strong>7. Financial Burden:</strong> Preventable dental issues can lead to expensive treatments such as fillings, root canals, and even tooth replacement with implants or dentures. Regular dental check-ups and good oral hygiene habits can help prevent these costly procedures.</p>
                <p><strong>8. Dental Emergencies:</strong> Neglecting oral hygiene increases the likelihood of dental emergencies such as severe toothaches, infections, or injuries. These emergencies often require immediate dental care and can be both physically and financially stressful.</p>                
              </div>          
            </div>

            <div v-else-if="blogStore.blog == 6">
              <div class="flex flex-row gap-10 border-4 lg:w-6/12 rounded-md p-3 lg:p-6 items-center overlay-color-2">
                    <img src="@/assets/Clinic Assets/Dental Clinic images/blogcontent/3.png" height="180px" width="180px" class="hidden lg:block">
                    <h1 class="text-4xl">Teaching children how to take care of their teeth</h1>
              </div>
              
              <div class="flex flex-col gap-4 mt-10">
                <p>Teaching children good oral hygiene habits early in life sets the foundation for a lifetime of healthy teeth and gums. By incorporating these strategies, you can help your children develop strong oral hygiene habits that will benefit them throughout their lives. Here are some effective strategies to help children learn how to take care of their teeth:</p>

                <div>
                  <p>Start Early</p>
                  <p>·Begin cleaning your baby's gums with a soft, damp cloth before their teeth even come in.</p>
                  <p>·Once teeth start to appear, use a small, soft-bristled toothbrush and water to brush them gently.</p>
                </div>

                <div>
                  <p>Make Brushing Fun</p>
                  <p>·Choose a toothbrush with their favorite character or in a fun color.</p>
                  <p>·Use flavored toothpaste that is safe for children.</p>
                  <p>·Play their favorite song or set a timer for two minutes to make sure they brush long enough.</p>
                </div>

                <div>
                  <p>Teach Proper Brushing Technique</p>
                  <p>·Show them how to hold the toothbrush at a 45-degree angle to the gums.</p>
                  <p>·Teach them to brush in gentle, circular motions on all surfaces of the teeth.</p>
                  <p>·Make sure they brush their tongue to remove bacteria and freshen their breath.</p>
                </div>

                <div>
                  <p>Flossing</p>
                  <p>·Help them floss between their teeth once they have two teeth that touch.</p>
                  <p>·Use child-friendly floss picks to make the process easier.</p>
                </div>

                <div>
                  <p>Lead by Example</p>
                  <p>·Brush and floss your teeth with your children to show them that it’s an important and regular part of your routine.</p>
                  <p>·Let them see you take care of your own teeth and explain why it’s important.</p>
                </div>

                <div>
                  <p>Establish a Routine</p>
                  <p>·Make brushing and flossing a regular part of their daily routine, twice a day.</p>
                  <p>·Encourage brushing after meals when possible.</p>
                </div>

                <div>
                  <p>Teach About Healthy Eating</p>
                  <p>·Explain how sugary and acidic foods and drinks can harm their teeth.</p>
                  <p>·Encourage a balanced diet with plenty of fruits, vegetables, and water.</p>
                </div>

                <div>
                  <p>Regular Dental Visits</p>
                  <p>·Schedule regular dental check-ups starting at age one or when their first tooth comes in.</p>
                  <p>·Make visits to the dentist a positive experience by reading books about dental visits or role-playing at home.</p>
                </div>

                <div>
                  <p>Use Educational Tools</p>
                  <p>·Utilize books, videos, and apps designed to teach children about oral health.</p>
                  <p>·There are many resources available that make learning about dental care fun and engaging.</p>
                </div>

                <div>
                  <p>Positive Reinforcement</p>
                  <p>·Praise your children for brushing and flossing their teeth properly.</p>
                  <p>·Use a reward system, like stickers or a chart, to track their progress and celebrate good habits.</p>
                </div>

                <div>
                  <p>Address Fears and Concerns</p>
                  <p>·Talk to your children about any fears or concerns they might have about dental care.</p>
                  <p>·Be reassuring and explain that dentists are there to help keep their teeth healthy.</p>
                </div>

                <div>
                  <p>Monitor and Assist</p>
                  <p>·Supervise their brushing until they are capable of doing it effectively on their own, usually around age 7 or 8.</p>
                  <p>·Continue to check their brushing and flossing habits as they grow older to ensure they maintain good techniques.</p>
                </div>
              </div>          
            </div>

            <div v-else-if="blogStore.blog == 7">
              <div class="flex flex-row gap-10 border-4 w-6/12 rounded-md p-6 items-center overlay-color-2">
                    <img src="@/assets/Clinic Assets/Dental Clinic images/blogcontent/7.png" height="180px" width="180px" class="hidden lg:block">
                    <h1 class="text-4xl">Dental Cosmetics</h1>
              </div>
              
              <div class="flex flex-col gap-4 mt-10">
                <p>When we talk about dental cosmetics, we're essentially referring to the art and science of improving the appearance of your smile. It's like giving your teeth and gums a makeover to help you feel more confident and happy with how your smile looks.</p>
                <p>Just like how people might get a new haircut or put on makeup to enhance their appearance, dental cosmetic procedures aim to enhance the aesthetics of your teeth. It's all about making your smile more vibrant, aligned, and attractive.</p>
                <p>Imagine it as a way to boost your self-esteem and feel better about showing off your smile to the world. Whether it's brightening your teeth, fixing imperfections, or aligning your smile, dental cosmetics can help you achieve the smile you've always wanted.</p>
                
                <p><strong>Teeth Whitening:</strong> This is a cosmetic dental procedure that aims to lighten the color of your teeth. It can be done in the dentist's office or at home using special kits. The process involves bleaching the teeth to remove stains and discoloration, resulting in a brighter smile.</p>
                
                <p><strong>Dental Crowns/Veneers/Bridges:</strong></p>
                
                <p><strong>Dental Crowns:</strong> Crowns are tooth-shaped caps that are placed over damaged teeth to restore their shape, size, strength, and appearance. They can be made from various materials like porcelain, metal, or a combination of both.</p>
                <p><strong>Types of Dental Crowns:</strong></p>
                <p><strong>Porcelain Crowns:</strong> These are tooth-colored crowns that closely resemble natural teeth in appearance.They are a popular choice for front teeth due to their aesthetic appeal.</p>
                <p><strong>Ceramic Crowns:</strong> Like porcelain crowns, ceramic crowns are also tooth-colored and provide a natural look.They are a good option for people with metal allergies.</p>
                <p><strong>Porcelain-Fused-to-Metal (PFM) Crowns:</strong> These crowns have a metal base for strength with a layer of porcelain fused over it for a natural appearance.They are durable and suitable for both front and back teeth.</p>
                <p><strong>Metal Crowns:</strong> Made of alloys like gold, nickel, chromium, or palladium, metal crowns are known for their strength and durability.They are often used for back teeth that require extra support.</p>
                <p><strong>All-Ceramic Crowns:</strong> These crowns are made entirely of ceramic material, offering a natural look and good strength.They are a versatile option suitable for various teeth.</p>
                <p><strong>Zirconia Crowns:</strong> Zirconia crowns are known for their strength and durability.They are a popular choice for those who need crowns on their molars or teeth that undergo heavy chewing forces.</p>
                <p><strong>Composite Resin Crowns:</strong> These crowns are made of a tooth-colored resin material bonded to the tooth.They are less expensive than other types of crowns but may not be as durable.</p>

                
                <p><strong>Veneers:</strong> Veneers are thin shells made of porcelain or composite resin that are bonded to the front surface of the teeth to improve their appearance. They can be used to fix discoloration, chips, or gaps in teeth.</p>
                <p><strong>Types of Veneer:</strong></p>
                <p><strong>Porcelain Veneers:</strong> Porcelain veneers are wafer-thin, custom-made shells of porcelain that are bonded to the front surface of the teeth.</p>
                <p><strong>Appearance:</strong> They mimic the light-reflecting properties of natural teeth, providing a realistic look.</p>
                <p><strong>Durability:</strong> Porcelain veneers are stain-resistant and typically last longer than composite veneers.</p>
                <p><strong>Composite Resin Veneers:</strong> Composite resin veneers are made of a tooth-colored resin material that is applied directly to the teeth and shaped by the dentist.</p>
                <p><strong>Appearance:</strong> While they can be made to match the color of your natural teeth, composite veneers may not have the same translucency as porcelain veneers.</p>
                <p><strong>Durability:</strong> Composite veneers are more prone to staining and may not last as long as porcelain veneers.</p>

                
                <p><strong>Bridges:</strong> Dental bridges are used to replace one or more missing teeth. They consist of artificial teeth that are anchored in place by crowns on the adjacent natural teeth.</p>
                <p><strong>Types of Bridges:</strong></p>
                <p><strong>Traditional Bridges:</strong> Traditional bridges consist of artificial teeth supported by dental crowns placed on the adjacent natural teeth.</p>
                <p><strong>Cantilever Bridges:</strong> Cantilever bridges are similar to traditional bridges but are supported by a crown on only one side of the artificial tooth.</p>
                <p><strong>Use:</strong> They are often used when there is only one natural tooth next to the gap where the bridge will be placed.</p>
                <p><strong>Maryland Bonded Bridges (Resin-Bonded Bridges):</strong> Maryland bridges consist of artificial teeth held in place by a metal or porcelain framework bonded to the backs of adjacent natural teeth.</p>
                <p><strong>Minimally Invasive:</strong> This type of bridge is less invasive than traditional bridges as it requires minimal preparation of the adjacent teeth.</p>
                <p><strong>Implant-Supported Bridges:</strong> Implant-supported bridges are attached to dental implants surgically placed in the jawbone, providing a stable and long-lasting foundation.</p>
                <p><strong>Benefits:</strong> They offer a more secure and permanent solution for replacing multiple missing teeth without affecting adjacent teeth.</p>          
              </div>          
            </div>

            <div v-else-if="blogStore.blog == 8">
              <div class="flex flex-row gap-10 border-4 w-6/12 rounded-md p-6 items-center overlay-color-2">
                    <img src="@/assets/Clinic Assets/Dental Clinic images/blogcontent/2.png" height="180px" width="180px" class="hidden lg:block">
                    <h1 class="text-4xl">Dental Surgery</h1>
              </div>
              
              <div class="flex flex-col gap-4 mt-10">
                <p><strong>Dental Surgery:</strong>Dental surgery is a field of dentistry that involves surgical procedures to address various oral health issues.These surgeries are typically performed by dental specialists like oral surgeons or periodontists.Dental surgery can range from simple extractions to complex procedures like dental implants or jaw surgeries.These are just a few examples of the types of dental surgeries that address various dental conditions.The specific type of surgery recommended will depend on individual oral health needs and the expertise of the dental specialist.</p>
                <p><strong>Tooth Extraction:</strong>Tooth extraction involves the removal of a tooth from its socket in the jawbone.</p>
                <p><strong>Reasons:</strong>This may be necessary for severely decayed teeth, impacted wisdom teeth, overcrowded teeth, or to prepare for orthodontic treatment.</p>
                <p><strong>Dental Implants:</strong>Dental implants are artificial tooth roots surgically placed in the jawbone to support replacement teeth.</p>
                <p><strong>Procedure:</strong>It includes implant placement, healing, and attaching the final restoration like a crown, bridge, or denture.</p>
                <p><strong>Wisdom Teeth Removal:</strong>Wisdom teeth, or third molars, may need surgical extraction if they are impacted, causing pain, infection, or crowding.</p>
                <p><strong>Root Canal Therapy:</strong>Root canal therapy removes infected or damaged pulp from inside a tooth to save it from extraction.</p>
                <p><strong>Gum Surgery (Periodontal Surgery):</strong>Gum surgery is done to treat gum disease, gum recession, or reshape the gum line for aesthetic reasons.</p>
                <p><strong>Types:</strong>Procedures include gum grafts, flap surgery, and gingivectomy to address different gum issues.</p>
                <p><strong>Jaw Surgery (Orthognathic Surgery):</strong>Jaw surgery corrects jaw misalignment, TMJ disorders, or other structural issues affecting the jaw.</p>                
              </div>          
            </div>

            <div class="w-full flex justify-end mt-12">
                  <button @click="() => { router.push('/') }" class="cursor-pointer hover:bg-black hover:text-white p-2 rounded-md transition duration-300 ease-in-out">Return to Homepage</button>
            </div>
      </div>
  </div>

  <!-- Footer -->
  <div class="flex flex-col lg:flex-row justify-evenly items-center h-full w-full overlay-color-2 p-10">
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
  <div class="flex flex-col lg:flex-row justify-evenly items-evenly h-full w-full overlay-color p-4 lg:p-10">
    <div class="flex flex-col justify-center lg:w-3/12">
      <img src="@/assets/Clinic Assets/Dental Clinic images/image/logo3.png" height="240px" width="240px">
    </div>

    <div class="flex flex-col justify-center lg:w-3/12 text-white">
      <h4>REPUBLIC OF THE PHILIPPINES</h4>
      <p>All content is in the public domain unless otherwise stated.</p>
    </div>

    <div class="flex flex-col justify-center lg:w-3/12 text-white">
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

    <div class="flex flex-col lg:w-3/12 footer-links-1">
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
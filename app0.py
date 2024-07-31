import streamlit as st
import pickle
import numpy as np

background_image = "https://img.freepik.com/free-vector/clean-medical-background_53876-97927.jpg?size=626&ext=jpg&ga=GA1.1.734836280.1694843058&semt=ais"

custom_css = f"""
<style>
    .stApp {{
        background-image: url('{background_image}');
        background-size: cover;
        background-attachment: scroll;
    }}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)


# Load the trained model
with open('gnb2_model.pkl', 'rb') as file:
    model, y_pred, y_test= pickle.load(file)

symptoms = ['Abdominal Pain', 'Abnormal Menstruation', 'Acute Liver Failure', 'Altered Sensorium', 
            'Back Pain', 'Belly Pain', 'Blackheads', 'Bladder Discomfort', 'Blister', 
            'Blood In Sputum', 'Bloody Stool', 'Blurred And Distorted Vision', 'Brittle Nails', 
            'Bruising', 'Chest Pain', 'Coma', 'Congestion', 'Constipation', 'Continuous Feel Of Urine',
            'Cramps', 'Depression', 'Diarrhoea', 'Dischromic  Patches', 'Distention Of Abdomen', 
            'Dizziness', 'Drying And Tingling Lips', 'Enlarged Thyroid', 'Excessive Hunger', 
            'Extra Marital Contacts', 'Family History', 'Fast Heart Rate', 'Fluid Overload',
            'Fluid Overload', 'Foul Smell Of Urine', 'Hip Joint Pain', 'History Of Alcohol Consumption',
            'Increased Appetite', 'Inflammatory Nails', 'Internal Itching', 'Irritability', 'Irritation In Anus',
            'Knee Pain', 'Lack Of Concentration', 'Loss Of Balance', 'Loss Of Smell', 'Malaise', 
            'Mild Fever', 'Movement Stiffness', 'Mucoid Sputum', 'Muscle Pain', 'Muscle Weakness', 
            'Neck Pain', 'Obesity', 'Pain During Bowel Movements', 'Pain In Anal Region', 
            'Painful Walking', 'Palpitations', 'Passage Of Gases', 'Phlegm', 'Polyuria',
            'Prominent Veins On Calf', 'Puffy Face And Eyes', 'Pus Filled Pimples', 
            'Receiving Blood Transfusion', 'Receiving Unsterile Injections', 'Red Sore Around Nose',
            'Red Spots Over Body', 'Redness Of Eyes', 'Runny Nose', 'Rusty Sputum', 'Scurring',
            'Silver Like Dusting', 'Sinus Pressure', 'Skin Peeling', 'Slurred Speech',
            'Small Dents In Nails', 'Spinning Movements', 'Stiff Neck', 'Stomach Bleeding', 
            'Swelled Lymph Nodes', 'Swelling Joints', 'Swelling Of Stomach', 'Swollen Blood Vessels', 
            'Swollen Extremeties', 'Swollen Legs', 'Throat Irritation', 'Toxic Look (Typhos)', 
            'Unsteadiness', 'Visual Disturbances', 'Watering From Eyes', 'Weakness In Limbs', 
            'Weakness Of One Body Side', 'Yellow Crust Ooze', 'Yellow Urine', 'Yellowing Of Eyes']

disease_labels = [
    'Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction', 'Peptic ulcer diseae', 'AIDS',
    'Diabetes', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension', 'Migraine', 'Cervical spondylosis',
    'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A',
    'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis',
    'Common Cold', 'Pneumonia', 'Dimorphic hemorrhoids(piles)', 'Heartattack', 'Varicoseveins', 'Hypothyroidism',
    'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthristis', 'Arthritis', '(vertigo) Paroymsal  Positional Vertigo',
    'Acne', 'Urinary tract infection', 'Psoriasis', 'Impetigo'
]

predicted_disease = -1



st.write(f"<h1>Select the symptoms:<h1>",unsafe_allow_html=True)



selected_symptoms = [st.selectbox(f"Symptom {i+1}", symptoms) for i in range(5)]



age_options = list(range(5, 100)) 

age = st.selectbox("Select your Age :", age_options)

if st.button("Check Disease"):
    # Encode user input
    input_vector = np.zeros(len(symptoms))
    for symptom in selected_symptoms:
        index = symptoms.index(symptom)
        input_vector[index] = 1

    
    predicted_disease = model.predict([input_vector])[0]

    st.write(f"<h4>Predicted Disease: {disease_labels[predicted_disease]}<h4>",unsafe_allow_html=True)

if predicted_disease >= 0:
    disease_descriptions = {
        "Drug Reaction":"An adverse drug reaction (ADR) is an injury caused by taking medication. ADRs may occur following a single dose or prolonged administration of a drug or result from the combination of two or more drugs.",
"Malaria":"An infectious disease caused by protozoan parasites from the Plasmodium family that can be transmitted by the bite of the Anopheles mosquito or by a contaminated needle or transfusion. Falciparum malaria is the most deadly type.",
"Allergy":"An allergy is an immune system response to a foreign substance that's not typically harmful to your body.They can include certain foods, pollen, or pet dander. Your immune system's job is to keep you healthy by fighting harmful pathogens.",
"Hypothyroidism":"Hypothyroidism, also called underactive thyroid or low thyroid, is a disorder of the endocrine system in which the thyroid gland does not produce enough thyroid hormone.",
"Psoriasis":"Psoriasis is a common skin disorder that forms thick, red, bumpy patches covered with silvery scales. They can pop up anywhere, but most appear on the scalp, elbows, knees, and lower back. Psoriasis can't be passed from person to person. It does sometimes happen in members of the same family.",
"GERD":"Gastroesophageal reflux disease, or GERD, is a digestive disorder that affects the lower esophageal sphincter (LES), the ring of muscle between the esophagus and stomach. Many people, including pregnant women, suffer from heartburn or acid indigestion caused by GERD.",
"Chronic cholestasis":"Chronic cholestatic diseases, whether occurring in infancy, childhood or adulthood, are characterized by defective bile acid transport from the liver to the intestine, which is caused by primary damage to the biliary epithelium in most cases.",
"hepatitis A":"Hepatitis A is a highly contagious liver infection caused by the hepatitis A virus. The virus is one of several types of hepatitis viruses that cause inflammation and affect your liver's ability to function.",
"Osteoarthristis":"Osteoarthritis is the most common form of arthritis, affecting millions of people worldwide. It occurs when the protective cartilage that cushions the ends of your bones wears down over time.",
"(vertigo) Paroymsal Positional Vertigo":"Positional Vertigo	Benign paroxysmal positional vertigo (BPPV) is one of the most common causes of vertigo â€” the sudden sensation that you're spinning or that the inside of your head is spinning. Benign paroxysmal positional vertigo causes brief episodes of mild to intense dizziness.",
"Hypoglycemia":"Hypoglycemia is a condition in which your blood sugar (glucose) level is lower than normal. Glucose is your body's main energy source. Hypoglycemia is often related to diabetes treatment. But other drugs and a variety of conditions many rare can cause low blood sugar in people who don't have diabetes.",
"Acne":"Acne vulgaris is the formation of comedones, papules, pustules, nodules, and/or cysts as a result of obstruction and inflammation of pilosebaceous units (hair follicles and their accompanying sebaceous gland). Acne develops on the face and upper trunk. It most often affects adolescents.",
"Diabetes":"Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high. Blood glucose is your main source of energy and comes from the food you eat. Insulin, a hormone made by the pancreas, helps glucose from food get into your cells to be used for energy.",
"Impetigo":"Impetigo (im-puh-TIE-go) is a common and highly contagious skin infection that mainly affects infants and children. Impetigo usually appears as red sores on the face, especially around a child's nose and mouth, and on hands and feet. The sores burst and develop honey-colored crusts.",
"Hypertension":"Hypertension (HTN or HT), also known as high blood pressure (HBP), is a long-term medical condition in which the blood pressure in the arteries is persistently elevated. High blood pressure typically does not cause symptoms.",
"Peptic ulcer diseae":"Peptic ulcer disease (PUD) is a break in the inner lining of the stomach, the first part of the small intestine, or sometimes the lower esophagus. An ulcer in the stomach is called a gastric ulcer, while one in the first part of the intestines is a duodenal ulcer.",
"Dimorphic hemorrhoids(piles)":"Hemorrhoids, also spelled haemorrhoids, are vascular structures in the anal canal. Haemorrhoids, also known as piles, are swellings containing enlarged blood vessels that are found inside or around the bottom (the rectum and anus). In many cases, haemorrhoids don't cause symptoms, and some people don't even realise they have them.",
"Common Cold":"The common cold is a viral infection of your nose and throat (upper respiratory tract). It's usually harmless, although it might not feel that way. Many types of viruses can cause a common cold.",
"Chicken pox":"Chickenpox is a highly contagious disease caused by the varicella-zoster virus (VZV). It can cause an itchy, blister-like rash. The rash first appears on the chest, back, and face, and then spreads over the entire body, causing between 250 and 500 itchy blisters.",
"Cervical spondylosis":"Cervical spondylosis is a general term for age-related wear and tear affecting the spinal disks in your neck. As the disks dehydrate and shrink, signs of osteoarthritis develop, including bony projections along the edges of bones (bone spurs).",
"Hyperthyroidism":"Hyperthyroidism (overactive thyroid) occurs when your thyroid gland produces too much of the hormone thyroxine. Hyperthyroidism can accelerate your body's metabolism, causing unintentional weight loss and a rapid or irregular heartbeat.",
"Urinary tract infection":"An infection of the kidney, ureter, bladder, or urethra. Abbreviated UTI. Not everyone with a UTI has symptoms, but common symptoms include a frequent urge to urinate and pain or burning when urinating.",
"Varicoseveins":"A vein that has enlarged and twisted, often appearing as a bulging, blue blood vessel that is clearly visible through the skin. Varicose veins are most common in older adults, particularly women, and occur especially on the legs.",
"AIDS":"Acquired immunodeficiency syndrome (AIDS) is a chronic, potentially life-threatening condition caused by the human immunodeficiency virus (HIV). By damaging your immune system, HIV interferes with your body's ability to fight infection and disease.",
"Paralysis (brain hemorrhage)":"Intracerebral hemorrhage (ICH) is when blood suddenly bursts into brain tissue, causing damage to your brain. Symptoms usually appear suddenly during ICH. They include headache, weakness, confusion, and paralysis, particularly on one side of your body.",
"Typhoid":"An acute illness characterized by fever caused by infection with the bacterium Salmonella typhi. Typhoid fever has an insidious onset, with fever, headache, constipation, malaise, chills, and muscle pain. Diarrhea is uncommon, and vomiting is not usually severe.",
"Hepatitis B":"Hepatitis B is an infection of your liver. It can cause scarring of the organ, liver failure, and cancer. It can be fatal if it isn't treated. It's spread when people come in contact with the blood, open sores, or body fluids of someone who has the hepatitis B virus.",
"Fungal infection":"In humans, fungal infections occur when an invading fungus takes over an area of the body and is too much for the immune system to handle. Fungi can live in the air, soil, water, and plants. There are also some fungi that live naturally in the human body. Like many microbes, there are helpful fungi and harmful fungi.",
"Hepatitis C":"Inflammation of the liver due to the hepatitis C virus (HCV), which is usually spread via blood transfusion (rare), hemodialysis, and needle sticks. The damage hepatitis C does to the liver can lead to cirrhosis and its complications as well as cancer.",
"Migraine":"A migraine can cause severe throbbing pain or a pulsing sensation, usually on one side of the head. It's often accompanied by nausea, vomiting, and extreme sensitivity to light and sound. Migraine attacks can last for hours to days, and the pain can be so severe that it interferes with your daily activities.",
"Bronchial Asthma":"Bronchial asthma is a medical condition which causes the airway path of the lungs to swell and narrow. Due to this swelling, the air path produces excess mucus making it hard to breathe, which results in coughing, short breath, and wheezing. The disease is chronic and interferes with daily working.",
"Alcoholic hepatitis":"Alcoholic hepatitis is a diseased, inflammatory condition of the liver caused by heavy alcohol consumption over an extended period of time. It's also aggravated by binge drinking and ongoing alcohol use. If you develop this condition, you must stop drinking alcohol.",
"Jaundice":"Yellow staining of the skin and sclerae (the whites of the eyes) by abnormally high blood levels of the bile pigment bilirubin. The yellowing extends to other tissues and body fluids. Jaundice was once called the 'morbus regius' (the regal disease) in the belief that only the touch of a king could cure it.",
"Hepatitis E":"A rare form of liver inflammation caused by infection with the hepatitis E virus (HEV). It is transmitted via food or drink handled by an infected person or through infected water supplies in areas where fecal matter may get into the water. Hepatitis E does not cause chronic liver disease.",
"Dengue":"An acute infectious disease caused by a flavivirus (species Dengue virus of the genus Flavivirus), transmitted by aedes mosquitoes, and characterized by headache, severe joint pain, and a rash. It is also called as breakbone fever, dengue fever.",
"Hepatitis D":"Hepatitis D, also known as the hepatitis delta virus, is an infection that causes the liver to become inflamed. This swelling can impair liver function and cause long-term liver problems, including liver scarring and cancer. The condition is caused by the hepatitis D virus (HDV).",
"Heart attack":"The death of heart muscle due to the loss of blood supply. The loss of blood supply is usually caused by a complete blockage of a coronary artery, one of the arteries that supplies blood to the heart muscle.",
"Pneumonia":"Pneumonia is an infection in one or both lungs. Bacteria, viruses, and fungi cause it. The infection causes inflammation in the air sacs in your lungs, which are called alveoli. The alveoli fill with fluid or pus, making it difficult to breathe.",
"Arthritis":"Arthritis is the swelling and tenderness of one or more of your joints. The main symptoms of arthritis are joint pain and stiffness, which typically worsen with age. The most common types of arthritis are osteoarthritis and rheumatoid arthritis.",
"Gastroenteritis":"Gastroenteritis is an inflammation of the digestive tract, particularly the stomach, and large and small intestines. Viral and bacterial gastroenteritis are intestinal infections associated with symptoms of diarrhea , abdominal cramps, nausea , and vomiting .",
"Tuberculosis":"Tuberculosis (TB) is an infectious disease usually caused by Mycobacterium tuberculosis (MTB) bacteria. Tuberculosis generally affects the lungs, but can also affect other parts of the body. Most infections show no symptoms, in which case it is known as latent tuberculosis."
    }

    disease_precautions = {
        "Drug Reaction": "1. Stop irritation\n2. Consult nearest hospital\n3. Stop taking drug\n4. Follow up",
    "Malaria": "1. Consult nearest hospital\n2. Avoid oily food\n3. Avoid non-veg food\n4. Keep mosquitoes out",
    "Allergy": "1. Apply calamine\n2. Cover area with bandage\n3. Use ice to compress itching",
    "Hypothyroidism": "1. Reduce stress\n2. Exercise\n3. Eat healthy\n4. Get proper sleep",
    "Psoriasis": "1. Wash hands with warm soapy water\n2. Stop bleeding using pressure\n3. Consult doctor\n4. Salt baths",
    "GERD": "1. Avoid fatty spicy food\n2. Avoid lying down after eating\n3. Maintain healthy\n4. Weight exercise",
    "Chronic cholestasis": "1. Cold baths\n2. Anti-itch medicine\n3. Consult doctor\n4. Eat healthy",
    "hepatitis A": "1. Consult nearest hospital\n2. Wash hands through\n3. Avoid fatty spicy food\n4. Medication",
    "Osteoarthritis": "1. Acetaminophen\n2. Consult nearest hospital\n3. Follow up\n4. Salt baths",
    "(vertigo) Paroxysmal Positional Vertigo": "1. Lie down\n2. Avoid sudden change in body\n3. Avoid abrupt head movement\n4. Relax",
    "Hypoglycemia": "1. Lie down on side\n2. Check pulse\n3. Drink sugary drinks\n4. Consult doctor",
    "Acne": "1. Bath twice\n2. Avoid fatty spicy food\n3. Drink plenty of water\n4. Avoid too many products",
    "Diabetes": "1. Have a balanced diet\n2. Exercise\n3. Consult doctor\n4. Follow up",
    "Impetigo": "1. Soak affected area in warm water\n2. Use antibiotics\n3. Remove scabs with wet compressed cloth\n4. Consult doctor",
    "Hypertension": "1. Meditation\n2. Salt baths\n3. Reduce stress\n4. Get proper sleep",
    "Peptic ulcer disease": "1. Avoid fatty spicy food\n2. Consume probiotic food\n3. Eliminate milk\n4. Limit alcohol",
    "Dimorphic hemorrhoids(piles)": "1. Avoid fatty spicy food\n2. Consume witch hazel\n3. Warm bath with Epsom salt\n4. Consume aloe vera juice",
    "Common Cold": "1. Drink vitamin C-rich drinks\n2. Take vapor\n3. Avoid cold food\n4. Keep fever in check",
    "Chicken pox": "1. Use neem in bathing\n2. Consume neem leaves\n3. Take vaccine\n4. Avoid public places",
    "Cervical spondylosis": "1. Use a heating pad or cold pack\n2. Exercise\n3. Take OTC pain reliever\n4. Consult doctor",
    "Hyperthyroidism": "1. Eat healthy\n2. Massage\n3. Use lemon balm\n4. Take radioactive iodine treatment",
    "Urinary tract infection": "1. Drink plenty of water\n2. Increase vitamin C intake\n3. Drink cranberry juice\n4. Take probiotics",
    "Varicoseveins": "1. Lie down flat and raise the leg high\n2. Use ointments\n3. Use vein compression\n4. Don't stand still for long",
    "AIDS": "1. Avoid open cuts\n2. Wear PPE if possible\n3. Consult doctor\n4. Follow up",
    "Paralysis (brain hemorrhage)": "1. Massage\n2. Eat healthy\n3. Exercise\n4. Consult doctor",
    "Typhoid": "1. Eat high-calorie vegetables\n2. Antibiotic therapy\n3. Consult doctor\n4. Medication",
    "Hepatitis B": "1. Consult nearest hospital\n2. Vaccination\n3. Eat healthy\n4. Medication",
    "Fungal infection": "1. Bath twice\n2. Use Dettol or neem in bathing water\n3. Keep the infected area dry\n4. Use clean cloths",
    "Hepatitis C": "1. Consult nearest hospital\n2. Vaccination\n3. Eat healthy\n4. Medication",
    "Migraine": "1. Meditation\n2. Reduce stress\n3. Use polaroid glasses in the sun\n4. Consult doctor",
    "Bronchial Asthma": "1. Switch to loose clothing\n2. Take deep breaths\n3. Get away from triggers\n4. Seek help",
    "Alcoholic hepatitis": "1. Stop alcohol consumption\n2. Consult doctor\n3. Medication\n4. Follow up",
    "Jaundice": "1. Drink plenty of water\n2. Consume milk thistle\n3. Eat fruits and high-fiber food\n4. Medication",
    "Hepatitis E": "1. Stop alcohol consumption\n2. Rest\n3. Consult doctor\n4. Medication",
    "Dengue": "1. Drink papaya leaf juice\n2. Avoid fatty spicy food\n3. Keep mosquitoes away\n4. Keep hydrated",
    "Hepatitis D": "1. Consult doctor\n2. Medication\n3. Eat healthy\n4. Follow up",
    "Heart attack": "1. Call ambulance\n2. Chew or swallow aspirin\n3. Keep calm\n4. Do CPR",
    "Pneumonia": "1. Consult doctor\n2. Medication\n3. Rest\n4. Follow up",
    "Arthritis": "1. Exercise\n2. Use hot and cold therapy\n3. Try acupuncture\n4. Massage",
    "Gastroenteritis": "1. Stop eating solid food for a while\n2. Try taking small sips of water\n3. Rest\n4. Ease back into eating",
    "Tuberculosis": "1. Cover mouth\n2. Consult doctor\n3. Medication\n4. Rest"
        }

    disease_tablets = {
"Fungal infection":["Tropical Antifungal Creams","Efzole Dry Syrup", "Antifungal Shampoo"],
"Allergy":["Oral Antihistamines","Diphenhydramine","Nasal Corticosteroid sprays"],
"Bronchial Asthma":["Albuterol","Beclomethasone","Oral Corticosteroids"],
"AIDS":["Abacavir and Lamivudine(Brand Name:Epzicom) ","Tenofovir Alafenamide(Brand Name:Descovy) ","Integrase Inhibitors"],
"GERD":["Antacids","H2 Blockers","Prokinetics"]," cervical Spondylosis":["Acetaminophen","NSAIDs","NSAIDs"],
"Migraine":[" Acetaminophen "," Sumatriptan","Triptans"],
"Hypertension ":[" Not exist","Angiotensin Converting Enzyme (ACE) Inhibitors","Diuretics"],
"Gastroenteritis":["Oral Rehydration Solutions ","Oral Rehydration Solutions"," Antidiarrheal Medication "],
" Chronic Cholestasis":["Ursodeoxycholic Acid(UDCA) "," Nutritional Counselling "," Liver Transplant "],
" Peptic Ulcer Disease":["Protom Pump Inhibitors","Antacids","Antibiotics "],
" Diabetes":["Not exist "," Not exist","Tolbutamide"],
"Paralysis(Brain Hemorrhage)":["Speech Therapy "," Surgery","surgery "],
"Jaundice":[" Fluid Intake","Rest","Hydration "]," Malaria":["Chloroquine "," Primaquine","Coartem(High Dosage) "],
" Chicken Pox":["Calamine Lotion","Antipyretics","Hydration "],
"Dengue": ["Acetaminophen (Tylenol)", "Acetaminophen (Tylenol) or ibuprofen (Advil, Motrin)", "Acetaminophen (Tylenol) or ibuprofen (Advil, Motrin)"],
"Typhoid": ["Cefixime or Azithromycin", "Ciprofloxacin or Cefixime", "Ciprofloxacin"],
"Hepatitis A":[" Supportive Care","Avoid Alcohol","Acetaminophen(Tylenol) "],
" Hepatitis B":["Entecavir","Tenofovir disoproxil fumarate","Interferon-alpha"],
"Hepatitis C":["Ledipasvir/Sofosbuvir(Harvoni) "," Velpatasvir(Epclusa) "," Elbasvir/Grazoprevir(Zepatier) "],
" Hepatitis D":["Vaccination "," Antiviral Medication "," Vaccination "],
" Hepatitis E":["Vaccination "," Vaccination ", " Hospitalization"],
"Alcoholic Hepatitis ":[" Mental Health Support "," Abstinence "," Alcohol Cessation "],
" Tuberculosis ":["Isoniazid"," Anti-TB Regimen","Pyrazinamide"],
"Common Cold ":[" Acetaminophen "," Ibuprofen "," Decongestant "],
" Pneumonia ":[" Amoxicillin","Azithromycin "," Levofloxacin"],
"Dimorphic Hemorrhoids (piles) ":[" Witch Hazel Ointment "," Hydrocortisone "," Sclerotherapy"],
"Heart Attack":["Not Exist","Not Exist","Aspirin"],
"Varicose Veins":["Not Exist","Not Exist","Sclerotherapy "],
" Hypothyroidism ":[" Not Exist","Not Exist "," Levothyroxine"],
"Hyperthyroidism ":[" Methimazole","Propylthiouracil","Radiactive Iodine Therapy "],
" Hypoglycemia ":[" Consult Doctor "," Diazoxiode","Octreotide"],
"Osteoarthritis ":[" Acetaminophen "," Acetaminophen "," Corticosteroid Injection "],
" Arthritis ":[" Methotrexate","Methotrexate "," Hyaluronic Acid Injection "],
" Paroymsal Positional Vertigo":["Epley Maneuver","Epley Maneuver "," Semont Maneuver "],
" Acne":["Benzoyl Peroxide "," Doxycycline","Tropical Treatment (Retinoids) "],
"Urinary tract infection":["Amoxicillin "," Ciprofloxacin "," Nitrofurantoin"],
"Psoriasis":["Emollient Moisturizer "," Methotrexate "," Photo Therapy "],
"Impetigo": ["Mupirocin (brand name Bactroban)","Amoxicillin or Cephalexin","Amoxicillin or Cephalexin"],
    }


    st.markdown(f"<h5>Description for {disease_labels[predicted_disease]}:<h5>",unsafe_allow_html=True)
    if disease_labels[predicted_disease] in disease_descriptions:
        st.write(disease_descriptions[disease_labels[predicted_disease]])
    else:
        st.write("Description not found for this disease.")

    st.write(f"<h5>Precautions for {disease_labels[predicted_disease]}:<h5>",unsafe_allow_html=True)
    if disease_labels[predicted_disease] in disease_precautions:
        precautions = disease_precautions[disease_labels[predicted_disease]]
        precautions_list = precautions.split("\n")  # Split precautions into a list
        for step in precautions_list:
            st.write(step)
    else:
        st.write("Precautions not found for this disease.")

    age_index = -1
    if age >=  5 and age <= 11:
        age_index=0
    elif age > 11 and age <= 17:
        age_index = 1
    else:
        age_index = 2
 
    disease_name = disease_labels[predicted_disease]
    st.write(f"<h5> Medicines for {disease_name} (Age {age}):<h5>",unsafe_allow_html=True)
    if disease_name in disease_tablets:
        tablets = disease_tablets[disease_name][age_index]
        st.write(tablets)
    else:
        st.write(f"No information available for {disease_name}.")


        

            
        


    
            

        

   

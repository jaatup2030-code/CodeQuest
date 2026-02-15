# HazardReady: Personalized Disaster Risk & Preparedness Planner

## Project Overview
HazardReady is a **user-friendly web application** that helps families **prepare for natural hazards** such as typhoons, floods, earthquakes, landslides, and fires. The program generates a **personalized emergency plan** based on household factors, location, family composition, pets, and available resources. HazardReady provides **practical, actionable guidance** that is easy to follow, even for students and families with no technical background.

---

## Problem Statement
Existing disaster preparedness guides are often **too generic**, leaving families **underprepared** during emergencies. HazardReady addresses this by creating **customized checklists and emergency plans** tailored to each user’s unique situation.

---

## Project Objectives
HazardReady aims to:
1. Generate a **personalized emergency checklist** based on user inputs.  
2. Identify **household-specific hazards** based on location and home conditions.  
3. Provide a **family communication plan** and suggested evacuation strategies.  
4. Assess **household resources**, including go-bag contents, vehicles, and utilities.  
5. Offer **practical safety recommendations** to improve preparedness.  

---

## Key Features
- Personalized emergency checklist  
- Household hazard identification  
- Family communication plan generator  
- Go-bag readiness assessment  
- Resource evaluation (vehicles, electricity, water)  
- Disaster-specific guidance (typhoon, earthquake, flood, fire, landslide)  
- Printable emergency plan  

---
## Methodology

### Core Features Implementation
1. **User Input Collection**  
   - Collected through dropdowns and input fields in `index.html`.  
   - Inputs include house type, building condition, location type, family members, pets, special needs, vehicle availability, utilities, and optional disaster focus.

2. **Risk and Hazard Evaluation**  
   - Implemented in the `generatePlan()` JavaScript function.  
   - Uses conditional statements (IF-ELSE) to identify potential hazards based on house type, location, and household factors.  
   - Examples:  
     - Flood-prone area → Flooding risk  
     - Poor building condition → Structural instability risk  
     - Wood/lightweight house → Fire risk  

3. **Emergency Plan Generation**  
   - Dynamically generates a **customized checklist** with actionable tips.  
   - Includes household-specific recommendations, disaster-focused guidance, and responsibilities for family members.  
   - Special considerations for pets, infants, elderly, PWDs, and resource limitations (like no vehicle or limited utilities).

4. **Output Display and Printing**  
   - Results are shown in a dedicated `.result` div in real-time.  
   - Users can print the emergency plan using `window.print()`.  

---

### Technologies Used and Justification
- **HTML5** → Semantic structure for accessible and responsive forms.  
- **CSS3** → Clean and readable UI with gradient backgrounds, card layout, and print-friendly styles.  
- **JavaScript** → Dynamic logic for hazard assessment, checklist generation, and interactivity.  
- **Browser APIs** → `window.print()` enables printing without external libraries or server-side processing.  

**Justification:**  
We chose **client-side JavaScript** because it allows real-time personalized emergency plans without requiring a backend, keeping the app lightweight and user-friendly.

---

### Key Design Decisions and Trade-offs
- **Client-side only:** No database to avoid storing personal data → safer for privacy.  
- **Dynamic JS logic:** Easier to maintain and update hazard rules as needed.  
- **Print-friendly design:** Allows offline access, which is essential during disasters.  
- **Accessibility considerations:** High contrast colors, readable font sizes, and clear labels for all inputs.  

---

### Ethical Considerations
- **User Privacy:** No personal data is stored or transmitted.  
- **Accessibility:** UI is designed for clarity and readability for users of all ages and abilities.  
- **Intellectual Property:** Any open-source references or code snippets are properly credited.  
- **Safety & Responsibility:** All recommendations are general preparedness guidance and do not replace official disaster management instructions.

---

## Inputs
- **Type of House:** Wood, Concrete, Mixed, Apartment, Lightweight Structure  
- **Condition of Building:** Good, Average, Poor/Old  
- **Location Type:** Flood-Prone, Coastal, Urban, Rural, Hillside, Near Fault Line  
- **Number of Family Members**  
- **Presence of Pets**  
- **Presence of Elderly, Infants, or Persons with Disabilities (PWDs)**  
- **Vehicle Available for Evacuation**  
- **Access to Electricity and Water**  
- **Optional Disaster Focus:** Typhoon, Earthquake, Flood, Fire, Landslide  

---

## Outputs
- **Identified Risks** based on household and location  
- **Customized Emergency Preparedness Plan** with actionable tips  
- **Household Size** summary  
- **Printable Emergency Plan**  

---

## Logic Plan
1. **User Inputs:** Collected via web form.  
2. **Risk Evaluation:** Calculates hazards based on house type, location, and household factors.  
3. **Checklist Generation:** Recommends items, safety preparations, and family communication strategies.  
4. **Resource Assessment:** Evaluates go-bag readiness, vehicles, and utilities.  
5. **Outputs:** Displays hazards, emergency plan, and household info. Users can print the plan for reference.  

*A flowchart and pseudocode can be included in the project documentation.*

---

## Website Screenshot

![HazardReady Website](websitescreenshot)

---

## Contributors
- Atup  
- Cuevo  
- Escala

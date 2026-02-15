function generatePlan() {
    const house = document.getElementById("house").value;
    const condition = document.getElementById("condition").value;
    const location = document.getElementById("location").value;
    const family = parseInt(document.getElementById("family").value);
    const pets = document.getElementById("pets").value;
    const special = document.getElementById("special").value;
    const vehicle = document.getElementById("vehicle").value;
    const utilities = document.getElementById("utilities").value;
    const disaster = document.getElementById("disaster").value;

    let hazards = [];
    let checklist = ["Water", "Food", "First Aid Kit", "Flashlight", "Important Documents"];
    let tips = [];

    // Hazard evaluation
    if(location === "flood") hazards.push("Flooding");
    if(location === "coastal") hazards.push("Storm surge and strong winds");
    if(location === "hillside") hazards.push("Landslides");
    if(location === "nearFault") hazards.push("Earthquakes");
    if(house === "wood" || house === "light") hazards.push("Fire hazards");
    if(condition === "poor") hazards.push("Structural instability");

    // Checklist adjustments
    if(pets === "yes") checklist.push("Pet supplies");
    if(special === "yes") checklist.push("Medications / Special items");
    if(vehicle === "no") tips.push("Coordinate evacuation with neighbors or authorities.");
    if(utilities === "limited") tips.push("Prepare alternative lighting and water storage.");
    if(family >= 4) tips.push("Assign emergency responsibilities to family members.");
    if(disaster !== "") tips.unshift(`This emergency plan focuses on preparedness for ${disaster}.`);

    // Risk score
    let risk = "Low";
    if(hazards.length >= 3) risk = "High";
    else if(hazards.length === 2) risk = "Moderate";

    // Family communication
    let communication = "Prepare emergency contacts and evacuation plan.";

    // Output
    const outputDiv = document.getElementById("result");
    outputDiv.innerHTML = `
        <h3>Identified Risks</h3>
        <ul>${hazards.map(h => `<li>${h}</li>`).join("")}</ul>

        <h3>Emergency Preparedness Plan</h3>
        <ul>
            ${checklist.map(item => `<li>${item}</li>`).join("")}
            ${tips.map(item => `<li>${item}</li>`).join("")}
            <li>${communication}</li>
        </ul>

        <p><strong>Household Size:</strong> ${family}</p>
        <p><strong>Risk Score:</strong> ${risk}</p>
    `;
    document.getElementById("printBtn").style.display = "block";
    outputDiv.style.display = "block";
}

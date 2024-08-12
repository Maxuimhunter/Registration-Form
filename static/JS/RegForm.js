// First Section/Funtion used to print the data entered in the form at the bottom.
function runscript() {
    this.textContent = "Done";
    
    var firstName = document.getElementById("first-name").value;
    var secondName = document.getElementById("second-name").value;
    var familyName = document.getElementById("family-name").value;
    var age = document.getElementById("age").value;
    var dob = document.getElementById("dob").value;
    var gender = document.getElementById("gender").value;
    var dateTested = document.getElementById("date-tested").value;
    var hivStatus = document.querySelector('input[name="hiv-status"]:checked').value;

    var message = "<h2>Thank you " + firstName + " " + secondName + " " + familyName + " for your submission</h2>";
    message += "<h3><p>Please confirm the data below:</p></h3>";
    message += "<p>First Name:&ensp;" + firstName + "</p>";
    message += "<p>Second Name:&ensp;" + secondName + "</p>";
    message += "<p>Family Name:&ensp;" + familyName + "</p>";
    message += "<p>Age:&ensp;" + age + "</p>";
    message += "<p>Date of Birth:&ensp;" + dob + "</p>";
    message += "<p>Gender:&ensp;" + gender + "</p>";
    message += "<p>Date HIV Tested:&ensp;" + dateTested + "</p>";
    message += "<p>HIV Status:&ensp;" + hivStatus + "</p>";
    message += '<button id="confirmButton">Confirm</button>';

    document.getElementById("content").innerHTML = message;

    document.getElementById("confirmButton").onclick = function() {
        alert("Data confirmed!");
    };
}
 
// Second Section/Function will be used to Auto-Calculate the age of the person using the DOB column.
function calculateAge() {
    const birthdate = document.getElementById("dob").value;
    const birthdateObj = new Date(birthdate);
    
    const today = new Date();
    let age = today.getFullYear() - birthdateObj.getFullYear();
    const monthDifference = today.getMonth() - birthdateObj.getMonth();
    
    // Adjust age if the birthdate hasn't occurred yet this year
    if (monthDifference < 0 || (monthDifference === 0 && today.getDate() < birthdateObj.getDate())) {
        age--;
    }
    
    document.getElementById("age").value = age;
}
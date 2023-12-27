function setOfficeValue(officeValue) {
  // Set the office value in the hidden input field
  document.getElementById("selectedOffice").value = officeValue;

  // Store the value in a variable
  var selectedOffice = document.getElementById("selectedOffice").value;

  // Alert the stored value
  alert("Stored office value: " + selectedOffice);
}

function setrestrorantValue(restrorantValue) {
  // Set the restaurant value in the hidden input field
  document.getElementById("restrorant").value = restrorantValue;

  // Store the value in a variable
  var selectedRestrorant = document.getElementById("restrorant").value;

  // Alert the stored value
  alert("Stored restrorant value: " + selectedRestrorant);
}

// Function to submit the form with the selected office value
function submitForm() {
  // Trigger the form submission
  var purpose = document.getElementById("selectedOffice").submit();
  alert(purpose);
}

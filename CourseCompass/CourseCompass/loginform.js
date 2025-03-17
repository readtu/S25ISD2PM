function validateForm() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var errorMessage = '';

    // Check if the username is empty
    if (username == "") {
        errorMessage += "Please enter your email.\n";
    }

    // Check if the password is empty
    if (password == "") {
        errorMessage += "Please enter your password.\n";
    }

    // If there's an error, display the message and prevent form submission
    if (errorMessage != '') {
        alert(errorMessage);
        return false; // Prevent form submission
    }

    // If no errors, allow form submission
    return true;
}
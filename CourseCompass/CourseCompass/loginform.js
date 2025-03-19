function validateForm() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    //var errorMessage = 'Please enter your username and password.';

    var fakeUser = {
        username: "testuser",
        password: "test123"
    };

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
    //return true;

    if (username === fakeUser.username && password === fakeUser.password) {
        alert("Login successful! Redirecting...");
        window.location.href = "../home_page.html"; // Redirect to the homepage
        return true; // Prevent actual form submission for now
    } else {
        alert("Invalid username or password.");
        return false; // Prevent form submission
    }
}

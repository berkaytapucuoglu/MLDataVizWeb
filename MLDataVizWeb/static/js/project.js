let create_new_button = document.querySelector(".create_new_button");
let login_button = document.querySelector(".login_button");
let login_part = document.querySelector(".login_part");
let register_part = document.querySelector(".register_part");

create_new_button.addEventListener("click", create_new_button_click);
login_button.addEventListener("click", login_button_click);

function create_new_button_click() {
  login_part.classList.add("display_off");
  register_part.classList.remove("display_off");
}

function login_button_click() {
  register_part.classList.add("display_off");
  login_part.classList.remove("display_off");
}

document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.querySelector('#login-form');
    loginForm.addEventListener('submit', async function(event) {
        event.preventDefault();

        const formData = new FormData(loginForm);
        const username = formData.get('username');
        const password = formData.get('password');

        try {
            const response = await fetch('/login', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                const responseData = await response.json();
                const error = responseData.message;
                showError(error);
            } else {
                window.location.href = '/main_page';
            }
        } catch (error) {
            console.error('Error:', error);
        }
    });

    function showError(error) {
        const errorElement = document.querySelector('#error-message');
        errorElement.textContent = error;
        errorElement.style.display = 'block';
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const registerForm = document.querySelector('#register-form');
    registerForm.addEventListener('submit', async function(event) {
        event.preventDefault();

        const formData = new FormData(registerForm);
        const username = formData.get('username');
        const password = formData.get('password');

        try {
            const response = await fetch('/register', {
                method: 'POST',
                body: formData
            });

            const responseData = await response.json();

            if (!response.ok) {
                // Show warning message in case of error
                const error = responseData.message;
                showError(error);
            } else {
                // Show success message in case of successful registration
                const successMessage = responseData.message;
                showSuccess(successMessage);
            }
        } catch (error) {
            console.error('Error:', error);
        }
    });

    function showError(message) {
        const errorElement = document.querySelector('#register-error-message');
        errorElement.textContent = message;
        errorElement.style.display = 'block';
        const successElement = document.querySelector('#success-message');
        successElement.style.display = 'none';
    }

    function showSuccess(message) {
        const successElement = document.querySelector('#success-message');
        successElement.textContent = message;
        successElement.style.display = 'block';
        const errorElement = document.querySelector('#register-error-message');
        errorElement.style.display = 'none';
    }
});

// project.js

// Get exercise links
const exerciseLinks = document.querySelectorAll('.accordion_element a');

// Listen for click events on each exercise link
exerciseLinks.forEach(link => {
    link.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent the page from reloading
        const exerciseName = this.innerText; // Get the clicked exercise name
        // Fetch exercise results
        fetch(`/exercise_results?exercise=${exerciseName}`)
            .then(response => response.text())
            .then(data => {
                 // Display exercise results
                document.getElementById('exerciseResults').innerHTML = data;
            })
            .catch(error => console.error('Error:', error));
    });
});





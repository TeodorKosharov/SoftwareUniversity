import {updateNavi, updateSections} from "../app.js";

const registerForm = document.querySelector('#register-form');

async function onSubmit(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const email = formData.get('email');
    const password = formData.get('password');
    const repeat = formData.get('repeatPassword');
    event.target.reset();

    if (email === '' || password === '') {
        return alert('All fields are required!');
    }

    if (password !== repeat) {
        return alert('Passwords do not match!');
    }

    const response = await fetch('http://localhost:3030/users/register', {
        method: 'post', headers: {
            'content-type': 'application/json'
        }, body: JSON.stringify({email, password})
    });

    if (response.ok === false) {
        const error = await response.json();
        return alert(error.message);
    }

    const data = await response.json();
    sessionStorage.setItem('userData', JSON.stringify({email: data.email, id: data._id, token: data.accessToken}));
    updateNavi();
    updateSections('home-page', 'add-movie-button', 'movie');
    registerForm.removeEventListener('submit', onSubmit);
}

export async function register() {
    registerForm.addEventListener('submit', onSubmit);
}

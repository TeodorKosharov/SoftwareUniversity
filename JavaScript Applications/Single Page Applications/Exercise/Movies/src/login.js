import {updateNavi, updateSections} from "../app.js";

const loginForm = document.querySelector('#login-form');

async function onSubmit(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const email = formData.get('email');
    const password = formData.get('password');
    event.target.reset();

    if (email === '' || password === '') {
        return alert('All fields are required!');
    }

    const response = await fetch('http://localhost:3030/users/login', {
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
    loginForm.removeEventListener('submit', onSubmit);
}

export function login() {
    loginForm.addEventListener('submit', onSubmit);
}

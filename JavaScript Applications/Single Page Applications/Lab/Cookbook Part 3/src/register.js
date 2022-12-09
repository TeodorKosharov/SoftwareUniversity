import {highlightBtn, loadCatalog} from "./app.js";

export async function register(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const email = formData.get('email');
    const password = formData.get('password');
    const repeat = formData.get('rePass');

    if (email === '' || password === '') {
        return alert('All fields are required!');
    }

    if (password !== repeat) {
        return alert('Passwords do not match!');
    }

    const response = await fetch('http://localhost:3030/users/register', {
        method: 'post',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify({email, password})
    });

    if (response.ok === false) {
        const error = await response.json();
        return alert(error.message);
    }

    const data = await response.json();
    sessionStorage.setItem('authToken', data.accessToken);
    document.querySelector('main').innerHTML = '';
    highlightBtn('Catalog');
    loadCatalog();
}
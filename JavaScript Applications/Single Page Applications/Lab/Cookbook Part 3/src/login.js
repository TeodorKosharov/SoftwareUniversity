import {loadCatalog, highlightBtn} from "./app.js";

export async function login(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const email = formData.get('email');
    const password = formData.get('password');

    if (email === '' || password === '') {
        return alert('All fields are required!');
    }

    event.target.reset();

    const response = await fetch('http://localhost:3030/users/login', {
        method: 'post', headers: {
            'Content-Type': 'application/json'
        }, body: JSON.stringify({email, password})
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

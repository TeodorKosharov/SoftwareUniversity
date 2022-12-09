import {updateNavi} from "../app.js";
updateNavi();

document.getElementById('loginForm').addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const email = formData.get('email');
    const password = formData.get('password');
    event.target.reset();

    if (email === '' || password === '') {
        return alert('All fields are required!');
    }

    const response = await fetch('http://localhost:3030/users/login', {
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
    sessionStorage.setItem('userData', JSON.stringify({email: data.email, id: data._id, token: data.accessToken}));
    window.location.href = 'http://localhost:63342/JS%20Applications/Remote%20Data%20and%20Authentication/Exercise/Fisher%20Game/src/home.html';
});

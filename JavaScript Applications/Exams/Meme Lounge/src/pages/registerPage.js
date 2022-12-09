import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';
import {updateNavi} from "../app.js";

const registerTemplate = (onSubmit) => html`<section id="register">
    <form id="register-form" @submit="${onSubmit}">
        <div class="container">
            <h1>Register</h1>
            <label for="username">Username</label>
            <input id="username" type="text" placeholder="Enter Username" name="username">
            <label for="email">Email</label>
            <input id="email" type="text" placeholder="Enter Email" name="email">
            <label for="password">Password</label>
            <input id="password" type="password" placeholder="Enter Password" name="password">
            <label for="repeatPass">Repeat Password</label>
            <input id="repeatPass" type="password" placeholder="Repeat Password" name="repeatPass">
            <div class="gender">
                <input type="radio" name="gender" id="female" value="female">
                <label for="female">Female</label>
                <input type="radio" name="gender" id="male" value="male" checked>
                <label for="male">Male</label>
            </div>
            <input type="submit" class="registerbtn button" value="Register">
            <div class="container signin">
                <p>Already have an account?<a href="/login">Sign in</a>.</p>
            </div>
        </div>
    </form>
</section>`;

export function registering() {
    render(registerTemplate(onSubmit), document.querySelector('main'));
}

async function onSubmit(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const username = formData.get('username');
    const email = formData.get('email');
    const password = formData.get('password');
    const repeat = formData.get('repeatPass');
    const gender = formData.get('gender');
    event.target.reset();

    if (username === '' || password === '' || email === '') {
        return alert('Input field must not be empty!');
    }

    if (password !== repeat) {
        return alert('Passwords do not match!');
    }

    const response = await fetch('http://localhost:3030/users/register', {
        method: 'post', headers: {
            'content-type': 'application/json'
        }, body: JSON.stringify({username, email, password, gender})
    });

    if (response.ok === false) {
        const error = await response.json();
        return alert(error.message);
    }

    const data = await response.json();
    const userData = {
        id: data._id,
        username: data.username,
        email: data.email,
        gender: data.gender,
        token: data.accessToken
    };
    sessionStorage.setItem('userData', JSON.stringify(userData));
    updateNavi();
    page.redirect('/memes');
}

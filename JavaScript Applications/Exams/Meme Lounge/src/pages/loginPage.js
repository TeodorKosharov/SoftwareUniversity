import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';
import {updateNavi} from '../app.js';

const loginTemplate = (onSubmit) => html`
    <section id="login">
        <form id="login-form" @submit="${onSubmit}">
            <div class="container">
                <h1>Login</h1>
                <label for="email">Email</label>
                <input id="email" placeholder="Enter Email" name="email" type="text">
                <label for="password">Password</label>
                <input id="password" type="password" placeholder="Enter Password" name="password">
                <input type="submit" class="registerbtn button" value="Login">
                <div class="container signin">
                    <p>Dont have an account?<a href="/register">Sign up</a>.</p>
                </div>
            </div>
        </form>
    </section>
`;

export function logging() {
    render(loginTemplate(onSubmit), document.querySelector('main'));
}

async function onSubmit(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const email = formData.get('email').trim();
    const password = formData.get('password').trim();
    event.target.reset();

    if (password === '' || email === '') {
        return alert('Input field must not be empty!');
    }

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

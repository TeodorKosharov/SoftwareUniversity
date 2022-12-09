import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';
import {updateNavi} from "../app.js";

const registerTemplate = (onSubmit) => html`
    <section id="register-page" class="auth">
        <form id="register" @submit="${onSubmit}">
            <h1 class="title">Register</h1>

            <article class="input-group">
                <label for="register-email">Email: </label>
                <input type="email" id="register-email" name="email">
            </article>

            <article class="input-group">
                <label for="register-password">Password: </label>
                <input type="password" id="register-password" name="password">
            </article>

            <article class="input-group">
                <label for="repeat-password">Repeat Password: </label>
                <input type="password" id="repeat-password" name="repeatPassword">
            </article>

            <input type="submit" class="btn submit-btn" value="Register">
        </form>
    </section>
`;

export function registerPage() {
    render(registerTemplate(onSubmit), document.querySelector('main'));
}

async function onSubmit(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const email = formData.get('email').trim();
    const password = formData.get('password').trim();
    const repeat = formData.get('repeatPassword').trim();
    event.target.reset();

    if (password === '' || email === '') {
        return alert('Input field must not be empty!');
    }

    if (password !== repeat) {
        return alert('Passwords do not match!');
    }

    const response = await fetch('http://localhost:3030/users/register', {
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
        email: data.email,
        token: data.accessToken
    };
    sessionStorage.setItem('userData', JSON.stringify(userData));
    updateNavi();
    page.redirect('/dashboard');
}

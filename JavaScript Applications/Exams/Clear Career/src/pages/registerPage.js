import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';
import {updateNavi} from "../app.js";

const registerTemplate = (onSubmit) => html`
    <section id="register">
        <div class="form">
            <h2>Register</h2>
            <form class="login-form" @submit="${onSubmit}">
                <input
                        type="text"
                        name="email"
                        id="register-email"
                        placeholder="email"
                />
                <input
                        type="password"
                        name="password"
                        id="register-password"
                        placeholder="password"
                />
                <input
                        type="password"
                        name="re-password"
                        id="repeat-password"
                        placeholder="repeat password"
                />
                <button type="submit">register</button>
                <p class="message">Already registered? <a href="/login">Login</a></p>
            </form>
        </div>
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
    const repeat = formData.get('re-password').trim();
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

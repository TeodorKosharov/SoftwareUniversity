import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';
import {updateNavi} from "../app.js";

const loginTemplate = (onSubmit) => html`<section id="login">
    <div class="form">
        <h2>Login</h2>
        <form class="login-form" @submit="${onSubmit}">
            <input type="text" name="email" id="email" placeholder="email" />
            <input
                    type="password"
                    name="password"
                    id="password"
                    placeholder="password"
            />
            <button type="submit">login</button>
            <p class="message">
                Not registered? <a href="/register">Create an account</a>
            </p>
        </form>
    </div>
</section>`;

export function loginPage() {
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
        email: data.email,
        token: data.accessToken
    };
    sessionStorage.setItem('userData', JSON.stringify(userData));
    updateNavi();
    page.redirect('/dashboard');
}

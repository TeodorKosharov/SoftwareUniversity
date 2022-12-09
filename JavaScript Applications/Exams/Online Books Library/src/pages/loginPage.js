import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';
import {updateNavi} from '../app.js';

const loginTemplate = (onSubmit) => html`
    <section id="login-page" class="login">
        <form id="login-form" action="" method="" @submit="${onSubmit}">
            <fieldset>
                <legend>Login Form</legend>
                <p class="field">
                    <label for="email">Email</label>
                    <span class="input">
                            <input type="text" name="email" id="email" placeholder="Email">
                        </span>
                </p>
                <p class="field">
                    <label for="password">Password</label>
                    <span class="input">
                            <input type="password" name="password" id="password" placeholder="Password">
                        </span>
                </p>
                <input class="button submit" type="submit" value="Login">
            </fieldset>
        </form>
    </section>

`;

export function loginPage() {
    render(loginTemplate(onSubmit), document.querySelector('main'));

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
        page.redirect('/dashboard');
    }
}

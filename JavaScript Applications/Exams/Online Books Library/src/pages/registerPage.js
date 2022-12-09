import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';
import {updateNavi} from '../app.js';

const registerTemplate = (onSubmit) => html`
    <section id="register-page" class="register">
        <form id="register-form" action="" method="" @submit="${onSubmit}">
            <fieldset>
                <legend>Register Form</legend>
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
                <p class="field">
                    <label for="repeat-pass">Repeat Password</label>
                    <span class="input">
                            <input type="password" name="confirm-pass" id="repeat-pass" placeholder="Repeat Password">
                        </span>
                </p>
                <input class="button submit" type="submit" value="Register">
            </fieldset>
        </form>
    </section>

`;


export function registerPage() {
    render(registerTemplate(onSubmit), document.querySelector('main'));

    async function onSubmit(event) {
        event.preventDefault();
        const formData = new FormData(event.target);
        const email = formData.get('email').trim();
        const password = formData.get('password').trim();
        const repeat = formData.get('confirm-pass').trim();
        event.target.reset();

        if (password === '' || email === '' || repeat === '') {
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

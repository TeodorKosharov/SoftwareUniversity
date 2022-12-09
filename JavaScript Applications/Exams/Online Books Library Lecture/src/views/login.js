import {html} from '../../node_modules/lit-html/lit-html.js';
import {login} from "../api/api.js";

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

// Това е функцията за ъпдейтване на страницата при кликане на логин anchor-a
// Приема параметър context, който идва автоматично когато използваме функцията при метода page()

// За context-a, което всъщност е обект, сме закачили метода render() и така във функцията
// използваме метода като подаваме темплейта за логина. След това извличаме данните от формуляра
// и викаме функцията login(), която ни логва и след това ъпдейтваме страницата чрез метода
// updateUserNav(), който също е закачен за context обекта. Накрая редиректваме към началната страница
export function loginPage(context) {
    context.render(loginTemplate(onSubmit));

    async function onSubmit(event) {
        event.preventDefault();
        const formData = new FormData(event.target);

        const email = formData.get('email').trim();
        const password = formData.get('password').trim();

        if (email === '' || password === '') {
            return alert('Please, fill all fields!');
        }
        await login(email, password);
        context.updateUserNav();
        context.page.redirect('/');
    }
}
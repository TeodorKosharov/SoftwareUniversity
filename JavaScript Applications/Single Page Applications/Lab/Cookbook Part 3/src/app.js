import {login} from "./login.js";
import {register} from "./register.js";
import {create} from "./create.js";

async function getRecipes() {
    const response = await fetch('http://localhost:3030/data/recipes');
    const recipes = await response.json();

    return recipes;
}

async function getRecipeById(id) {
    const response = await fetch('http://localhost:3030/data/recipes/' + id);
    const recipe = await response.json();

    return recipe;
}

function createRecipePreview(recipe) {
    const result = e('article', {
        className: 'preview', onClick: toggleCard
    }, e('div', {className: 'title'}, e('h2', {}, recipe.name)), e('div', {className: 'small'}, e('img', {src: recipe.img})),);

    return result;

    async function toggleCard() {
        const fullRecipe = await getRecipeById(recipe._id);

        result.replaceWith(createRecipeCard(fullRecipe));
    }
}

function createRecipeCard(recipe) {
    const result = e('article', {}, e('h2', {}, recipe.name), e('div', {className: 'band'}, e('div', {className: 'thumb'}, e('img', {src: recipe.img})), e('div', {className: 'ingredients'}, e('h3', {}, 'Ingredients:'), e('ul', {}, recipe.ingredients.map(i => e('li', {}, i))),)), e('div', {className: 'description'}, e('h3', {}, 'Preparation:'), recipe.steps.map(s => e('p', {}, s))),);

    return result;
}

async function logout() {
    const response = await fetch('http://localhost:3030/users/logout', {
        method: 'get', headers: {
            'X-Authorization': sessionStorage.getItem('authToken')
        },
    });

    if (response.ok !== false) {
        sessionStorage.clear();
        window.location.href = 'http://localhost:63342/JS%20Applications/Single%20Page%20Applications/Lab/Cookbook%20Part%203/index.html?_ijt=b524udqebogk5ef1o022qe5p70&_ij_reload=RELOAD_ON_SAVE';
    } else {
        console.error(await response.json());
    }
}

window.addEventListener('load', loadCatalog);

// Loading catalog
export async function loadCatalog() {
    if (sessionStorage.getItem('authToken') !== null) {
        document.getElementById('user').style.display = 'inline-block';
        document.getElementById('logoutBtn').addEventListener('click', logout);
        document.getElementById('guest').style.display = 'none';
    } else {
        document.getElementById('guest').style.display = 'inline-block';
        document.getElementById('user').style.display = 'none';
    }

    const main = document.querySelector('main');

    const recipes = await getRecipes();
    const cards = recipes.map(createRecipePreview);

    // main.innerHTML = '';
    cards.forEach(c => main.appendChild(c));
}

// Login button
document.getElementById('login').addEventListener('click', () => {
    highlightBtn('Login');
    document.querySelector('main').innerHTML = `
    <article>
            <h2>Login</h2>
            <form>
                <label>E-mail: <input type="text" name="email"></label>
                <label>Password: <input type="password" name="password"></label>
                <input type="submit" value="Login">
            </form>
        </article>
    `;
    document.querySelector('form').addEventListener('submit', login);
});

// Register button
document.getElementById('register').addEventListener('click', () => {
    highlightBtn('Register');
    document.querySelector('main').innerHTML = `
    <article>
            <h2>Register</h2>
            <form>
                <label>E-mail: <input type="text" name="email"></label>
                <label>Password: <input type="password" name="password"></label>
                <label>Repeat: <input type="password" name="rePass"></label>
                <input type="submit" value="Register">
            </form>
        </article>
    `;
    document.querySelector('form').addEventListener('submit', register);

});

// Catalog button
document.getElementById('catalog').addEventListener('click', () => {
    highlightBtn('Catalog');
    document.querySelector('main').innerHTML = '';
    loadCatalog();
});

// Create button
document.getElementById('create').addEventListener('click', () => {
    highlightBtn('Create Recipe');
    document.querySelector('main').innerHTML = `
    <article>
            <h2>New Recipe</h2>
            <form>
                <label>Name: <input type="text" name="name" placeholder="Recipe name"></label>
                <label>Image: <input type="text" name="img" placeholder="Image URL"></label>
                <label class="ml">Ingredients: <textarea name="ingredients" placeholder="Enter ingredients on separate lines"></textarea></label>
                <label class="ml">Preparation: <textarea name="steps" placeholder="Enter preparation steps on separate lines"></textarea></label>
                <input type="submit" value="Create Recipe">
            </form>
        </article>
    `;
    document.querySelector('form').addEventListener('submit', create);
});

// Highlight clicked button
export function highlightBtn(button) {
    const buttons = Array.from(document.querySelectorAll('a'));
    buttons.forEach(btn => {
        if (btn.textContent === button) {
            btn.className = 'active';
        } else {
            btn.className = '';
        }
    });
}

function e(type, attributes, ...content) {
    const result = document.createElement(type);

    for (let [attr, value] of Object.entries(attributes || {})) {
        if (attr.substring(0, 2) == 'on') {
            result.addEventListener(attr.substring(2).toLocaleLowerCase(), value);
        } else {
            result[attr] = value;
        }
    }

    content = content.reduce((a, c) => a.concat(Array.isArray(c) ? c : [c]), []);

    content.forEach(e => {
        if (typeof e == 'string' || typeof e == 'number') {
            const node = document.createTextNode(e);
            result.appendChild(node);
        } else {
            result.appendChild(e);
        }
    });

    return result;
}

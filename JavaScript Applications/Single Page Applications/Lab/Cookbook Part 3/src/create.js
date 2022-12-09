import {highlightBtn, loadCatalog} from "./app.js";

export async function create(event) {
    event.preventDefault();
    const formData = new FormData(event.target);

    const name = formData.get('name');
    const img = formData.get('img');
    const ingredients = formData.get('ingredients');
    const steps = formData.get('steps');

    if (name === '' || img === '' || ingredients === '' || steps === '') {
        return alert('All fields are required!');
    }

    await fetch('http://localhost:3030/data/recipes', {
        method: 'post',
        headers: {
            'content-type': 'application/json',
            'x-authorization': sessionStorage.getItem('authToken')
        },
        body: JSON.stringify({name, img, ingredients, steps})
    });

    document.querySelector('main').innerHTML = '';
    highlightBtn('Catalog');
    loadCatalog();
}

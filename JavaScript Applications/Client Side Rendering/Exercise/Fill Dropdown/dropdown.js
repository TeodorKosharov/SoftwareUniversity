import {html, render} from "../../../node_modules/lit-html/lit-html.js";

async function addItem() {
    const inputText = document.getElementById('itemText');
    render(await getResult(), document.querySelector('#menu'));

    document.querySelector('form').addEventListener('submit', async (event) => {
        event.preventDefault();
        await fetch('http://localhost:3030/jsonstore/advanced/dropdown', {
            method: 'post',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({text: inputText.value})
        });
        render(await getResult(), document.querySelector('#menu'));
        inputText.value = '';
    });
}

await addItem();

function template(obj) {
    return html`
        <option value="${obj._id}">${obj.text}</option>
    `;
}

async function getResult() {
    const response = await fetch('http://localhost:3030/jsonstore/advanced/dropdown');
    const data = Object.entries(await response.json()).map(x => x[1]);
    return data.map(el => template(el));
}


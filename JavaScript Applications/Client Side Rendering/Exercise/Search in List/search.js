import {towns} from './towns.js';
import {html, render} from "../../../node_modules/lit-html/lit-html.js";

const townsDiv = document.getElementById('towns');
const searchBar = document.getElementById('searchText');
render(template(), townsDiv);

document.querySelector('button').addEventListener('click', () => {
    render(template(), townsDiv);
});

function template() {
    return html`
    <ul>
        ${towns.map(town => search(town))}
    </ul>
    `;
}

function search(town) {
    if (town.includes(searchBar.value) && searchBar.value !== '') return html`<li class="active">${town}</li>`;
    return html`<li>${town}</li>`;
}

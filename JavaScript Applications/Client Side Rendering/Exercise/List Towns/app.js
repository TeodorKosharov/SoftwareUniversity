import {html, render} from "../../../node_modules/lit-html/lit-html.js";

function template(cities) {
    return html`
        <ul>
            ${cities.map(city => html`
                <li>${city}</li>`)}
        </ul>
    `;
}

document.querySelector('.content').addEventListener('submit', (event) => {
    event.preventDefault();
    const root = document.getElementById('root');
    const input = document.getElementById('towns');
    const cities = input.value.split(', ');
    render(template(cities), root);
});

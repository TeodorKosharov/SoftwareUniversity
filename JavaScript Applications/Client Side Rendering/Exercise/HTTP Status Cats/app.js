import {cats} from "./catSeeder.js";
import {html, render} from "../../../node_modules/lit-html/lit-html.js";

function template(cat) {
    return html`
        <ul>
            <li>
                <img src="./images/${cat.imageLocation}.jpg" width="250" height="250" alt="Card image cap">
                <div class="info">
                    <button class="showBtn" @click="${showMore}">Show status code</button>
                    <div class="status" style="display: none" id="100">
                        <h4>Status Code: ${cat.statusCode}</h4>
                        <p>Continue</p>
                    </div>
                </div>
            </li>
        </ul>
    `;
}

function showMore(event) {
    const div = event.target.parentElement.querySelector('.status');
    if (div.style.display === 'none') div.style.display = 'block'; else div.style.display = 'none';
}

const result = cats.map(cat => template(cat));
render(result, document.getElementById('allCats'));

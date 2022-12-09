import {html, render} from '../../node_modules/lit-html/lit-html.js';

export async function dashboardPage() {
    const shoes = await (await fetch('http://localhost:3030/data/shoes?sortBy=_createdOn%20desc')).json();
    let dashboardTemplate;

    if (shoes.length > 0) {
        dashboardTemplate = html`
            <section id="dashboard">
                <h2>Collectibles</h2>
                <ul class="card-wrapper">
                    <!-- Display a li with information about every post (if any)-->
                    ${shoes.map(el => html`
                        <li class="card">
                            <img src="${el.imageUrl}" alt="travis" />
                            <p>
                                <strong>Brand: </strong><span class="brand">${el.brand}</span>
                            </p>
                            <p>
                                <strong>Model: </strong
                                ><span class="model">${el.model}</span>
                            </p>
                            <p><strong>Value:</strong><span class="value">${el.value}</span>$</p>
                            <a class="details-btn" href="/dashboard/${el._id}">Details</a>
                        </li>
                    `)}
                </ul>
            </section>
        `;
    } else {
        dashboardTemplate = html`
            <section id="dashboard">
                <h2>Collectibles</h2>
                <!-- Display an h2 if there are no posts -->
                <h2>There are no items added yet.</h2>
            </section>
        `;
    }

    render(dashboardTemplate, document.querySelector('main'));
}

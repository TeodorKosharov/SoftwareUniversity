import {html, render} from '../../node_modules/lit-html/lit-html.js';

export async function dashboardPage() {
    const offers = await (await fetch('http://localhost:3030/data/offers?sortBy=_createdOn%20desc')).json();
    let dashboardTemplate;

    if (offers.length > 0) {
        dashboardTemplate = (offers) => html`
            <section id="dashboard">
                <h2>Job Offers</h2>
                ${offers.map(offer => html`
                    <div class="offer">
                        <img src="${offer.imageUrl}" alt="example1"/>
                        <p>
                            <strong>Title: </strong><span class="title">${offer.title}</span>
                        </p>
                        <p><strong>Salary:</strong><span class="salary">${offer.salary}</span></p>
                        <a class="details-btn" href="/dashboard/${offer._id}">Details</a>
                    </div>
                `)}
            </section>
        `;
    } else {
        dashboardTemplate = (offers) => html`
            <section id="dashboard">
                <h2>Job Offers</h2>
                <!-- Display an h2 if there are no posts -->
                <h2>No offers yet.</h2>
            </section>
        `;
    }

    render(dashboardTemplate(offers), document.querySelector('main'));
}


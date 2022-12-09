import {html, render} from '../../node_modules/lit-html/lit-html.js';

export async function dashboardPage() {
    const pets = await (await fetch('http://localhost:3030/data/pets?sortBy=_createdOn%20desc&distinct=name')).json();
    let dashboardTemplate;

    if (pets.length > 0) {
        dashboardTemplate = html`
            <section id="dashboard">
                <h2 class="dashboard-title">Services for every animal</h2>
                <div class="animals-dashboard">
                    ${pets.map(pet => html`
                        <div class="animals-board">
                            <article class="service-img">
                                <img class="animal-image-cover" src="${pet.imageUrl}">
                            </article>
                            <h2 class="name">${pet.name}</h2>
                            <h3 class="breed">${pet.breed}</h3>
                            <div class="action">
                                <a class="btn" href="/dashboard/${pet._id}">Details</a>
                            </div>
                        </div>
                    `)}
                </div>
            </section>
        `;
    } else {
        dashboardTemplate = html`
            <section id="dashboard">
                <h2 class="dashboard-title">Services for every animal</h2>
                <div class="animals-dashboard">
                    <!--If there is no pets in dashboard-->
                    <div>
                        <p class="no-pets">No pets in dashboard</p>
                    </div>
                </div>
            </section>
        `;
    }

    render(dashboardTemplate, document.querySelector('main'));
}

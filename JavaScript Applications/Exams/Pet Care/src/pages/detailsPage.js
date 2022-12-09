import {html, render} from '../../node_modules/lit-html/lit-html.js';

export async function detailsPage(context) {
    const clickedPetId = context.params.id;
    const clickedPet = await (await fetch(`http://localhost:3030/data/pets/${clickedPetId}`)).json();
    let detailsTemplate;

    if (sessionStorage.userData !== undefined && JSON.parse(sessionStorage.userData).id === clickedPet._ownerId) {
        detailsTemplate = html`
            <section id="detailsPage">
                <div class="details">
                    <div class="animalPic">
                        <img src="${clickedPet.imageUrl}">
                    </div>
                    <div>
                        <div class="animalInfo">
                            <h1>Name: ${clickedPet.name}</h1>
                            <h3>Breed: ${clickedPet.breed}</h3>
                            <h4>Age: ${clickedPet.age}</h4>
                            <h4>Weight: ${clickedPet.weight}</h4>
                            <h4 class="donation">Donation: 0$</h4>
                        </div>
                        <!-- if there is no registered user, do not display div-->
                        <div class="actionBtn">
                            <!-- Only for registered user and creator of the pets-->
                            <a href="/edit/${clickedPet._id}" class="edit">Edit</a>
                            <a href="/delete/${clickedPet._id}" class="remove">Delete</a>
                        </div>
                    </div>
                </div>
            </section>

        `;
    } else {
        detailsTemplate = html`
            <section id="detailsPage">
                <div class="details">
                    <div class="animalPic">
                        <img src="${clickedPet.imageUrl}">
                    </div>
                    <div>
                        <div class="animalInfo">
                            <h1>Name: ${clickedPet.name}</h1>
                            <h3>Breed: ${clickedPet.breed}</h3>
                            <h4>Age: ${clickedPet.age}</h4>
                            <h4>Weight: ${clickedPet.weight}</h4>
                            <h4 class="donation">Donation: 0$</h4>
                        </div>
                    </div>
                </div>
            </section>
        `;
    }

    render(detailsTemplate, document.querySelector('main'));
}

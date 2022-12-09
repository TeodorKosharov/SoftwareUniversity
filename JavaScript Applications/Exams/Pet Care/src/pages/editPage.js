import {html, render} from '../../node_modules/lit-html/lit-html.js';

export async function editPage(context) {
    const clickedPetId = context.params.id;
    const clickedPet = await (await fetch(`http://localhost:3030/data/pets/${clickedPetId}`)).json();

    const editTemplate = (onSubmit) => html`
        <section id="editPage">
            <form class="editForm" @submit="${onSubmit}">
                <img src="${clickedPet.image}">
                <div>
                    <h2>Edit PetPal</h2>
                    <div class="name">
                        <label for="name">Name:</label>
                        <input name="name" id="name" type="text" value="${clickedPet.name}">
                    </div>
                    <div class="breed">
                        <label for="breed">Breed:</label>
                        <input name="breed" id="breed" type="text" value="${clickedPet.breed}">
                    </div>
                    <div class="Age">
                        <label for="age">Age:</label>
                        <input name="age" id="age" type="text" value="${clickedPet.age}">
                    </div>
                    <div class="weight">
                        <label for="weight">Weight:</label>
                        <input name="weight" id="weight" type="text" value="${clickedPet.weight}">
                    </div>
                    <div class="image">
                        <label for="image">Image:</label>
                        <input name="image" id="image" type="text" value="${clickedPet.image}">
                    </div>
                    <button class="btn" type="submit">Edit Pet</button>
                </div>
            </form>
        </section>
    `;

    render(editTemplate(onSubmit), document.querySelector('main'));

    async function onSubmit(event) {
        event.preventDefault();
        const formData = new FormData(event.target);
        const name = formData.get('name');
        const breed = formData.get('breed');
        const age = formData.get('age');
        const weight = formData.get('weight');
        const image = formData.get('image');

        if (name === '' || breed === '' || age === '' || weight === '' || image === '') {
            return alert('All fields are required!');
        }

        await fetch(`http://localhost:3030/data/pets/${clickedPetId}`, {
            method: 'put', headers: {
                'content-type': 'application/json', 'x-authorization': JSON.parse(sessionStorage.userData).token
            }, body: JSON.stringify({name, breed, age, weight, image})
        });
        page.redirect(`/dashboard/${clickedPetId}`);
    }
}

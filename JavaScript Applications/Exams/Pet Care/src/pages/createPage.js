import {html, render} from '../../node_modules/lit-html/lit-html.js';

export async function createPage() {
    const createTemplate = (onSubmit) => html`
        <section id="createPage">
            <form class="createForm" @submit="${onSubmit}">
                <img src="./images/cat-create.jpg">
                <div>
                    <h2>Create PetPal</h2>
                    <div class="name">
                        <label for="name">Name:</label>
                        <input name="name" id="name" type="text" placeholder="Max">
                    </div>
                    <div class="breed">
                        <label for="breed">Breed:</label>
                        <input name="breed" id="breed" type="text" placeholder="Shiba Inu">
                    </div>
                    <div class="Age">
                        <label for="age">Age:</label>
                        <input name="age" id="age" type="text" placeholder="2 years">
                    </div>
                    <div class="weight">
                        <label for="weight">Weight:</label>
                        <input name="weight" id="weight" type="text" placeholder="5kg">
                    </div>
                    <div class="image">
                        <label for="image">Image:</label>
                        <input name="image" id="image" type="text" placeholder="./image/dog.jpeg">
                    </div>
                    <button class="btn" type="submit">Create Pet</button>
                </div>
            </form>
        </section>
    `;
    render(createTemplate(onSubmit), document.querySelector('main'));

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

        await fetch('http://localhost:3030/data/pets', {
            method: 'post',
            headers: {
                'content-type': 'application/json',
                'x-authorization': JSON.parse(sessionStorage.userData).token
            },
            body: JSON.stringify({name, breed, age, weight, image})
        });
        page.redirect('/');
    }
}

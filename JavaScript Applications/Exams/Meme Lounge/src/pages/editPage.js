import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';

const editTemplate = (onSubmit, meme) => html`
    <section id="edit-meme">
        <form id="edit-form" @submit="${onSubmit}">
            <h1>Edit Meme</h1>
            <div class="container">
                <label for="title">Title</label>
                <input id="title" type="text" placeholder="Enter Title" name="title" value="${meme.title}">
                <label for="description">Description</label>
                <textarea id="description" placeholder="Enter Description"
                          name="description">${meme.description}</textarea>
                <label for="imageUrl">Image Url</label>
                <input id="imageUrl" type="text" placeholder="Enter Meme ImageUrl" name="imageUrl" value="${meme.imageUrl}">
                <input type="submit" class="registerbtn button" value="Edit Meme">
            </div>
        </form>
    </section>
`;

export async function editPage(context) {
    const chosenMemeId = context.params.id;
    const chosenMeme = await fetch(`http://localhost:3030/data/memes/${chosenMemeId}`);
    const chosenMemeData = await chosenMeme.json();
    console.log(context);
    console.log(context.params);

    render(editTemplate(onSubmit, chosenMemeData), document.querySelector('main'));

    async function onSubmit(event) {
        event.preventDefault();
        const formData = new FormData(event.target);
        const title = formData.get('title');
        const description = formData.get('description');
        const imageUrl = formData.get('imageUrl');

        if (title === '' || description === '' || imageUrl === '') {
            return alert('All fields are required!');
        }

        const data = {title, description, imageUrl: imageUrl};
        await fetch(`http://localhost:3030/data/memes/${chosenMemeId}`, {
            method: 'put',
            headers: {
                'content-type': 'application/json',
                'x-authorization': JSON.parse(sessionStorage.userData).token
            },
            body: JSON.stringify(data)
        });
        page.redirect(`/memes/${chosenMemeId}`);
        console.log(chosenMemeId);
        console.log(chosenMemeData._id);
    }
}

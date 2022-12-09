function solve() {

    const creatorField = document.getElementById('creator');
    const titleField = document.getElementById('title');
    const categoryField = document.getElementById('category');
    const contentField = document.getElementById('content');
    const createButton = document.querySelector('.btn');
    const postsSection = Array.from(document.querySelectorAll('section'))[1];
    const archiveSection = document.querySelector('.archive-section ol');

    createButton.addEventListener('click', creating);

    function creating(event) {
        event.preventDefault();
        const newArticle = document.createElement('article');
        newArticle.innerHTML = `
        <h1>${titleField.value}</h1>
        <p>Category:
            <strong>${categoryField.value}</strong>
        </p>
        <p>Creator:
            <strong>${creatorField.value}</strong>
        </p>
        <p>${contentField.value}</p>
        <div class="buttons">
            <button class="btn delete">Delete</button>
            <button class="btn archive">Archive</button>
        </div>
        `;
        postsSection.appendChild(newArticle);

        const [deleteButton, archiveButton] = Array.from(newArticle.querySelectorAll('button'));
        archiveButton.addEventListener('click', archiving);
        deleteButton.addEventListener('click', deleting);
    }

    function archiving(event) {
        const currentPost = event.target.parentElement.parentElement;
        const title = currentPost.querySelector('h1').textContent;
        const newItem = document.createElement('li');
        newItem.textContent = title;
        archiveSection.appendChild(newItem);
        currentPost.remove();
        const sortedItems = Array.from(archiveSection.children).sort((a, b) => a.textContent.localeCompare(b.textContent));
        sortedItems.forEach(x => archiveSection.appendChild(x));
    }

    function deleting(event) {
        event.target.parentElement.parentElement.remove();
    }
}

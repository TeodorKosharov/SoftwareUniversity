async function attachEvents() {
    const posts = Object.values(await (await fetch('http://localhost:3030/jsonstore/blog/posts')).json());
    const comments = Object.values(await (await fetch('http://localhost:3030/jsonstore/blog/comments')).json());
    const optionsMenu = document.getElementById('posts');
    const loadButton = document.getElementById('btnLoadPosts');
    const viewButton = document.getElementById('btnViewPost');
    const textArea = document.getElementById('post-body');
    const commentsArea = document.getElementById('post-comments');

    loadButton.addEventListener('click', loadPosts);

    viewButton.addEventListener('click', viewing);

    function loadPosts() {
        posts.forEach(post => {
            const newOption = document.createElement('option');
            newOption.setAttribute('value', post.id);
            newOption.textContent = post.title;
            optionsMenu.appendChild(newOption);
        });
        loadButton.removeEventListener('click', loadPosts);
    }

    async function viewing() {
        const options = Array.from(optionsMenu.children);
        const selectedOptionValue = optionsMenu.value;
        const data = options.filter(option => option.value === selectedOptionValue)[0];

        document.getElementById('post-title').textContent = data.textContent;
        textArea.textContent = '';
        commentsArea.innerHTML = '';

        for (const obj of posts) {
            if (obj.id === selectedOptionValue) {
                textArea.textContent += obj.body + ' '
            }
        }

        for (const value of comments) {
            if (value.postId === selectedOptionValue) {
                commentsArea.innerHTML += `<li>${value.text}</li>`;
            }
        }
    }
}

attachEvents();

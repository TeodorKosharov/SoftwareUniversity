window.addEventListener("load", solve);

function solve() {
    const titleField = document.getElementById('post-title');
    const categoryField = document.getElementById('post-category');
    const contentField = document.getElementById('post-content');
    const publishButton = document.getElementById('publish-btn');
    const reviewList = document.getElementById('review-list');
    const publishedList = document.getElementById('published-list');
    const clearButton = document.getElementById('clear-btn');

    publishButton.addEventListener('click', publish);
    clearButton.addEventListener('click', clear);

    function publish() {
        if (titleField.value !== '' && categoryField.value !== '' && contentField.value !== '') {
            const newLi = document.createElement('li');
            newLi.className = 'rpost';
            const newArticle = document.createElement('article');

            const h4 = document.createElement('h4');
            h4.textContent = titleField.value;

            const categoryPara = document.createElement('p');
            categoryPara.textContent = 'Category: ' + categoryField.value;

            const contentPara = document.createElement('p');
            contentPara.textContent = 'Content: ' + contentField.value;

            const editButton = document.createElement('button');
            editButton.className = 'action-btn edit';
            editButton.textContent = 'Edit';
            editButton.addEventListener('click', edit);

            const approveButton = document.createElement('button');
            approveButton.className = 'action-btn approve';
            approveButton.textContent = 'Approve';
            approveButton.addEventListener('click', approve);

            newArticle.appendChild(h4);
            newArticle.appendChild(categoryPara);
            newArticle.appendChild(contentPara);
            newLi.appendChild(newArticle);
            newLi.appendChild(editButton);
            newLi.appendChild(approveButton);
            reviewList.appendChild(newLi);
        }

        titleField.value = '';
        categoryField.value = '';
        contentField.value = '';
    }

    function edit(event) {
        const section = event.target.parentElement;
        section.remove();
        const article = section.querySelector('article');
        const [title, category, content] = Array.from(article.children);
        titleField.value = title.textContent;
        categoryField.value = category.textContent.replace('Category: ', '');
        contentField.value = content.textContent.replace('Content: ', '');
    }

    function approve(event) {
        const section = event.target.parentElement;
        section.parentElement.removeChild(section);
        const buttons = Array.from(section.querySelectorAll('button'));
        for (const button of buttons) section.removeChild(button);
        publishedList.appendChild(section);
    }

    function clear() {
        publishedList.innerHTML = '';
    }
}

function solve() {
    const addButton = document.getElementById('add');
    addButton.addEventListener('click', addArticle);

    const taskField = document.getElementById('task');
    const descriptionField = document.getElementById('description');
    const dateField = document.getElementById('date');

    const sections = Array.from(document.querySelectorAll('section'));
    const openSection = sections[1].children[1];
    const progressSection = sections[2].children[1];
    const completeSection = sections[3].children[1];

    function addArticle(event) {
        if (taskField.value === '' || descriptionField.value === '' || dateField.value === '') return '';

        event.preventDefault();
        const newArticle = document.createElement('article');

        const newTitle = document.createElement('h3');
        newTitle.textContent = taskField.value;

        const descriptionParagraph = document.createElement('p');
        descriptionParagraph.textContent = `Description: ${descriptionField.value}`;

        const dateParagraph = document.createElement('p');
        dateParagraph.textContent = `Due Date: ${dateField.value}`;

        const newDiv = document.createElement('div');
        newDiv.classList.add('flex');

        const startButton = document.createElement('button');
        startButton.textContent = 'Start';
        startButton.classList.add('green');

        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.classList.add('red');

        newDiv.appendChild(startButton);
        newDiv.appendChild(deleteButton);

        newArticle.appendChild(newTitle);
        newArticle.appendChild(descriptionParagraph);
        newArticle.appendChild(dateParagraph);
        newArticle.appendChild(newDiv);
        openSection.appendChild(newArticle);

        startButton.addEventListener('click', inProgress);
        deleteButton.addEventListener('click', deleteSection);

        taskField.value = '';
        descriptionField.value = '';
        dateField.value = '';
    }

    function deleteSection(event) {
        openSection.removeChild(event.target.parentElement.parentElement);
    }

    function deleteProgress(event) {
        progressSection.removeChild(event.target.parentElement.parentElement);
    }

    function inProgress(event) {
        const removedSection = event.target.parentElement.parentElement;
        openSection.removeChild(removedSection);
        progressSection.appendChild(removedSection);
        const [deleteButton, finishButton] = Array.from(removedSection.querySelectorAll('button'));

        deleteButton.textContent = 'Delete';
        deleteButton.classList.remove('green');
        deleteButton.classList.add('red');
        deleteButton.removeEventListener('click', inProgress);
        deleteButton.addEventListener('click', deleteProgress);

        finishButton.textContent = 'Finish';
        finishButton.classList.remove('red');
        finishButton.classList.add('orange');
        finishButton.removeEventListener('click', deleteSection);
        finishButton.addEventListener('click', finished);
    }

    function finished(event) {
        let removed = event.target.parentElement.parentElement;
        progressSection.removeChild(removed);
        const unnecessaryDiv = removed.children[3];
        removed.removeChild(unnecessaryDiv);
        completeSection.appendChild(removed);

    }
}

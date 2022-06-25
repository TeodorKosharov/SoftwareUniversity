function lockedProfile() {
    const buttons = document.getElementsByTagName('button');
    Array.from(buttons).forEach(x => x.addEventListener('click', action));

    function action(event) {
        const currentButton = event.target;
        const blockElements = currentButton.parentElement.children;
        const isLocked = Array.from(blockElements).filter(x => x.value === 'lock')[0].checked;
        const infoDiv = currentButton.parentElement.querySelector('div');

        if (!isLocked) {
            if (event.target.textContent === 'Show more') {
                infoDiv.style.display = 'block';
                event.target.textContent = 'Hide it';
            } else {
                infoDiv.style.display = 'none';
                event.target.textContent = 'Show more';
            }
        }
    }
}

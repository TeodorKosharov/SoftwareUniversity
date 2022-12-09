async function getInfo() {

    const baseUrl = 'http://localhost:3030/jsonstore/bus/businfo/';
    const inputElement = document.getElementById('stopId');
    const ulElement = document.getElementById('buses');
    const divElement = document.getElementById('stopName');
    const checkButton = document.getElementById('submit');

    try {
        divElement.textContent = 'Loading...';
        const result = await fetch(`${baseUrl}/${inputElement.value}`);

        if (result.status !== 200) {
            alert('Stop ID not found');
        }

        const data = await result.json();
        divElement.textContent = data.name;
        Object.entries(data.buses).forEach(bus => {
            const liElement = document.createElement('li');
            liElement.textContent = `Bus ${bus[0]} arrives in ${bus[1]} minutes`;
            ulElement.appendChild(liElement);
        });

    } catch (error) {
        divElement.textContent = 'Error';
    }


}
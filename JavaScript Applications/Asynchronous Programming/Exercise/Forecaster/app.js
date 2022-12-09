function attachEvents() {

    // weather symbols codes:
    const symbols = {
        'Sunny': '&#x2600', 'Partly sunny': '&#x26C5', 'Overcast': '&#x2601', 'Rain': '&#x2614', 'Degrees': '&#176'
    };

    function invalidData(section) {
        section.style.display = 'block';
        const infoDiv = document.getElementById('upcoming');
        infoDiv.style.display = 'none';
        infoDiv.children[0].style.display = 'none';
        section.querySelector('.label').textContent = 'Error';
    }

    const location = document.getElementById('location');
    const getWeatherButton = document.getElementById('submit');
    const forecastSection = document.getElementById('forecast');
    getWeatherButton.addEventListener('click', action);

    async function action() {
        if (location.value !== 'barcelona' && location.value !== 'ny' && location.value !== 'london') invalidData(forecastSection);

        document.getElementById('upcoming').style.display = 'block';

        const locationsUrl = `http://localhost:3030/jsonstore/forecaster/locations`;
        const locationsResponse = await fetch(locationsUrl);
        if (locationsResponse.status !== 200) invalidData(forecastSection);
        const data = await locationsResponse.json();

        const chosenLocation = data.filter(obj => obj.code === location.value)[0];
        const chosenLocationUrl = `http://localhost:3030/jsonstore/forecaster/today/${chosenLocation.code}`;
        const chosenLocationResponse = await fetch(chosenLocationUrl);
        if (chosenLocationResponse.status !== 200) invalidData(forecastSection);
        const chosenLocationData = await chosenLocationResponse.json();

        const chosenLocationForecastUrl = `http://localhost:3030/jsonstore/forecaster/upcoming/${chosenLocation.code}`;
        const chosenLocationForecastResponse = await fetch(chosenLocationForecastUrl);
        const chosenLocationForecastData = await chosenLocationForecastResponse.json();

        forecastSection.style.display = 'block';
        document.getElementById('current').innerHTML = `
        <div class="label">Current conditions</div>
        <div class="forecasts">
            <span class="condition symbol">${symbols[chosenLocationData.forecast.condition]}</span>
            <span class="condition">
                <span class="forecast-data">${chosenLocationData.name}</span>
                <span class="forecast-data">${chosenLocationData.forecast.low}${symbols['Degrees']}/${chosenLocationData.forecast.high}${symbols['Degrees']}</span>
                <span class="forecast-data">${chosenLocationData.forecast.condition}</span>
            </span>
        </div>
        `;
        document.getElementById('upcoming').innerHTML = `
        <div class="label">Three-day forecast</div>
        <div class="forecast-info">
            <span class="upcoming">
                <span class="symbol">${symbols[chosenLocationForecastData.forecast[0].condition]}</span>
                <span class="forecast-data">${chosenLocationForecastData.forecast[0].low}${symbols['Degrees']}/${chosenLocationForecastData.forecast[0].high}${symbols['Degrees']}</span>
                <span class="forecast-data">${chosenLocationForecastData.forecast[0].condition}</span>
            </span>
            <span class="upcoming">
                <span class="symbol">${symbols[chosenLocationForecastData.forecast[1].condition]}</span>
                <span class="forecast-data">${chosenLocationForecastData.forecast[1].low}${symbols['Degrees']}/${chosenLocationForecastData.forecast[0].high}${symbols['Degrees']}</span>
                <span class="forecast-data">${chosenLocationForecastData.forecast[1].condition}</span>
            </span>
            <span class="upcoming">
                <span class="symbol">${symbols[chosenLocationForecastData.forecast[2].condition]}</span>
                <span class="forecast-data">${chosenLocationForecastData.forecast[2].low}${symbols['Degrees']}/${chosenLocationForecastData.forecast[0].high}${symbols['Degrees']}</span>
                <span class="forecast-data">${chosenLocationForecastData.forecast[2].condition}</span>
            </span>
        </div>
        `;
    }
}

attachEvents();
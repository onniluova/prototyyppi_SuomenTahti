'use strict'
const map = L.map('map', { click: false });
L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
  maxZoom: 20,
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
}).addTo(map);
map.setView([63, 24], 5.5);


async function getData(url) {
    const response = await fetch(url);
    if(!response.ok) throw new Error('invalid server input');
    const data = await response.json();
    return data
}
async function statusData() {
    try {
        const status = await getData('http://127.0.0.1:5000/getStatus');
        document.getElementById('money').textContent = `$ ${status.rahat}`;
        document.getElementById('fuel').textContent = `${status.polttoaine}%`;
        document.getElementById('climate-points').textContent = status.ilmastopisteet;
        document.getElementById('current-location').textContent = status.nykyinenSijainti

    }catch (error) {
        console.error(error)
    }
    return status
}

async function tankkaus() {
    try {
        const status = await getData('http://127.0.0.1:5000/tankkaustiedot');
        document.getElementById('money').textContent = `$ ${status.rahat}`;
        document.getElementById('fuel').textContent = `${status.polttoaine}%`;
        document.getElementById('climate-points').textContent = status.ilmastopisteet;
        haeMahdolliset()
    } catch (error) {
        console.error(error);
    }
    // No need to return status if you're not using it after calling tankkaus
}

// Ensure your DOM is loaded before attaching event listeners
document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('tankkausButton').addEventListener('click', async function() {
        await tankkaus();
    });
});

document.getElementById('tankkausButton').addEventListener('click', async function() {
    await tankkaus();
});

let selectedAirportId = null;

// Pää funktio
async function gameSetup() {
    try {
        const start = await getData('http://127.0.0.1:5000/luoPeli');
        const gameData = await getData('http://127.0.0.1:5000/haeMahdolliset');

        for (let airportId in gameData) {
            const { nimi, latitude, longitude } = gameData[airportId];
            const marker = L.marker([latitude, longitude]).addTo(map);
            marker.bindPopup(`${nimi}`);

            // Add click event listener to marker
            marker.on('click', function() {
                selectedAirportId = airportId;
                // You can also update the UI to show the selected airport
            });
        }
    } catch (error) {
        console.log(error);
    }
}

async function haeMahdolliset() {
    try {
        const gameData = await getData('http://127.0.0.1:5000/haeMahdolliset');

        for (let airportId in gameData) {
            const { nimi, latitude, longitude } = gameData[airportId];
            const marker = L.marker([latitude, longitude]).addTo(map);
            marker.bindPopup(`${nimi}`);

            // Add click event listener to marker
            marker.on('click', function() {
                selectedAirportId = airportId;
                // You can also update the UI to show the selected airport
            });
        }
    } catch (error) {
        console.log(error);
    }
}

// Function to handle "siirry" button click
async function onSiirryButtonClick() {
    if (selectedAirportId) {
        try {
            const newStatus = await getData(`http://127.0.0.1:5000/siirry/${selectedAirportId}`);
            // Update the UI with the new game status
            statusData();
            haeMahdolliset();

            alert(`You have arrived in ${newStatus.nykyinenSijainti}`);
        } catch (error) {
            console.error(error);
        }
    } else {
        alert("Please select an airport first.");
    }
}

// Attach the click event handler to the "siirry" button
document.getElementById('siirryButton').addEventListener('click', onSiirryButtonClick);

gameSetup();
statusData();
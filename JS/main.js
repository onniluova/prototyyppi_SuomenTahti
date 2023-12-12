'use strict'

// Alustetaan kartta
const map = L.map('map', { click: false });
L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
  maxZoom: 20,
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
}).addTo(map);
map.setView([63, 24], 5.5);

// Funktio joka hakee datan
async function getData(url) {
    const response = await fetch(url);
    if(!response.ok) throw new Error('invalid server input');
    const data = await response.json();
    return data
}

// Funktio joka hakee status datan
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

// Funktio joka tankkaa
async function tankkaus() {
    try {
        const status = await getData('http://127.0.0.1:5000/tankkaustiedot');
        document.getElementById('money').textContent = `$ ${status.rahat}`;
        document.getElementById('fuel').textContent = `${status.polttoaine}%`;
        document.getElementById('climate-points').textContent = status.ilmastopisteet;
        await haeMahdolliset();
        alert("Tankkaus valmis.");
    } catch (error) {
        console.error(error);
    }
}

// Funktio lisää tankkaus napille event listenerin
document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('tankkausButton').addEventListener('click', async function() {
        await tankkaus();
    });
});

let selectedAirportId = null;

// Funktio luo pelin
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

// Funktio hakee mahdolliset lentokentät
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
                haeSää(selectedAirportId);
                // You can also update the UI to show the selected airport
            });
        }
    } catch (error) {
        console.log(error);
    }
}

async function noppa() {
    try {
        const status = await getData('http://127.0.0.1:5000/noppa');
        document.getElementById('money').textContent = `$ ${status.rahat}`;
        document.getElementById('fuel').textContent = `${status.polttoaine}%`;
        document.getElementById(
            'climate-points').textContent = status.ilmastopisteet;
        alert(status.message);
    } catch (error) {
        console.error(error);
    }
}

// Funktio siirtyy lentokentälle
async function onSiirryButtonClick() {
    if (selectedAirportId) {
        try {
            const newStatus = await getData(`http://127.0.0.1:5000/siirry/${selectedAirportId}`);
            // Update the UI with the new game status
            await statusData();
            await haeMahdolliset();

            alert(`You have arrived in ${newStatus.nykyinenSijainti}`);
            await noppa();
            await tarkistaLentokenttä(newStatus.nykyinenSijainti);
        } catch (error) {
            console.error(error);
        }
    } else {
        alert("Please select an airport first.");
    }
}

async function haeSää(airportId) {
    try {
        const weatherStatus = await getData(`http://127.0.0.1:5000/haeSaatiedot/${airportId}`);
        document.getElementById('weather-info').textContent = `Weather: ${weatherStatus.description}, Temp: ${weatherStatus.temperature.toFixed(1)}°C`;
    }
    catch (error) {
        console.error(error);
    }
}

// Funktio tarkistaa onko lentokenttä Rovaniemellä
async function tarkistaLentokenttä(nykyinenSijainti) {
    if (nykyinenSijainti === "Rovaniemi") {
        const status = await getData('http://127.0.0.1:5000/getStatus');
        document.getElementById('climate-points').textContent = status.ilmastopisteet;

        alert("You have arrived in Rovaniemi! Congratulations!" + "\n" +
            "Ilmastopisteesi: " + status.ilmastopisteet);
    }
}

// Funktio lisää siirry napille event listenerin
document.getElementById('siirryButton').addEventListener('click', onSiirryButtonClick);

gameSetup();
statusData();
haeSää("EFMA");
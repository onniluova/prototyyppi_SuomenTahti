'use strict'
const map = L.map('map', { tap: false });
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

async function gameSetup() {
    try {
        const gameData = await getData('http://127.0.0.1:5000/luoPeli');

        console.log(gameData)
    }catch (error) {
        console.log(error)
    }
}


gameSetup()
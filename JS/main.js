'use strict'

async function gameSetup () {
    try {
        const response = await fetch('http://127.0.0.1:5000');
        const data = await response.json();
        console.log(data);
    } catch (error){
        console.log(error);
    }

}

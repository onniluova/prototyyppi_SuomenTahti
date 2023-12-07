'use strict'

async function gameSetup () {
    try {
        const response = await fetch(url);
        const data = await response.json();
        console.log(data);
    } catch (error){
        console.log(error);
    }

}

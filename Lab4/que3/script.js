const paragraph1 = document.getElementById('paragraph1');
const paragraph2 = document.getElementById('paragraph2');
const paragraph3 = document.getElementById('paragraph3');

const paragraph1_height = paragraph1.clientHeight;
const paragraph2_height = paragraph2.clientHeight;
const paragraph3_height = paragraph3.clientHeight;

const window_height = window.innerHeight;

paragraph1.style.top = `${window_height/2 - 3*paragraph1_height}px`;

paragraph2.style.top = `${window_height/2 - 3*paragraph2_height}px`;

paragraph3.style.top = `${window_height/2 - 3*paragraph3_height}px`;

window.addEventListener('resize', () => {
    paragraph1.style.top = `${window.innerHeight/2 - 3.5*paragraph1_height}px`;
    paragraph2.style.top = `${window.innerHeight/2 - 2.6*paragraph2_height}px`;
    paragraph3.style.top = `${window.innerHeight/2 - 2*paragraph3_height}px`;
});

const list = document.querySelector('.list')
for(let i =0;i<10;i++){
    const elem = document.createElement('li');
    elem.textContent = `Bangali ${i+1}`
    list.appendChild(elem)
    elem.addEventListener('click',(e)=>{
        elem.style.color = 'red'
    })
}
const ramesh = document.querySelector('.ramesh')
const age = [17,18,19,20];
age.forEach((age,index)=>{
    const row = document.createElement('tr');
    row.innerHTML = `<td>${index+1}</td><td>${age}</td>`
    ramesh.appendChild(row)
})


const form = document.getElementById('form')
const nameInput = document.getElementById('name')
const genders = document.getElementsByName('gender')
const interests = document.getElementsByName('interests');
const cement = document.getElementById('cement')
form.addEventListener('submit',(eve)=>{
    eve.preventDefault();
    console.log(nameInput.value)
    genders.forEach((gender,index)=>{
        if(gender.checked===true)
            console.log(gender.value)
    })
    interests.forEach((interest,index)=>{
        if(interest.checked==true)
            console.log(interest.value)
    })
    console.log(cement.value)
})
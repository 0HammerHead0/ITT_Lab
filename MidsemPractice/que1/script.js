console.log("hell")
let studentCount = prompt("How many students do you want ?")
const table = document.createElement('table');
table.innerHTML='<thead><tr><th>ID</th><th>Name</th><th>Marks</th></tr></thead>'
table.border = 1
document.body.appendChild(table)
if(isNaN(parseInt(studentCount))){
    alert("Please enter an integer")
}
else{
    alert(`Your number entered is ${parseInt(studentCount)}`)
    for(let i =0;i<parseInt(studentCount);i++){
        const name = prompt(`Enter the name of the student ${i+1}`);
        const marks = prompt(`Enter marks for student ${i+1}`);
        const row = document.createElement('tr');
        row.innerHTML = `<td>${i+1}</td><td>${name}</td><td>${marks}</td>`;
        table.appendChild(row);
        
    }
}
const inputTag = document.createElement('input');
inputTag.id = 'name';
const inputTag2 = document.createElement('input');
inputTag2.id = 'marks';
const row = document.createElement('tr');
const td1= document.createElement('td')
td1.appendChild(inputTag)
const td2 = document.createElement('td');
td2.appendChild(inputTag2)
row.appendChild(td1)
row.appendChild(td2)
table.appendChild(row)


inputTag.addEventListener('keydown',(e)=>{
    console.log(e.key)
})
inputTag.addEventListener('submit',(e)=>{
    console.log("submit")
})

const frameset = document.createElement('frameset');
frameset.rows="100,100,*,100,100";
frameset.border = 1
for(let i =0;i<=4;i++){
    const frame = document.createElement('frame');
    frame.src = "ramesh.html";
    frameset.appendChild(frame)
}
// document.body.appendChild(frameset)
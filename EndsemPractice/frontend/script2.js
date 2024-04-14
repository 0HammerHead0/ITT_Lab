
const storedObj = JSON.parse(window.localStorage.getItem("obj"));
const sweets = document.getElementsByName('sweets')
const toothpastes = document.getElementsByName('toothpaste');
const nickname = document.getElementById('nickname')
const helloji = document.getElementById('helloji')
const submit = document.getElementById('submit')
const date = document.getElementById('date');
console.log(storedObj);
nickname.innerHTML = storedObj['nickname']
nickname.style.fontSize = '30px'
helloji.style.fontSize = '20px'
const result = {}

submit.addEventListener('click',(e)=>{
    e.preventDefault();
    let flag=false;
    sweets.forEach((sweet)=>{
        if(sweet.checked){
            flag=true;
            result['sweet']=sweet.value
        }
    })
    result['tp']=[]
    toothpastes.forEach((tp)=>{
        if(tp.checked){
            flag=true;
            result['tp'].push(tp.value)
        }
    })
    const inpDate = date.value;
    console.log(inpDate)
    console.log(parseInt(inpDate.slice(0,4)),parseInt(inpDate.slice(5,7)),parseInt(inpDate.slice(8,10)))
    if(parseInt(inpDate.slice(0,4))>=new Date().getFullYear() && parseInt(inpDate.slice(5,7))>=new Date().getMonth() +1 && parseInt(inpDate.slice(8,10))>=new Date().getDate()){

        if(!flag){
            alert('you left all fields blank')
        }
        else{
            result['date']=inpDate
            const result_ = document.getElementById('result');
            result_.innerHTML=''
            const table = document.createElement('table')
            let data=`
                <tr><th>Item</th><th>Value</th></tr>
                <tr><td>Poison</td><td>${result['sweet']}</td></tr>
            `
            result['tp'].forEach((e,i)=>{
                data+=`
                <tr><td>TP${i}</td><td>${e}</td></tr>
                `
            })
            data+=`
            <tr><td>Date</td><td>${result['date']}</td></tr>
            `
            table.innerHTML=data
            result_.appendChild(table)
        }
    }else{
        alert('Old Date')
    }
})
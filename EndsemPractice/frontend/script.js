const obj ={}
const submit = document.getElementById('submit');
submit.addEventListener('click', (e)=>{
    e.preventDefault();
    obj['username'] = document.getElementById('username').value;
    obj['pass'] = document.getElementById("pass").value;
    if(obj['username']=='' || obj['pass']==''){
        alert('Some fields might be empty!')
    }
    else if(obj['pass']!='pass'){
        alert('Password is wrong!')
    }
    else{
        obj['nickname'] = prompt('Please enter your nickname')
    }
    window.localStorage.setItem("obj", JSON.stringify(obj).toString());
    console.log(JSON.stringify(obj).toString())
    window.location.href = './index2.html'

})
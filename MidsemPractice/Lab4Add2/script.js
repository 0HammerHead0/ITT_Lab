console.log("hell")
document.addEventListener('click',(e)=>{
    if(e.shiftKey)
        alert("Shift key")
    else if(e.ctrlKey)
        alert(e.target.id + e.target.innerHTML)
})
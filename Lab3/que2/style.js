const text = document.getElementById("input");
const output = document.getElementById("output");
output.style.width = text.offsetWidth+'px';

function convert(){
    let words=text.value.split(' ');
    let res='';
    words.forEach((word)=>{
        firstChar = word[0];
        let newWord = word.slice(1,word.length)
        if()
            newWord+=firstChar+'ay';
            res+=newWord+' ';
    })
    output.innerHTML=res
}
text.addEventListener('input',(event)=>{
    convert();
})
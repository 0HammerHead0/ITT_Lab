const text = document.getElementById("input");
const output = document.getElementById("output");
output.style.width = text.offsetWidth+'px';

function convert(){
    let words=text.value.split(' ');
    let res='Nothing here yet';
    console.log(words)
    if(text.value!=''){
        res='';
        words.forEach((word)=>{
            if(word!=''){
                firstChar = word[0];
                let newWord = word.slice(1,word.length)
                newWord+=firstChar+'ay';
                res+=newWord+' ';
            }
        })
    }
    output.innerHTML=res
}
text.addEventListener('input',(event)=>{
    convert();
})
console.log("helo")
const input = document.getElementById('input');
const input_content = document.getElementById("input-content");
const output1 = document.getElementById("output1")
var input_num ;
input.addEventListener('submit',(e)=>{
    e.preventDefault();
})
input_content.addEventListener('keypress',(event)=>{
    if(event.key=="Enter"){
        const inp = event.target.value;
        if(!isNaN(parseInt(inp))){
            output1.innerHTML = String(event.target.value).split('').reverse().join('');
        }
        else{
            var inputString = event.target.value;
            for (var index = 0; index < inputString.length; index++) {
                var e = inputString[index];
                if (e == 'a' || e == 'A' || e == 'e' || e == 'E' || e == 'i' || e == 'i' || e == 'I' || e == 'O' || e == 'o' || e == 'u' || e == 'U') {
                    output1.innerHTML = "Position of first vowel (" + e + ") is " + String(index);
                    break;
                }
            }
        }
    }
})
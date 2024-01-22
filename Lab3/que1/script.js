const text = document.querySelector(".text");
let curSize = 5;
function loopingFunction(){
    loopPromise().then(loopingFunction);
}
const loopPromise = ()=>{
    return new Promise((resolve) =>{
        const bigger = setInterval( ()=>{
            curSize +=1;
            if(curSize == 50){
                const smaller = setInterval( ()=>{
                    curSize -=1;
                    if(curSize == 5){
                        clearInterval(smaller);
                        bigger();
                    }
                    text.style.fontSize = `${curSize}pt`;
                    text.style.color = 'blue';
                    text.textContent = 'Text-Shrinking';
                },100)
                clearInterval(bigger);
            }
            text.style.fontSize = `${curSize}pt`;
            text.style.color = 'red';
            text.textContent = 'Text-Growing';
        },100)
    })
}

loopingFunction();
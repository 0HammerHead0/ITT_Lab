console.log("helo")
const input = document.getElementById('input');
const input_content = document.getElementById("input-content");
const output1 = document.getElementById("output1")
const output2 = document.getElementById("output2")

function fun1(num){
    if(num!=NaN){
        if(num <= 0) output1.innerHTML = "Give something greater than 0 idiot"
        if(num==1) output1.innerHTML = 0;
        else if(num==2) output1.innerHTML = "0 1";
        else{
            output1.innerHTML = "0 1";
            count=2;
            var fibSeries = [0, 1];
            for (var i = 2; i < num; i++) {
                fibSeries[i] = fibSeries[i - 1] + fibSeries[i - 2];
                output1.innerHTML = output1.innerHTML + " "+String(fibSeries[i]);
            }
        }
    }
}

function fun2(n){
    if (!isNaN(n)) {
        // Convert n to an integer
        n = parseInt(n);

        // Display the table using alert
        var table = "Number\tSquare\n";
        for (var i = 1; i <= n; i++) {
            var square = i * i;
            table += i + "\t" + square + "\n";
        }

        alert(table);
    } else {
        alert("Invalid input. Please enter a number.");
    }
}


var input_num ;

input_content.addEventListener('keypress',(event)=>{
    if( event.key < "0" || event.key > "9"){
        event.preventDefault();
    }
    if(event.key=="Enter"){
        fun1(parseInt(event.target.value));
        fun2(parseInt(event.target.value))
    }
})
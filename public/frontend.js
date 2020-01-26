const inputform = document.querySelector("#inputform");

const inputfunc = async (a,b,c,d,e,f,g,h,i,j,k) => {
    // console.log("HELLO WORLD");
    try {
        const data = { a,b,c,d,e,f,g,h,i,j,k };
        // console.log(data);
        // console.log("HI");
        const res = await axios.post("/api/input", data);
        console.log(res);
        alert("The expected value of cotton from the given factors is : " + res.data.res + " INR");
        if(res){
            // alert("Done");
        }
    } catch (err) {
        console.log(err);
    }
}

if(inputform){
    inputform.addEventListener("submit" , temp=>{
        temp.preventDefault();
        const a = document.getElementById("a").value;
        const b = document.getElementById("b").value;
        const c = document.getElementById("c").value;
        const d = document.getElementById("d").value;
        const e = document.getElementById("e").value;
        const f = document.getElementById("f").value;
        const g = document.getElementById("g").value;
        const h = document.getElementById("h").value;
        const i = document.getElementById("i").value;
        const j = document.getElementById("j").value;
        const k = document.getElementById("k").value;

        inputfunc(a,b,c,d,e,f,g,h,i,j,k);
    })
}
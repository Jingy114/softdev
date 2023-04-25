var c = document.getElementById("slate");


var ctx = c.getContext("2d");


var mode = "rect";

var bToggler = document.getElementById("buttonToggle");

var toggleMode = (e) => {
   console.log("toggling...");
   if (mode === "rect") {
       mode = "circ";
       bToggler.innerHTML = "circ"
   } else {
       mode = "rect";
       bToggler.innerHTML = "rect";
   }
}


var drawRect = function(e) {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    //console.log("mouseclick registered at ", mouseX, mouseY);
    //console.log(e.offsetX, e.offSetY);
    //ctx.fillStyle = "red";
    ctx.fillRect(mouseX, mouseY, 100, 200);
}


var drawCircle = (e) => {
   var mouseX = e.offsetX;
   var mouseY = e.offsetY;
   console.log("mouseclick registered at ", mouseX, mouseY);
   //console.log(e.offSetX, e.offSetY);
   //ctx.fillStyle = "red";
   ctx.beginPath();
   ctx.arc(mouseX, mouseY, 20, 0, Math.PI * 2);
   ctx.fillStyle = "red";
   ctx.fill();
   ctx.stroke();
}
var draw = (e) => {
   if (mode === "rect") {
       drawRect(e);
   }
   else {
       drawCircle(e);
   }
}




var wipeCanvas = () => {
   ctx.clearRect(0,0,600,600);
}




c.addEventListener("click", draw);
bToggler.addEventListener("click", toggleMode);
var clearB = document.getElementById('buttonClear');
clearB.addEventListener("click", wipeCanvas);


var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");
var dvdButton = document.getElementById("dvd");

var ctx = c.getContext("2d");

ctx.fillStyle = "red";

var requestID; 
var clear = (e) => {
    ctx.clearRect(0,0,500,500);
}

//stops whatever animation is happening
var dvdlogoSetup function() {
    window.cancelAnimationFrame(requestID);


var rectWidth = 60;
var rectHeight = 40;

var rectX = Math.random() * 500;
var rectY = Math.random() * 500;

var xVel = 
var yVel = 
var logo = new Image();
logo.src - "logo_dvd.jpg";

var dvdLogo = function() {
    ctx.clearRect(0, 0, c.width, c.height);
    //
    ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);
    //
    rectX ++
    rectY ++
    requestID = window.requestAnimationFrame(dvd)

}
dvdLogo();
}
var radius = 0;
var growing = true;
var animating = false;

var drawDot = (e) => {
    if (e.type == "click" && animating) {
        return
    }
    animating = true;
    clear();
    requestID = window.requestAnimationFrame(drawDot);
    console.log(requestID);
    ctx.beginPath();
    ctx.arc(250, 250, radius, 1, Math.PI * 2);
    ctx.fillStyle = "red";
    ctx.fill();
    ctx.stroke();

    if (growing == true){
        radius = radius  + 2;
    }
    else {
        radius --;
    }
    if (radius > 250){
        growing = false;
    }
    if (radius == 0){
        growing = true;
    }
}

var stopIt = function() {
    console.log("stopIt  invoked...")
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
    animating = false;
}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);

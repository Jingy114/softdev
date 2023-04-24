var c = getElementByID('slate');

var ctx = c.getContext("2d");

var mode = "rect";

var toggleMode = function() {
    console.log("toggling...");
    if (mode = 'rect') {
        mode = 'circle';
    } else {
        mode = "rect";
    }
}

var drawRect = function() {
    var mouseX = ctx.offsetX;
    var mouseY = ctx.offsetY;
    fillRect(mouseX, mouseY, 5, 12);
    console.log("mouseclick registered at", mouseX, mouseY);
}

var drawCircle = function() {
    var mouseX = ctx.offsetX;
    var mouseY = ctx.offsetY;
    arc(mouseX, mouseY, 3, 17, 17, counterclockwise);
    console.log("mouseClick registered at", mouseX, mouseY);
}

var draw = function(e){
    if (mode == 'rect'){
        drawRect();
    }
    else {
        drawCircle();
    }
}


var wipeCanvas = function() {

}

var bToggler = getElementByID('buttonToggle');

c.addEventListener("click", draw);
bToggler.addEventListener("click", toggleMode);
var clearB = getElementByID('buttonClear');
clearB.addEventListener("click", wipeCanvas);
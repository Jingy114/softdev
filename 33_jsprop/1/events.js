// demo 1
// JS event propagation

var tds = document.getElementsByTagName('td');

//alert displays message upon click
var clicky = function(e) {
  alert( this.innerHTML );
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}

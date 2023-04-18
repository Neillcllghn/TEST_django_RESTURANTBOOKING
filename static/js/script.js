
let sidenav = document.querySelectorAll('.sidenav');
M.Sidenav.init(sidenav);

let collapsible = document.querySelectorAll('.collapsible');
M.Collapsible.init(collapsible);

// Get the modal
let modal = document.getElementById("myModal");

// Get the button that opens the modal
let btn = document.getElementById("myBtn");

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}


// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
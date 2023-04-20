
let sidenav = document.querySelectorAll('.sidenav');
M.Sidenav.init(sidenav);

let collapsible = document.querySelectorAll('.collapsible');
M.Collapsible.init(collapsible);

let modal = document.querySelectorAll('.modal');
M.Modal.init(modal);

var messages = document.getElementsByClassName("messages");

setTimeout(function(){
   if (messages && messages.length) {
       messages[0].classList.add('hide');
   }
}, 3000);
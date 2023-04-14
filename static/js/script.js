let sidenav = document.querySelectorAll('.sidenav');
M.Sidenav.init(sidenav);

let modals = document.querySelectorAll('.modal');
M.Modal.init(modals);

$(document).ready(function(){
    // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
    $('.modal-trigger').leanModal();
  });

  
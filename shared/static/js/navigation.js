/* Toggle sidebar in mobile-mode */
function sidebarToggle(element, event) {
  event.preventDefault();
  element.classList.toggle("active");
  var sidebars = document.getElementsByClassName("sidebar");
  var j;
  for (j=0;j<sidebars.length;j++) {
    sidebars[j].classList.toggle("d-block");
  }
}
/* Toggle sidebar dropdown menus */
var dropdown = document.getElementsByClassName("sidebar-dropdown-btn");
for (var i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function(ev) {
    ev.preventDefault();
    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;
    dropdownContent.classList.toggle("d-block");
  });
}

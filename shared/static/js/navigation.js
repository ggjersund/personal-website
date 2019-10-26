/* Toggle sidebar in mobile-mode */
var toggle = document.getElementsByClassName("sidebar-toggle");
for (let i=0;i<toggle.length;i++) {
  toggle[i].addEventListener("click", function(ev) {
    ev.preventDefault();
    toggle[i].classList.toggle("active");
    let sidebars = document.getElementsByClassName("sidebar");
    for (let j=0;j<sidebars.length;j++) {
      sidebars[j].classList.toggle("d-block");
    }
  });
}
/* Toggle sidebar dropdown menus */
var dropdown = document.getElementsByClassName("sidebar-dropdown-btn");
for (let i=0;i<dropdown.length;i++) {
  dropdown[i].addEventListener("click", function(ev) {
    ev.preventDefault();
    this.classList.toggle("active");
    let dropdownContent = this.nextElementSibling;
    dropdownContent.classList.toggle("d-block");
  });
}

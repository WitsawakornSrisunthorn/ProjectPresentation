window.onscroll = function() {
  if (window.scrollY >= 100) {
    document.querySelector(".navbar.fixed-bottom").classList.remove("display-none");
  } else {
    document.querySelector(".navbar.fixed-bottom").classList.add("display-none");
  }
};

 let year = new Date();
    let now = year.getFullYear();
    let p = document.querySelector("#year");
    p.innerHTML = now;

      let hamburger = document.querySelector(".hamburger");
      let nav = document.querySelector(".ul");

      hamburger.addEventListener("click", function(){
      nav.classList.toggle("nave");
      });
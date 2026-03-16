
// Toggles the hamburger menu with click
import Lenis from 'https://unpkg.com/@studio-freight/lenis@1.0.42/dist/lenis.mjs'
import gsap from 'https://unpkg.com/gsap@3.12.5/index.js'
import ScrollTrigger from 'https://unpkg.com/gsap@3.12.5/ScrollTrigger.js'
const toggles = document.querySelectorAll(".faq-toggle");
toggles.forEach((toggle)=>{
    toggle.addEventListener("click",()=>{
        toggle.parentNode.classList.toggle("active");
    })
})
const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        // Add the 'show' class when it enters the screen
        entry.target.classList.add('show');
      } else {
        // Optional: remove it if you want the animation to repeat
        // entry.target.classList.remove('show');
      }
    });
  }, {
    threshold: 0.2 // Trigger when 20% of the element is visible
  });
  
  // Grab all elements you want to animate
  const hiddenElements = document.querySelectorAll('.fly-in');
  hiddenElements.forEach((el) => observer.observe(el));
  document.getElementById('rsvp-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevents the default full page reload
  
    const formData = new FormData(event.target); // Collects all form data
  
    fetch('/', { // Replace '/' with your specific Flask route URL
      method: 'POST',
      body: formData,
    })
    .then(response => {
      // Handle the response from the Flask backend here (e.g., show a success message)
      console.log('Form submitted successfully without page reload!');
      // You can update specific parts of the page dynamically if needed
    })
    .catch(error => {
      console.error('Error submitting form:', error);
    });
  });

  const lenis = new Lenis();

lenis.on("scroll", ScrollTrigger.update);
gsap.ticker.add((time) => {
  lenis.raf(time * 1000);
});
gsap.ticker.lagSmoothing(0);

gsap.registerPlugin(ScrollTrigger);

const reveal = document.querySelector(".reveal");

ScrollTrigger.create({
  trigger: reveal,
  start: "top top",
  end: "bottom top",
  pin: true,
  scrub: true,
  onUpdate: (self) => {
    const p = self.progress;
    const eased = gsap.parseEase("power4.in")(p);

    reveal.style.setProperty("--progress", p);
    reveal.style.setProperty("--sub-opacity", eased);
    reveal.style.setProperty("--sub-scale", 0.25 + 1 * p);
  }
});

document.querySelector('.hamburger').addEventListener('click', function() {
    var navRight = document.getElementById('navbarRight');
    if (navRight.style.left === "0px") {
        navRight.style.left = "-100%"; // Slide out
    } else {
        navRight.style.left = "0"; // Slide in
    }
});

document.querySelector('.hamburger').addEventListener('click', function() {
    document.getElementById('navbarRight').style.left = "0"; // Slide in
});

document.querySelector('.closebtn').addEventListener('click', function() {
    document.getElementById('navbarRight').style.left = "-100%"; // Slide out
});




// Toggles the dropdown menu with click

const dropBtn = document.getElementById('dropBtn');
if (dropBtn) { // Check if the element actually exists
const dropdownContent = document.querySelector('.dropdown-content');

dropBtn.addEventListener('click', function() {
    console.log('clicked');
    if (dropdownContent.style.display === "none") {
        dropdownContent.style.display = "block";
    } else {
        dropdownContent.style.display = "none";
    }
    console.log(dropdownContent);
});
}



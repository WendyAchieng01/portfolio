console.log("hello");

var typed = new Typed(".text", {
  strings: ["Frontend Developer", "Web Designer", "UX/UI Developer"],
  typeSpeed: 100,
  backSpeed: 100,
  backDelay: 1000,
  loop: true,
});

//scroll
// Get all elements with the class 'reveal'
const reveals = document.querySelectorAll(".reveal");

// Create a new Intersection Observer instance
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    // Check if the element is intersecting with the viewport
    if (entry.isIntersecting) {
      // Add the 'active' class to the element
      entry.target.classList.add("active");

      // Find the animation elements inside the container
      const animatedElements = entry.target.querySelectorAll(
        ".anim, .content-image, .container-rev"
      );

      // Add the animation classes to the elements
      animatedElements.forEach((element) => {
        element.classList.add("animate");
      });
    } else {
      // Remove the 'active' class from the element
      entry.target.classList.remove("active");

      // Find the animation elements inside the container
      const animatedElements = entry.target.querySelectorAll(
        ".anim, .content-image, .container-rev"
      );

      // Remove the animation classes from the elements
      animatedElements.forEach((element) => {
        element.classList.remove("animate");
      });
    }
  });
});

// Observe each element with the class 'reveal'
reveals.forEach((reveal) => {
  observer.observe(reveal);
});

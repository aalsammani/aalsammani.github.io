// Mobile menu toggle
function toggleMenu() {
  const navMenu = document.getElementById('nav-menu');
  const mobileIcon = document.querySelector('.mobile-menu-icon');
  
  navMenu.classList.toggle('active');
  mobileIcon.classList.toggle('active');
}

// Close menu when clicking on a link (mobile)
document.addEventListener('DOMContentLoaded', function() {
  // Get all nav links
  const navLinks = document.querySelectorAll('.nav-links a');
  
  // Add click event to each link
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      const navMenu = document.getElementById('nav-menu');
      const mobileIcon = document.querySelector('.mobile-menu-icon');
      
      // Only close if it's open (has active class)
      if (navMenu.classList.contains('active')) {
        navMenu.classList.remove('active');
        mobileIcon.classList.remove('active');
      }
    });
  });

  // Publication tabs functionality (for research page)
  const pubTabs = document.querySelectorAll('.publication-tab');
  if (pubTabs.length > 0) {
    pubTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        // Remove active class from all tabs
        pubTabs.forEach(t => t.classList.remove('active'));
        
        // Add active class to clicked tab
        tab.classList.add('active');
        
        // Get category to filter
        const category = tab.getAttribute('data-category');
        
        // Get all publication items
        const pubItems = document.querySelectorAll('.publication-item');
        
        // Show/hide based on category
        pubItems.forEach(item => {
          if (category === 'all' || item.getAttribute('data-type') === category) {
            item.style.display = 'block';
          } else {
            item.style.display = 'none';
          }
        });
      });
    });
  }

  // Add animation to expertise cards
  const expertiseCards = document.querySelectorAll('.expertise-card');
  if (expertiseCards.length > 0) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('animate');
        }
      });
    }, { threshold: 0.3 });
    
    expertiseCards.forEach(card => {
      observer.observe(card);
    });
  }

  // Add counter animation for stats if they exist
  const statNumbers = document.querySelectorAll('.stat-number');
  if (statNumbers.length > 0) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const target = entry.target;
          const countTo = parseInt(target.getAttribute('data-count'));
          let count = 0;
          const speed = 2000 / countTo;
          
          const updateCount = () => {
            count++;
            target.textContent = count;
            
            if (count < countTo) {
              setTimeout(updateCount, speed);
            }
          };
          
          updateCount();
          observer.unobserve(target);
        }
      });
    }, { threshold: 0.5 });
    
    statNumbers.forEach(num => {
      observer.observe(num);
    });
  }
});

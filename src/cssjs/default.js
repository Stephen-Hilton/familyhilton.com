// Default Theme JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Navigation functionality
    initNavigation();
    
    // Smooth scrolling for anchor links
    initSmoothScrolling();
    
    // Interactive features
    initInteractiveFeatures();
});

function initNavigation() {
    // Close navigation on escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            const activeNav = document.querySelector('.left-nav.active, .right-nav.active');
            if (activeNav) {
                closeNav(activeNav);
            }
        }
    });
}

// Global navigation functions
function toggleLeftNav() {
    const leftNav = document.getElementById('leftNav');
    if (leftNav) {
        toggleNav(leftNav);
    }
}

function toggleRightNav() {
    const rightNav = document.getElementById('rightNav');
    if (rightNav) {
        toggleNav(rightNav);
    }
}

function closeLeftNav() {
    const leftNav = document.getElementById('leftNav');
    if (leftNav) {
        closeNav(leftNav);
    }
}

function closeRightNav() {
    const rightNav = document.getElementById('rightNav');
    if (rightNav) {
        closeNav(rightNav);
    }
}

function toggleNav(nav) {
    const overlay = nav.querySelector('.nav-overlay');
    
    if (nav.classList.contains('active')) {
        closeNav(nav);
    } else {
        openNav(nav);
    }
}

function openNav(nav) {
    const overlay = nav.querySelector('.nav-overlay');
    
    nav.classList.add('active');
    if (overlay) {
        overlay.classList.add('active');
    }
    
    // Focus management
    const firstFocusable = nav.querySelector('a, button');
    if (firstFocusable) {
        firstFocusable.focus();
    }
}

function closeNav(nav) {
    const overlay = nav.querySelector('.nav-overlay');
    
    nav.classList.remove('active');
    if (overlay) {
        overlay.classList.remove('active');
    }
}

function initSmoothScrolling() {
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href === '#') return;
            
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

function initInteractiveFeatures() {
    // Add loading states to buttons
    document.querySelectorAll('button, .hero-cta').forEach(button => {
        button.addEventListener('click', function() {
            // Add a subtle loading effect
            this.style.transform = 'scale(0.98)';
            setTimeout(() => {
                this.style.transform = '';
            }, 150);
        });
    });
    
    // Lazy loading for images
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    if (img.dataset.src) {
                        img.src = img.dataset.src;
                        img.removeAttribute('data-src');
                        observer.unobserve(img);
                    }
                }
            });
        });
        
        document.querySelectorAll('img[data-src]').forEach(img => {
            imageObserver.observe(img);
        });
    }
    
    // Add hover effects to cards and tiles
    document.querySelectorAll('.page-card, .page-tile, .feature-item').forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-4px)';
        });
        
        item.addEventListener('mouseleave', function() {
            this.style.transform = '';
        });
    });
    
    // Animate elements on scroll
    if ('IntersectionObserver' in window) {
        const animateObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });
        
        // Add animation to sections
        document.querySelectorAll('section').forEach(section => {
            section.style.opacity = '0';
            section.style.transform = 'translateY(20px)';
            section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            animateObserver.observe(section);
        });
    }
    
    // Theme switching (if multiple themes are available)
    const themeToggle = document.querySelector('.theme-toggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            const currentTheme = document.documentElement.getAttribute('data-theme') || 'default';
            const newTheme = currentTheme === 'default' ? 'dark' : 'default';
            
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
        });
        
        // Load saved theme
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme) {
            document.documentElement.setAttribute('data-theme', savedTheme);
        }
    }
}

// Utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    }
}

// Handle window resize
window.addEventListener('resize', debounce(function() {
    // Close mobile navigation on resize to desktop
    if (window.innerWidth > 768) {
        const activeNav = document.querySelector('.left-nav.active, .right-nav.active');
        if (activeNav) {
            closeNav(activeNav);
        }
    }
}, 250));

// Add focus management for accessibility
document.addEventListener('keydown', function(e) {
    // Tab navigation enhancement
    if (e.key === 'Tab') {
        document.body.classList.add('keyboard-navigation');
    }
});

document.addEventListener('mousedown', function() {
    document.body.classList.remove('keyboard-navigation');
});

// Performance optimization: Preload critical resources
function preloadCriticalResources() {
    const criticalImages = document.querySelectorAll('img[data-critical]');
    criticalImages.forEach(img => {
        const link = document.createElement('link');
        link.rel = 'preload';
        link.as = 'image';
        link.href = img.src || img.dataset.src;
        document.head.appendChild(link);
    });
}

// Initialize preloading
preloadCriticalResources();
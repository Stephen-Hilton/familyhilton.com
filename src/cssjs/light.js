// Light Theme JavaScript
// Import default functionality
document.addEventListener('DOMContentLoaded', function() {
    // Load default.js functionality
    const script = document.createElement('script');
    script.src = '/src/cssjs/default.js';
    document.head.appendChild(script);
    
    // Light theme specific enhancements
    initLightThemeFeatures();
});

function initLightThemeFeatures() {
    // Enhanced animations for light theme
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -30px 0px'
    };
    
    if ('IntersectionObserver' in window) {
        const lightAnimationObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0) scale(1)';
                    entry.target.style.filter = 'blur(0px)';
                }
            });
        }, observerOptions);
        
        // Animate cards with a subtle scale effect
        document.querySelectorAll('.page-card, .feature-item').forEach(item => {
            item.style.opacity = '0';
            item.style.transform = 'translateY(20px) scale(0.95)';
            item.style.filter = 'blur(2px)';
            item.style.transition = 'all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
            lightAnimationObserver.observe(item);
        });
    }
    
    // Light theme specific interactions
    document.querySelectorAll('.feature-item').forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.boxShadow = '0 20px 25px -5px rgb(0 0 0 / 0.1), 0 10px 10px -5px rgb(0 0 0 / 0.04)';
            this.style.borderColor = 'var(--primary-color)';
        });
        
        item.addEventListener('mouseleave', function() {
            this.style.boxShadow = '';
            this.style.borderColor = '';
        });
    });
    
    // Subtle parallax effect for hero section
    const heroSection = document.querySelector('.hero-section');
    if (heroSection) {
        window.addEventListener('scroll', function() {
            const scrolled = window.pageYOffset;
            const rate = scrolled * -0.5;
            heroSection.style.transform = `translateY(${rate}px)`;
        });
    }
}
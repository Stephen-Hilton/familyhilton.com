// Dark Theme JavaScript
// Import default functionality
document.addEventListener('DOMContentLoaded', function() {
    // Load default.js functionality
    const script = document.createElement('script');
    script.src = '/src/cssjs/default.js';
    document.head.appendChild(script);
    
    // Dark theme specific enhancements
    initDarkThemeFeatures();
});

function initDarkThemeFeatures() {
    // Dark theme specific animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    if ('IntersectionObserver' in window) {
        const darkAnimationObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                    entry.target.classList.add('animate-glow');
                }
            });
        }, observerOptions);
        
        // Add glow animation to cards in dark theme
        document.querySelectorAll('.page-card, .feature-item').forEach(item => {
            item.style.opacity = '0';
            item.style.transform = 'translateY(30px)';
            item.style.transition = 'all 0.6s ease-out';
            darkAnimationObserver.observe(item);
        });
    }
    
    // Add CSS for glow effect
    const glowStyle = document.createElement('style');
    glowStyle.textContent = `
        .animate-glow {
            animation: subtleGlow 2s ease-in-out infinite alternate;
        }
        
        @keyframes subtleGlow {
            from {
                box-shadow: 0 0 5px rgba(96, 165, 250, 0.2);
            }
            to {
                box-shadow: 0 0 20px rgba(96, 165, 250, 0.1), 0 0 30px rgba(96, 165, 250, 0.05);
            }
        }
        
        .page-card:hover,
        .page-tile:hover {
            box-shadow: 0 0 30px rgba(96, 165, 250, 0.2) !important;
        }
        
        .hero-cta-primary {
            box-shadow: 0 0 20px rgba(96, 165, 250, 0.3);
        }
        
        .hero-cta-primary:hover {
            box-shadow: 0 0 30px rgba(251, 191, 36, 0.4);
        }
    `;
    document.head.appendChild(glowStyle);
    
    // Dark theme specific interactions
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('mouseenter', function() {
            this.style.color = 'var(--primary-color)';
            this.style.textShadow = '0 0 10px rgba(96, 165, 250, 0.5)';
        });
        
        link.addEventListener('mouseleave', function() {
            this.style.color = '';
            this.style.textShadow = '';
        });
    });
    
    // Enhanced hover effects for dark theme
    document.querySelectorAll('.feature-item').forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.background = 'linear-gradient(135deg, var(--surface-color), #374151)';
            this.style.borderColor = 'var(--primary-color)';
        });
        
        item.addEventListener('mouseleave', function() {
            this.style.background = '';
            this.style.borderColor = '';
        });
    });
    
    // Particle effect for hero section (subtle)
    const heroSection = document.querySelector('.hero-section');
    if (heroSection) {
        createParticleEffect(heroSection);
    }
}

function createParticleEffect(container) {
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    
    canvas.style.position = 'absolute';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.style.pointerEvents = 'none';
    canvas.style.opacity = '0.3';
    
    container.style.position = 'relative';
    container.appendChild(canvas);
    
    function resizeCanvas() {
        canvas.width = container.offsetWidth;
        canvas.height = container.offsetHeight;
    }
    
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);
    
    const particles = [];
    const particleCount = 50;
    
    for (let i = 0; i < particleCount; i++) {
        particles.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            vx: (Math.random() - 0.5) * 0.5,
            vy: (Math.random() - 0.5) * 0.5,
            size: Math.random() * 2 + 1,
            opacity: Math.random() * 0.5 + 0.2
        });
    }
    
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        particles.forEach(particle => {
            particle.x += particle.vx;
            particle.y += particle.vy;
            
            if (particle.x < 0 || particle.x > canvas.width) particle.vx *= -1;
            if (particle.y < 0 || particle.y > canvas.height) particle.vy *= -1;
            
            ctx.beginPath();
            ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(96, 165, 250, ${particle.opacity})`;
            ctx.fill();
        });
        
        requestAnimationFrame(animate);
    }
    
    animate();
}
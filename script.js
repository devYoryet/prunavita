/**
 * PRUNAVITA - Landing Page JavaScript
 * Handles all interactions and animations
 */

// ==========================================
// NAVIGATION FUNCTIONALITY
// ==========================================

class Navigation {
    constructor() {
        this.navbar = document.getElementById('navbar');
        this.menuToggle = document.getElementById('menuToggle');
        this.navMenu = document.getElementById('navMenu');
        this.navLinks = document.querySelectorAll('.nav-menu a');

        this.init();
    }

    init() {
        // Scroll event for navbar
        window.addEventListener('scroll', () => this.handleScroll());

        // Mobile menu toggle
        this.menuToggle.addEventListener('click', () => this.toggleMenu());

        // Close menu on link click
        this.navLinks.forEach(link => {
            link.addEventListener('click', () => this.closeMenu());
        });

        // Smooth scroll for anchor links
        this.navLinks.forEach(link => {
            link.addEventListener('click', (e) => this.smoothScroll(e));
        });

        // Close menu on outside click
        document.addEventListener('click', (e) => this.handleOutsideClick(e));
    }

    handleScroll() {
        if (window.scrollY > 50) {
            this.navbar.classList.add('scrolled');
        } else {
            this.navbar.classList.remove('scrolled');
        }
    }

    toggleMenu() {
        this.menuToggle.classList.toggle('active');
        this.navMenu.classList.toggle('active');
        document.body.style.overflow = this.navMenu.classList.contains('active') ? 'hidden' : '';
    }

    closeMenu() {
        this.menuToggle.classList.remove('active');
        this.navMenu.classList.remove('active');
        document.body.style.overflow = '';
    }

    smoothScroll(e) {
        const href = e.target.getAttribute('href');

        if (href && href.startsWith('#')) {
            e.preventDefault();
            const target = document.querySelector(href);

            if (target) {
                const offsetTop = target.offsetTop - 80;
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        }
    }

    handleOutsideClick(e) {
        if (!this.navMenu.contains(e.target) &&
            !this.menuToggle.contains(e.target) &&
            this.navMenu.classList.contains('active')) {
            this.closeMenu();
        }
    }
}

// ==========================================
// SCROLL ANIMATIONS (AOS Alternative)
// ==========================================

class ScrollAnimations {
    constructor() {
        this.elements = document.querySelectorAll('[data-aos]');
        this.observerOptions = {
            threshold: 0.15,
            rootMargin: '0px 0px -50px 0px'
        };

        this.init();
    }

    init() {
        // Create intersection observer
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    // Add delay if specified
                    const delay = entry.target.getAttribute('data-aos-delay') || 0;

                    setTimeout(() => {
                        entry.target.classList.add('aos-animate');
                    }, delay);

                    // Unobserve after animation
                    observer.unobserve(entry.target);
                }
            });
        }, this.observerOptions);

        // Observe all elements with data-aos attribute
        this.elements.forEach(el => observer.observe(el));
    }
}

// ==========================================
// CONTACT FORM HANDLING
// ==========================================

class ContactForm {
    constructor() {
        this.form = document.getElementById('contactForm');
        this.init();
    }

    init() {
        if (this.form) {
            this.form.addEventListener('submit', (e) => this.handleSubmit(e));
        }
    }

    handleSubmit(e) {
        e.preventDefault();

        // Get form data
        const formData = new FormData(this.form);
        const data = Object.fromEntries(formData.entries());

        // Validate form
        if (!this.validateForm(data)) {
            return;
        }

        // Show loading state
        const submitBtn = this.form.querySelector('button[type="submit"]');
        const originalText = submitBtn.textContent;
        const lang = window.langManager ? window.langManager.getCurrentLang() : 'es';
        const sendingText = lang === 'es' ? 'Enviando...' : 'Sending...';

        submitBtn.textContent = sendingText;
        submitBtn.disabled = true;

        // Send to PHP backend
        fetch('send-email.php', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            if (result.success) {
                const successMsg = window.langManager ? window.langManager.translate('form.success') : '¡Mensaje enviado! Nos contactaremos pronto.';
                this.showMessage(successMsg, 'success');
                this.form.reset();
            } else {
                throw new Error(result.message);
            }
        })
        .catch((error) => {
            console.error('Error:', error);
            const errorMsg = window.langManager ? window.langManager.translate('form.error') : 'Error al enviar el mensaje. Por favor intente nuevamente.';
            this.showMessage(errorMsg, 'error');
        })
        .finally(() => {
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
        });
    }

    validateForm(data) {
        // Basic validation
        const requiredFields = ['name', 'email', 'service', 'message'];

        for (let field of requiredFields) {
            if (!data[field] || data[field].trim() === '') {
                const msg = window.langManager ? window.langManager.translate('form.validation') : 'Por favor complete todos los campos requeridos.';
                this.showMessage(msg, 'error');
                return false;
            }
        }

        // Email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(data.email)) {
            const msg = window.langManager ? window.langManager.translate('form.email.invalid') : 'Por favor ingrese un email válido.';
            this.showMessage(msg, 'error');
            return false;
        }

        return true;
    }

    showMessage(message, type) {
        // Remove existing messages
        const existingMessage = document.querySelector('.form-message');
        if (existingMessage) {
            existingMessage.remove();
        }

        // Create message element
        const messageEl = document.createElement('div');
        messageEl.className = `form-message form-message-${type}`;
        messageEl.textContent = message;

        // Style message
        Object.assign(messageEl.style, {
            padding: '1rem',
            marginTop: '1rem',
            borderRadius: '0.5rem',
            fontSize: '0.9375rem',
            fontWeight: '500',
            backgroundColor: type === 'success' ? '#D1FAE5' : '#FEE2E2',
            color: type === 'success' ? '#065F46' : '#991B1B',
            border: `2px solid ${type === 'success' ? '#10B981' : '#EF4444'}`
        });

        // Insert message
        this.form.appendChild(messageEl);

        // Auto remove after 5 seconds
        setTimeout(() => {
            messageEl.style.transition = 'opacity 0.3s ease';
            messageEl.style.opacity = '0';
            setTimeout(() => messageEl.remove(), 300);
        }, 5000);
    }
}

// ==========================================
// PERFORMANCE OPTIMIZATIONS
// ==========================================

class PerformanceOptimizer {
    constructor() {
        this.init();
    }

    init() {
        // Lazy load images if any are added later
        this.setupLazyLoading();

        // Debounce scroll events
        this.debounceScrollEvents();

        // Optimize animations
        this.optimizeAnimations();
    }

    setupLazyLoading() {
        if ('loading' in HTMLImageElement.prototype) {
            const images = document.querySelectorAll('img[loading="lazy"]');
            images.forEach(img => {
                img.src = img.dataset.src || img.src;
            });
        } else {
            // Fallback for browsers that don't support lazy loading
            const lazyImages = document.querySelectorAll('img[data-src]');

            if (lazyImages.length > 0) {
                const imageObserver = new IntersectionObserver((entries) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            const img = entry.target;
                            img.src = img.dataset.src;
                            img.removeAttribute('data-src');
                            imageObserver.unobserve(img);
                        }
                    });
                });

                lazyImages.forEach(img => imageObserver.observe(img));
            }
        }
    }

    debounceScrollEvents() {
        let scrollTimeout;
        const originalScrollHandler = window.onscroll;

        window.addEventListener('scroll', () => {
            if (scrollTimeout) {
                window.cancelAnimationFrame(scrollTimeout);
            }

            scrollTimeout = window.requestAnimationFrame(() => {
                if (originalScrollHandler) {
                    originalScrollHandler();
                }
            });
        }, { passive: true });
    }

    optimizeAnimations() {
        // Reduce animations on low-end devices
        const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

        if (prefersReducedMotion.matches) {
            document.body.style.setProperty('--transition-fast', '0s');
            document.body.style.setProperty('--transition-base', '0s');
            document.body.style.setProperty('--transition-slow', '0s');
        }
    }
}

// ==========================================
// HERO STATS COUNTER ANIMATION
// ==========================================

class StatsCounter {
    constructor() {
        this.stats = document.querySelectorAll('.stat-number');
        this.hasAnimated = false;
        this.init();
    }

    init() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !this.hasAnimated) {
                    this.animateStats();
                    this.hasAnimated = true;
                }
            });
        }, { threshold: 0.5 });

        const statsSection = document.querySelector('.hero-stats');
        if (statsSection) {
            observer.observe(statsSection);
        }
    }

    animateStats() {
        this.stats.forEach(stat => {
            const target = stat.textContent;
            const isPercent = target.includes('%');
            const isPlus = target.includes('+');
            const numericValue = parseInt(target.replace(/[^\d]/g, ''));

            let current = 0;
            const increment = numericValue / 50; // 50 frames
            const duration = 2000; // 2 seconds
            const frameTime = duration / 50;

            const counter = setInterval(() => {
                current += increment;

                if (current >= numericValue) {
                    stat.textContent = target;
                    clearInterval(counter);
                } else {
                    const displayValue = Math.floor(current);
                    stat.textContent = displayValue + (isPlus ? '+' : '') + (isPercent ? '%' : '');
                }
            }, frameTime);
        });
    }
}

// ==========================================
// SCROLL PROGRESS INDICATOR
// ==========================================

class ScrollProgress {
    constructor() {
        this.createProgressBar();
        this.init();
    }

    createProgressBar() {
        const progressBar = document.createElement('div');
        progressBar.className = 'scroll-progress';

        Object.assign(progressBar.style, {
            position: 'fixed',
            top: '0',
            left: '0',
            width: '0%',
            height: '3px',
            background: 'linear-gradient(90deg, #6B46C1 0%, #9333EA 100%)',
            zIndex: '9999',
            transition: 'width 0.2s ease'
        });

        document.body.appendChild(progressBar);
        this.progressBar = progressBar;
    }

    init() {
        window.addEventListener('scroll', () => {
            const windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = (window.scrollY / windowHeight) * 100;
            this.progressBar.style.width = scrolled + '%';
        }, { passive: true });
    }
}

// ==========================================
// UTILITY FUNCTIONS
// ==========================================

const Utils = {
    // Debounce function
    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },

    // Throttle function
    throttle(func, limit) {
        let inThrottle;
        return function(...args) {
            if (!inThrottle) {
                func.apply(this, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    },

    // Check if element is in viewport
    isInViewport(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }
};

// ==========================================
// SERVICES CAROUSEL
// ==========================================

class ServicesCarousel {
    constructor() {
        this.carousel = document.getElementById('servicesCarousel');
        if (!this.carousel) {
            console.warn('Services carousel not found');
            return;
        }

        this.slides = this.carousel.querySelectorAll('.service-slide');
        this.indicators = document.querySelectorAll('.hero-services-carousel-wrapper .indicator-dot');
        this.prevBtn = document.getElementById('prevSlide');
        this.nextBtn = document.getElementById('nextSlide');

        this.currentSlide = 0;
        this.autoplayInterval = null;
        this.autoplayDelay = 5000; // 5 segundos

        console.log(`Services carousel initialized with ${this.slides.length} slides`);
        this.init();
    }

    init() {
        // Set up navigation buttons
        if (this.prevBtn) {
            this.prevBtn.addEventListener('click', () => this.prev());
        }
        if (this.nextBtn) {
            this.nextBtn.addEventListener('click', () => this.next());
        }

        // Set up indicators
        this.indicators.forEach((indicator, index) => {
            indicator.addEventListener('click', () => this.goToSlide(index));
        });

        // Start autoplay
        this.startAutoplay();

        // Pause on hover
        this.carousel.addEventListener('mouseenter', () => this.stopAutoplay());
        this.carousel.addEventListener('mouseleave', () => this.startAutoplay());

        // Pause on focus (accessibility)
        this.carousel.addEventListener('focusin', () => this.stopAutoplay());
        this.carousel.addEventListener('focusout', () => this.startAutoplay());

        // Handle visibility change (pause when tab is not visible)
        document.addEventListener('visibilitychange', () => {
            if (document.hidden) {
                this.stopAutoplay();
            } else {
                this.startAutoplay();
            }
        });
    }

    goToSlide(index) {
        // Remove active class from current slide
        this.slides[this.currentSlide].classList.remove('active');
        this.slides[this.currentSlide].classList.add('prev');
        this.indicators[this.currentSlide].classList.remove('active');

        // Update current slide
        this.currentSlide = index;

        // Add active class to new slide
        setTimeout(() => {
            this.slides.forEach(slide => slide.classList.remove('prev'));
            this.slides[this.currentSlide].classList.add('active');
            this.indicators[this.currentSlide].classList.add('active');
        }, 50);
    }

    next() {
        const nextIndex = (this.currentSlide + 1) % this.slides.length;
        this.goToSlide(nextIndex);
    }

    prev() {
        const prevIndex = (this.currentSlide - 1 + this.slides.length) % this.slides.length;
        this.goToSlide(prevIndex);
    }

    startAutoplay() {
        this.stopAutoplay(); // Clear any existing interval
        this.autoplayInterval = setInterval(() => this.next(), this.autoplayDelay);
    }

    stopAutoplay() {
        if (this.autoplayInterval) {
            clearInterval(this.autoplayInterval);
            this.autoplayInterval = null;
        }
    }
}

// ==========================================
// INITIALIZE ALL MODULES
// ==========================================

document.addEventListener('DOMContentLoaded', () => {
    // Add loading class to body
    document.body.classList.add('loading');

    // Initialize language manager first
    window.langManager = new LanguageManager();

    // Initialize all modules
    new Navigation();
    new ScrollAnimations();
    new ContactForm();
    new PerformanceOptimizer();
    new StatsCounter();
    new ScrollProgress();
    new ServicesCarousel(); // Initialize carousel

    // Log initialization
    console.log('%c🍇 Prunavita Website Loaded', 'color: #4A2545; font-size: 16px; font-weight: bold;');
    console.log('%cExportación de fruta deshidratada premium | Premium dried fruit exports', 'color: #5A7247; font-size: 12px;');
});

// ==========================================
// EXPORT FOR POTENTIAL MODULE USE
// ==========================================

if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        Navigation,
        ScrollAnimations,
        ContactForm,
        Utils
    };
}

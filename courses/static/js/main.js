// Main JavaScript for Semicolons Course Platform

document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    
    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
        });
        
        // Close mobile menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!mobileMenuBtn.contains(e.target) && !mobileMenu.contains(e.target)) {
                mobileMenu.classList.add('hidden');
            }
        });
    }

    // Add smooth scrolling for anchor links
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Auto-hide success messages after 5 seconds with animation
    const messages = document.querySelectorAll('.bg-green-100');
    messages.forEach(message => {
        setTimeout(() => {
            message.style.transition = 'opacity 0.5s ease-out';
            message.style.opacity = '0';
            setTimeout(() => {
                message.remove();
            }, 500);
        }, 5000);
    });

    // Enhanced form validation with SweetAlert
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            let emptyFields = [];
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('border-red-500', 'animate-pulse');
                    setTimeout(() => field.classList.remove('animate-pulse'), 1000);
                    emptyFields.push(field.previousElementSibling?.textContent || 'Field');
                } else {
                    field.classList.remove('border-red-500');
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                Swal.fire({
                    icon: 'error',
                    title: 'Validation Error',
                    text: 'Please fill in all required fields.',
                    confirmButtonColor: '#0d171b'
                });
            }
        });
    });

    // Course search functionality
    const searchInput = document.getElementById('course-search');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase().trim();
            const courseCards = document.querySelectorAll('.course-card');
            let visibleCount = 0;
            
            courseCards.forEach(card => {
                const title = card.querySelector('.course-title')?.textContent.toLowerCase() || '';
                const description = card.querySelector('.course-description')?.textContent.toLowerCase() || '';
                
                if (searchTerm === '' || title.includes(searchTerm) || description.includes(searchTerm)) {
                    card.style.display = 'block';
                    visibleCount++;
                } else {
                    card.style.display = 'none';
                }
            });
            
            // Show/hide no results message
            let noResultsMsg = document.getElementById('no-results-message');
            if (visibleCount === 0 && searchTerm !== '') {
                if (!noResultsMsg) {
                    noResultsMsg = document.createElement('div');
                    noResultsMsg.id = 'no-results-message';
                    noResultsMsg.className = 'col-span-full text-center py-20';
                    noResultsMsg.innerHTML = `
                        <svg class="w-24 h-24 text-gray-300 mx-auto mb-6" fill="currentColor" viewBox="0 0 20 20">
                            <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                        </svg>
                        <h3 class="text-[#0d171b] text-xl font-bold mb-2">No Courses Found</h3>
                        <p class="text-[#4c809a] text-base">Try searching with different keywords</p>
                    `;
                    document.getElementById('courses-grid').appendChild(noResultsMsg);
                }
                noResultsMsg.style.display = 'block';
            } else if (noResultsMsg) {
                noResultsMsg.style.display = 'none';
            }
        });
    }

    // No processing states for any submit buttons

    // SweetAlert helper functions
    window.showSuccess = function(message) {
        Swal.fire({
            icon: 'success',
            title: 'Success!',
            text: message,
            timer: 3000,
            showConfirmButton: false
        });
    };
    
    window.showError = function(message) {
        Swal.fire({
            icon: 'error',
            title: 'Error!',
            text: message,
            confirmButtonColor: '#0d171b'
        });
    };
    
    window.showConfirm = function(message, callback) {
        Swal.fire({
            title: 'Are you sure?',
            text: message,
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#0d171b',
            cancelButtonColor: '#4c809a',
            confirmButtonText: 'Yes, proceed!'
        }).then((result) => {
            if (result.isConfirmed && callback) {
                callback();
            }
        });
    };

    // Password toggle functionality
    window.togglePassword = function(fieldId) {
        const field = document.getElementById(fieldId);
        const eye = document.getElementById(fieldId + '-eye');
        
        if (field.type === 'password') {
            field.type = 'text';
            eye.textContent = 'visibility';
        } else {
            field.type = 'password';
            eye.textContent = 'visibility_off';
        }
    };

    // Add hover effects to cards
    const cards = document.querySelectorAll('.hover\\:shadow-xl');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
});
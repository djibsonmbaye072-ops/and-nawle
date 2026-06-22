document.addEventListener('DOMContentLoaded', () => {

    const counters = document.querySelectorAll('.counter');

    const animateCounter = (counter) => {

        const originalValue = counter.textContent.trim();

        const isPercent = originalValue.includes('%');

        const target = parseInt(
            originalValue.replace('%', ''),
            10
        );

        if (isNaN(target)) return;

        let current = 0;

        const increment = Math.max(
            1,
            Math.ceil(target / 100)
        );

        const updateCounter = () => {

            current += increment;

            if (current < target) {

                counter.textContent =
                    current +
                    (isPercent ? '%' : '');

                requestAnimationFrame(updateCounter);

            } else {

                counter.textContent =
                    target +
                    (isPercent ? '%' : '');
            }
        };

        updateCounter();
    };

    const observer = new IntersectionObserver(

        (entries, observer) => {

            entries.forEach(entry => {

                if (entry.isIntersecting) {

                    animateCounter(entry.target);

                    observer.unobserve(entry.target);
                }

            });

        },

        {
            threshold: 0.5
        }

    );

    counters.forEach(counter => {

        observer.observe(counter);

    });

});
document.addEventListener('DOMContentLoaded', () => {
    const langSwitch = document.querySelector('.header__lang-switch');
    const langButtons = document.querySelectorAll('.header__lang-btn');
    
    const setCookie = (name, value, days) => {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        document.cookie = `${name}=${value};path=/;expires=${date.toUTCString()}`;
    };

    const getCookie = (name) => {
        const match = document.cookie.match(new RegExp(`(^| )${name}=([^;]+)`));
        return match ? match[2] : null;
    };

    const updateActiveLang = () => {
        const currentLang = getCookie('language') || 'uk'; // Значення за замовчуванням — 'uk'
        langButtons.forEach((btn) => {
            if (btn.dataset.lang === currentLang) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });
    };

    langSwitch.addEventListener('click', (event) => {
        const target = event.target;
        if (target.classList.contains('header__lang-btn')) {
            const selectedLang = target.dataset.lang;
            const currentLang = getCookie('language');
            
            if (currentLang === selectedLang) return;
            
            setCookie('language', selectedLang, 30);

            updateActiveLang();

            location.reload()
        }
    });

    updateActiveLang();
});

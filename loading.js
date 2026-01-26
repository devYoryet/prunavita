/**
 * Loading Screen Handler
 * Removes loading screen when page is fully loaded
 */

(function() {
    'use strict';
    
    function hideLoading() {
        const loadingScreen = document.getElementById('loadingScreen');
        const body = document.body;
        
        if (loadingScreen) {
            loadingScreen.classList.add('hidden');
            setTimeout(function() {
                loadingScreen.remove();
                body.classList.add('loaded');
            }, 300);
        } else {
            body.classList.add('loaded');
        }
    }
    
    // Hide loading when DOM and resources are ready
    if (document.readyState === 'complete') {
        hideLoading();
    } else {
        window.addEventListener('load', hideLoading);
        // Fallback timeout to ensure loading screen disappears
        setTimeout(hideLoading, 2000);
    }
})();

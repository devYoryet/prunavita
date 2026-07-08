/**
 * Optional loading screen cleanup (legacy).
 * Content is visible immediately; this only removes a spinner if present.
 */
(function () {
    'use strict';

    function cleanup() {
        document.body.classList.add('loaded');
        var loadingScreen = document.getElementById('loadingScreen');
        if (loadingScreen) {
            loadingScreen.remove();
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', cleanup);
    } else {
        cleanup();
    }
})();

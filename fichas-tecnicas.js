/**
 * Catálogo interactivo de Fichas Técnicas — Prunavita
 * Visor PDF, descarga, resumen y lectura por voz (Web Speech API)
 */
(function () {
    'use strict';

    var FICHAS = [
        {
            id: 'cereza-iqf-prunavita',
            file: 'cereza-iqf-prunavita.pdf',
            category: 'cerezas',
            image: 'assets/images/productos/cerezas-descarozadas-iqf.jpg',
            icon: '🍒',
            title: { es: 'Cereza IQF PrunaVita', en: 'PrunaVita IQF Cherries' },
            summary: {
                es: 'Cerezas individuamente congeladas (IQF) de exportación. Especificaciones de calibre, color, defectos, humedad y parámetros microbiológicos para mercados internacionales.',
                en: 'Individually Quick Frozen (IQF) export cherries. Specifications for size, color, defects, moisture and microbiological parameters for international markets.'
            },
            tags: ['IQF', 'Exportación']
        },
        {
            id: 'cereza-descarozada-iqf',
            file: 'cereza-descarozada-iqf.pdf',
            category: 'cerezas',
            image: 'assets/images/productos/cerezas-descarozadas-iqf.jpg',
            icon: '🍒',
            title: { es: 'Cereza Descarozada IQF', en: 'Pitted IQF Cherries' },
            summary: {
                es: 'Cerezas descarozadas congeladas IQF. Producto listo para industria alimentaria, repostería y retail con control de calidad y trazabilidad.',
                en: 'Pitted IQF frozen cherries. Ready for food industry, bakery and retail with quality control and full traceability.'
            },
            tags: ['IQF', 'Descarozada']
        },
        {
            id: 'cerezas-descarozadas-pitted',
            file: 'cerezas-descarozadas-pitted.pdf',
            category: 'cerezas',
            image: 'assets/images/productos/cerezas-deshidratadas.jpg',
            icon: '🍒',
            title: { es: 'Cerezas Descarozadas (Pitted)', en: 'Pitted Cherries' },
            summary: {
                es: 'Ficha técnica de cerezas descarozadas para exportación. Incluye parámetros de calibre, color, textura y condiciones de almacenamiento.',
                en: 'Technical sheet for export pitted cherries. Includes size, color, texture parameters and storage conditions.'
            },
            tags: ['Pitted', 'Exportación']
        },
        {
            id: 'cerezas-sulfitadas-so2',
            file: 'cerezas-sulfitadas-so2.pdf',
            category: 'cerezas',
            image: 'assets/images/productos/ficha-cerezas-sulfitadas.jpg',
            icon: '🍒',
            title: { es: 'Cerezas Sulfitadas (SO₂)', en: 'Sulphited Cherries (SO₂)' },
            summary: {
                es: 'Cerezas tratadas con dióxido de azufre para conservación y estabilidad de color. Especificaciones de SO₂ residual, humedad y presentación comercial.',
                en: 'Cherries treated with sulphur dioxide for preservation and color stability. SO₂ residual, moisture and commercial presentation specs.'
            },
            tags: ['SO₂', 'Conservación']
        },
        {
            id: 'cerezas-frescas-camigo',
            file: 'cerezas-frescas-camigo.pdf',
            category: 'cerezas',
            image: 'assets/images/productos/cerezas-frescas.jpg',
            icon: '🍒',
            title: { es: 'Cerezas Frescas CAMIGO', en: 'CAMIGO Fresh Cherries' },
            summary: {
                es: 'Cerezas frescas de exportación bajo marca CAMIGO. Calibres, madurez, empaque y condiciones de frío para cadena de frío internacional.',
                en: 'Export fresh cherries under CAMIGO brand. Sizes, ripeness, packaging and cold chain conditions for international shipping.'
            },
            tags: ['Fresco', 'CAMIGO']
        },
        {
            id: 'cerezas-congeladas-camigo',
            file: 'cerezas-congeladas-camigo.pdf',
            category: 'cerezas',
            image: 'assets/images/productos/cerezas-congeladas.jpg',
            icon: '🍒',
            title: { es: 'Cerezas Congeladas CAMIGO', en: 'CAMIGO Frozen Cherries' },
            summary: {
                es: 'Cerezas congeladas IQF CAMIGO para industria y retail. Parámetros de congelación, defectos permitidos y vida útil en congelación.',
                en: 'CAMIGO IQF frozen cherries for industry and retail. Freezing parameters, allowed defects and frozen shelf life.'
            },
            tags: ['IQF', 'CAMIGO']
        },
        {
            id: 'cerezas-deshidratadas-camigo',
            file: 'cerezas-deshidratadas-camigo.pdf',
            category: 'cerezas',
            image: 'assets/images/productos/cerezas-deshidratadas.jpg',
            icon: '🍒',
            title: { es: 'Cerezas Deshidratadas CAMIGO', en: 'CAMIGO Dried Cherries' },
            summary: {
                es: 'Cerezas deshidratadas con humedad controlada. Ideal para snacks, repostería e ingredientes industriales con trazabilidad completa.',
                en: 'Dehydrated cherries with controlled moisture. Ideal for snacks, bakery and industrial ingredients with full traceability.'
            },
            tags: ['Deshidratada', 'CAMIGO']
        },
        {
            id: 'ciruela-natural-prunavita-cn',
            file: 'ciruela-natural-prunavita-cn.pdf',
            category: 'ciruelas',
            image: 'assets/images/productos/ciruelas-deshidratadas.jpg',
            icon: '🫐',
            title: { es: 'Ciruela Natural CN PrunaVita', en: 'PrunaVita Natural Prunes CN' },
            summary: {
                es: 'Ciruelas deshidratadas naturales sin aditivos (CN). Calibre, humedad, defectos y embalaje certificado para exportación a Asia, Europa y América.',
                en: 'Natural dried prunes without additives (CN). Size, moisture, defects and certified packaging for export to Asia, Europe and America.'
            },
            tags: ['Natural', 'Exportación']
        },
        {
            id: 'ciruela-pjc-prunavita',
            file: 'ciruela-pjc-prunavita.pdf',
            category: 'ciruelas',
            image: 'assets/images/productos/ciruelas-deshidratadas.jpg',
            icon: '🫐',
            title: { es: 'Ciruela PJC PrunaVita', en: 'PrunaVita PJC Prunes' },
            summary: {
                es: 'Ciruelas deshidratadas variedad D\'Agen línea PJC. Especificaciones de calibre, humedad, textura y condiciones de almacenamiento para mercados exigentes.',
                en: 'D\'Agen dried prunes PJC line. Size, moisture, texture and storage condition specifications for demanding markets.'
            },
            tags: ['PJC', 'D\'Agen']
        },
        {
            id: 'ciruela-tcc-prunavita',
            file: 'ciruela-tcc-prunavita.pdf',
            category: 'ciruelas',
            image: 'assets/images/productos/ciruelas-deshidratadas.jpg',
            icon: '🫐',
            title: { es: 'Ciruela TCC PrunaVita', en: 'PrunaVita TCC Prunes' },
            summary: {
                es: 'Ciruelas tiernizadas TCC con humedad ajustada a especificación del cliente. Producto premium chileno para retail e industria alimentaria.',
                en: 'TCC conditioned prunes with client-specified moisture. Premium Chilean product for retail and food industry.'
            },
            tags: ['TCC', 'Premium']
        },
        {
            id: 'ciruela-tsc-prunavita',
            file: 'ciruela-tsc-prunavita.pdf',
            category: 'ciruelas',
            image: 'assets/images/productos/ciruelas-deshidratadas.jpg',
            icon: '🫐',
            title: { es: 'Ciruela TSC PrunaVita', en: 'PrunaVita TSC Prunes' },
            summary: {
                es: 'Ciruelas deshidratadas línea TSC. Parámetros de calidad, calibre, humedad y certificaciones para cumplimiento normativo internacional.',
                en: 'TSC line dried prunes. Quality, size, moisture and certification parameters for international regulatory compliance.'
            },
            tags: ['TSC', 'Calidad']
        },
        {
            id: 'frutilla-iqf-prunavita',
            file: 'frutilla-iqf-prunavita.pdf',
            category: 'frutillas',
            image: 'assets/images/productos/frutillas-iqf.jpg',
            icon: '🍓',
            title: { es: 'Frutilla IQF PrunaVita', en: 'PrunaVita IQF Strawberries' },
            summary: {
                es: 'Frutillas individuamente congeladas IQF de exportación. Color, calibre, defectos, Brix y parámetros microbiológicos para mercados globales.',
                en: 'Export IQF individually frozen strawberries. Color, size, defects, Brix and microbiological parameters for global markets.'
            },
            tags: ['IQF', 'Exportación']
        },
        {
            id: 'frutilla-iqf-grado-ab',
            file: 'frutilla-iqf-grado-ab.pdf',
            category: 'frutillas',
            image: 'assets/images/productos/frutillas-iqf.jpg',
            icon: '🍓',
            title: { es: 'Frutilla IQF Grado A+B', en: 'IQF Strawberries Grade A+B' },
            summary: {
                es: 'Frutillas IQF grado A y B para industria y retail. Especificaciones detalladas de clasificación, defectos permitidos y presentación.',
                en: 'Grade A and B IQF strawberries for industry and retail. Detailed classification specs, allowed defects and presentation.'
            },
            tags: ['Grado A+B', 'IQF']
        },
        {
            id: 'pulpa-cerezas-camigo',
            file: 'pulpa-cerezas-camigo.pdf',
            category: 'pulpas',
            image: 'assets/images/productos/ficha-pulpa-cerezas.jpg',
            icon: '🧃',
            title: { es: 'Pulpa de Cerezas CAMIGO', en: 'CAMIGO Cherry Pulp' },
            summary: {
                es: 'Pulpa de cerezas para industria de jugos, confitería y alimentos procesados. Brix, acidez, color y parámetros de inocuidad.',
                en: 'Cherry pulp for juice, confectionery and processed food industry. Brix, acidity, color and food safety parameters.'
            },
            tags: ['Pulpa', 'CAMIGO']
        },
        {
            id: 'pulpa-ciruelas-camigo',
            file: 'pulpa-ciruelas-camigo.pdf',
            category: 'pulpas',
            image: 'assets/images/productos/ficha-pulpa-ciruelas.jpg',
            icon: '🧃',
            title: { es: 'Pulpa de Ciruelas CAMIGO', en: 'CAMIGO Prune Pulp' },
            summary: {
                es: 'Pulpa de ciruelas para industria alimentaria. Concentración, textura, color y especificaciones microbiológicas para exportación.',
                en: 'Prune pulp for food industry. Concentration, texture, color and microbiological specifications for export.'
            },
            tags: ['Pulpa', 'CAMIGO']
        }
    ];

    var PDF_BASE = 'assets/fichas-tecnicas/';
    var CATEGORY_IMAGES = {
        cerezas: 'assets/images/productos/cerezas-frescas.jpg',
        ciruelas: 'assets/images/productos/ciruelas-deshidratadas.jpg',
        frutillas: 'assets/images/productos/frutillas-iqf.jpg',
        pulpas: 'assets/images/productos/ficha-pulpa-cerezas.jpg'
    };
    var currentId = null;
    var speechUtterance = null;

    function getLang() {
        return document.documentElement.getAttribute('data-lang') || 'es';
    }

    function t(obj) {
        var lang = getLang();
        return obj[lang] || obj.es;
    }

    function trackEvent(action, label) {
        if (typeof gtag === 'function') {
            gtag('event', action, {
                event_category: 'fichas_tecnicas',
                event_label: label
            });
        }
    }

    function getFicha(id) {
        return FICHAS.find(function (f) { return f.id === id; });
    }

    function getFichaImage(ficha) {
        return ficha.image || CATEGORY_IMAGES[ficha.category] || 'assets/images/hero-prunes.jpg';
    }

    function renderList(filter) {
        var list = document.getElementById('fichasList');
        var count = document.getElementById('fichasCount');
        if (!list) return;

        var query = (filter && filter.query) ? filter.query.toLowerCase() : '';
        var category = (filter && filter.category) ? filter.category : 'all';

        var filtered = FICHAS.filter(function (f) {
            var matchCat = category === 'all' || f.category === category;
            var title = t(f.title).toLowerCase();
            var summary = t(f.summary).toLowerCase();
            var matchQuery = !query || title.indexOf(query) !== -1 || summary.indexOf(query) !== -1 || f.tags.join(' ').toLowerCase().indexOf(query) !== -1;
            return matchCat && matchQuery;
        });

        if (count) {
            count.textContent = filtered.length + ' ' + (getLang() === 'en' ? 'documents' : 'documentos');
        }

        list.innerHTML = filtered.map(function (f) {
            var active = f.id === currentId ? ' active' : '';
            var img = getFichaImage(f);
            return '<button type="button" class="ficha-card' + active + '" data-id="' + f.id + '" aria-pressed="' + (f.id === currentId) + '">' +
                '<div class="ficha-card-thumb" aria-hidden="true"><img src="' + img + '" alt="" loading="lazy"></div>' +
                '<div class="ficha-card-body">' +
                '<h3>' + t(f.title) + '</h3>' +
                '<p>' + t(f.summary).substring(0, 90) + '…</p>' +
                '<div class="ficha-card-meta">' + f.tags.map(function (tag) {
                    return '<span class="ficha-tag">' + tag + '</span>';
                }).join('') + '</div>' +
                '<span class="ficha-open-hint">' + (getLang() === 'en' ? 'Tap to view →' : 'Tocar para ver →') + '</span>' +
                '</div></button>';
        }).join('');

        list.querySelectorAll('.ficha-card').forEach(function (btn) {
            btn.addEventListener('click', function () {
                openFicha(btn.getAttribute('data-id'));
            });
        });
    }

    function stopSpeech() {
        if (window.speechSynthesis) {
            window.speechSynthesis.cancel();
        }
        document.querySelectorAll('.ficha-action-btn.speaking').forEach(function (b) {
            b.classList.remove('speaking');
        });
    }

    function speakSummary(ficha) {
        if (!window.speechSynthesis) {
            alert(getLang() === 'en' ? 'Your browser does not support text-to-speech.' : 'Su navegador no soporta lectura por voz.');
            return;
        }
        stopSpeech();
        var text = t(ficha.title) + '. ' + t(ficha.summary);
        speechUtterance = new SpeechSynthesisUtterance(text);
        speechUtterance.lang = getLang() === 'en' ? 'en-US' : 'es-CL';
        speechUtterance.rate = 0.95;
        var btn = document.getElementById('btnSpeak');
        if (btn) btn.classList.add('speaking');
        speechUtterance.onend = speechUtterance.onerror = function () {
            if (btn) btn.classList.remove('speaking');
        };
        window.speechSynthesis.speak(speechUtterance);
        trackEvent('ficha_listen', ficha.id);
    }

    function buildViewerHTML(ficha, isMobile) {
        var pdfUrl = PDF_BASE + ficha.file;
        var img = getFichaImage(ficha);
        var prefix = isMobile ? 'mobile-' : '';
        return '<div class="ficha-viewer-header">' +
            (isMobile ? '<button type="button" class="fichas-mobile-close" id="mobileClose" aria-label="Cerrar">✕</button>' : '') +
            '<div class="ficha-viewer-title-row">' +
            '<img class="ficha-viewer-thumb" src="' + img + '" alt="' + t(ficha.title) + '">' +
            '<h2>' + t(ficha.title) + '</h2></div>' +
            '<div class="ficha-viewer-actions">' +
            '<a href="' + pdfUrl + '" download class="ficha-action-btn primary" id="' + prefix + 'btnDownload">' +
            '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg>' +
            (getLang() === 'en' ? 'Download PDF' : 'Descargar PDF') + '</a>' +
            '<button type="button" class="ficha-action-btn" id="' + prefix + 'btnSpeak">' +
            '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/></svg>' +
            (getLang() === 'en' ? 'Listen summary' : 'Escuchar resumen') + '</button>' +
            '<a href="' + pdfUrl + '" target="_blank" rel="noopener" class="ficha-action-btn">' +
            '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6M15 3h6v6M10 14L21 3"/></svg>' +
            (getLang() === 'en' ? 'Open in new tab' : 'Abrir en pestaña') + '</a>' +
            '</div></div>' +
            '<div class="ficha-summary-box"><h3>' + (getLang() === 'en' ? 'Summary' : 'Resumen') + '</h3><p>' + t(ficha.summary) + '</p></div>' +
            '<div class="ficha-pdf-frame-wrap"><iframe class="ficha-pdf-frame" src="' + pdfUrl + '#view=FitH" title="' + t(ficha.title) + '"></iframe></div>';
    }

    function bindViewerActions(ficha, isMobile) {
        var prefix = isMobile ? 'mobile-' : '';
        var dl = document.getElementById(prefix + 'btnDownload');
        var speak = document.getElementById(prefix + 'btnSpeak');
        if (dl) {
            dl.addEventListener('click', function () {
                trackEvent('ficha_download', ficha.id);
            });
        }
        if (speak) {
            speak.addEventListener('click', function () {
                if (speak.classList.contains('speaking')) {
                    stopSpeech();
                } else {
                    speakSummary(ficha);
                }
            });
        }
        if (isMobile) {
            var close = document.getElementById('mobileClose');
            if (close) {
                close.addEventListener('click', function () {
                    stopSpeech();
                    document.getElementById('fichasMobileViewer').classList.remove('open');
                    document.body.style.overflow = '';
                });
            }
        }
    }

    function openFicha(id) {
        var ficha = getFicha(id);
        if (!ficha) return;
        currentId = id;
        stopSpeech();
        renderList(getCurrentFilter());

        var panel = document.getElementById('fichaViewerPanel');
        if (panel) {
            panel.innerHTML = buildViewerHTML(ficha, false);
            bindViewerActions(ficha, false);
        }

        if (window.innerWidth <= 960) {
            var mobile = document.getElementById('fichasMobileViewer');
            if (mobile) {
                mobile.innerHTML = buildViewerHTML(ficha, true);
                mobile.classList.add('open');
                document.body.style.overflow = 'hidden';
                bindViewerActions(ficha, true);
            }
        }

        trackEvent('ficha_view', ficha.id);

        if (panel) {
            panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
    }

    function getCurrentFilter() {
        var search = document.getElementById('fichasSearch');
        var activeFilter = document.querySelector('.ficha-filter-btn.active');
        return {
            query: search ? search.value : '',
            category: activeFilter ? activeFilter.getAttribute('data-category') : 'all'
        };
    }

    function init() {
        var search = document.getElementById('fichasSearch');
        var filters = document.querySelectorAll('.ficha-filter-btn');

        renderList({ category: 'all' });

        if (search) {
            search.addEventListener('input', function () {
                renderList(getCurrentFilter());
            });
        }

        filters.forEach(function (btn) {
            btn.addEventListener('click', function () {
                filters.forEach(function (b) { b.classList.remove('active'); });
                btn.classList.add('active');
                renderList(getCurrentFilter());
            });
        });

        var params = new URLSearchParams(window.location.search);
        var fichaParam = params.get('ficha');
        if (fichaParam && getFicha(fichaParam)) {
            openFicha(fichaParam);
        }

        document.addEventListener('languageChanged', function () {
            renderList(getCurrentFilter());
            if (currentId) openFicha(currentId);
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();

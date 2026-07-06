# Estrategia Baidu y Mercado Chino — Prunavita.cl

**Objetivo:** que compradores chinos de ciruelas deshidratadas y productos agroindustriales
chilenos encuentren a Prunavita. Activación en **meses 4–5** (septiembre–octubre 2026), con preparación en meses 2–3.

## Contexto clave (realidad del SEO en China)

1. **Baidu ≈ 60-70% del buscador en China**, pero el B2B chino real ocurre además en
   WeChat, Alibaba/1688, Made-in-China y ferias. La estrategia debe ser mixta.
2. Baidu indexa y posiciona mejor: contenido en **chino simplificado**, sitios **rápidos desde China**,
   HTML simple (✅ ya lo tenemos), y dominios con historial. Un `.cl` puede posicionar, pero compite
   en desventaja frente a `.cn`/`.com.cn` (que requieren licencia ICP y entidad legal en China).
3. Sin licencia ICP no se puede hostear en China continental; alternativa práctica: **CDN con nodos
   en Hong Kong/Singapur** para mejorar velocidad percibida desde China.
4. Baidu da poco peso a JSON-LD; prioriza **meta tags clásicos, títulos y contenido textual en chino**.

## Fase 0 — Preparación (Meses 1–3: jun–ago 2026)

- [x] HTML estático y liviano (carga rápido, sin dependencias bloqueadas en China,
      OJO: Google Fonts puede cargar lento desde China → evaluar self-host de fuentes en fase 5).
- [x] `robots.txt` permite explícitamente `Baiduspider`.
- [ ] Incluir términos semilla en chino en páginas clave (ya hay 智利西梅 en la página de ciruelas).
- [ ] Recopilar vocabulario comercial: 智利西梅干 (ciruelas pasas chilenas), 智利干果 (frutos secos
      chilenos), 智利供应商 (proveedor chileno), 农产品出口 (exportación agrícola).

## Fase 1 — Activación (Meses 4–5: sep–oct 2026)

1. **Página pilar en chino simplificado:** `/zh/ciruelas-deshidratadas.html` (o `/zh/xilimei.html`)
   - Title y description en chino, contenido original (no traducción literal del español).
   - Datos de contacto con WeChat ID (pedir al cliente crear cuenta WeChat).
   - hreflang `zh-Hans` ↔ `es-CL` ↔ `en`.
2. **Registro en Baidu Webmaster Tools (百度搜索资源平台):** requiere cuenta Baidu; verificar
   sitio y enviar sitemap específico de páginas /zh/.
3. **Presencia B2B paralela** (mayor ROI a corto plazo que Baidu orgánico):
   - Perfil en Alibaba.com / Made-in-China.com con link a prunavita.cl (backlinks + leads directos).
   - Considerar mini-perfil en 1688 si hay socio local.
4. **Velocidad:** medir desde China (herramientas: Dotcom-tools, 17ce.com) y decidir si conviene
   CDN con nodo HK o self-host de fuentes.

## Fase 2 — Crecimiento (post mes 6, propuesta siguiente etapa)

- Más páginas /zh/ (representación comercial para importadores chinos).
- Artículos en plataformas chinas (Zhihu, Baijiahao) que enlacen/mencionen la marca.
- Evaluar Baidu Ads (百度推广) — requiere entidad o agencia intermediaria.
- Evaluar dominio .com con versión china dedicada si el canal demuestra tracción.

## Métricas del canal chino

| Métrica | Meta mes 6 |
|---|---|
| Página /zh/ publicada e indexada en Baidu | ✔ |
| Consultas de compradores chinos (form/WeChat/email) | ≥ 2 |
| Perfil B2B activo con catálogo | ✔ |

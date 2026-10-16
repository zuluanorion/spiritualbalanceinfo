# -*- coding: utf-8 -*-
"""Generate spiritualbalanceinfo.com: English at /, Spanish at /es/. Output: ../web/public
Sister site of theflamecodex.com — same design family, linked both ways."""
import os, shutil, builtins
HERE = os.path.dirname(os.path.abspath(__file__))
# Two layouts: the workshop (../web/assets holds the images, ../web/public is rebuilt from scratch)
# and the GitHub repository (webgen/ next to public/, whose images and PDFs stay in place).
WORKSHOP = os.path.isdir(os.path.join(HERE, '..', 'web', 'assets'))
OUT = os.path.join(HERE, '..', 'web', 'public') if WORKSHOP else os.path.join(HERE, '..', 'public')
IMG_SRC = os.path.join(HERE, '..', 'web', 'assets', 'img')
DOMAIN = 'https://www.spiritualbalanceinfo.com'
FC = 'https://www.theflamecodex.com'

PAGES = ['', 'quantum-transformation', 'ayurveda', 'energy', 'evaluations', 'about', 'books', 'retreats', 'contact']
NAV = {
 'en': {'': 'Home', 'quantum-transformation': 'Quantum Transformation', 'ayurveda': 'Ayurveda', 'energy': 'Energy Therapies', 'evaluations': 'Evaluations', 'about': 'Dr. Orion & Grace', 'books': 'Books', 'retreats': 'Journeys & Retreats', 'contact': 'Visit'},
 'es': {'': 'Inicio', 'quantum-transformation': 'Transformación Cuántica', 'ayurveda': 'Ayurveda', 'energy': 'Terapias Energéticas', 'evaluations': 'Evaluaciones', 'about': 'Dr. Orion y Grace', 'books': 'Libros', 'retreats': 'Viajes y Retiros', 'contact': 'Visítanos'},
}
TITLES = {
 'en': {'': 'Spiritual Balance — Dr. Zuluan Orion · Weston, Florida', 'quantum-transformation': 'Quantum Transformation — Dr. Zuluan Orion', 'ayurveda': 'Ayurveda, Panchakarma and Rasayana — Spiritual Balance', 'energy': 'Bioresonance and Biofeedback — Spiritual Balance', 'evaluations': 'Live Blood Analysis and Energy Evaluations — Spiritual Balance', 'about': 'Dr. Zuluan Orion — Spiritual Balance', 'books': 'Books by Dr. Zuluan Orion', 'retreats': 'Holistic Journeys and Retreats with Dr. Zuluan Orion — Thailand and India', 'contact': 'Visit Spiritual Balance — Weston, Florida'},
 'es': {'': 'Spiritual Balance — Dr. Zuluan Orion · Weston, Florida', 'quantum-transformation': 'Transformación Cuántica — Dr. Zuluan Orion', 'ayurveda': 'Ayurveda, Panchakarma y Rasayana — Spiritual Balance', 'energy': 'Biorresonancia y Biofeedback — Spiritual Balance', 'evaluations': 'Análisis de sangre en vivo y evaluaciones energéticas — Spiritual Balance', 'about': 'Dr. Zuluan Orion — Spiritual Balance', 'books': 'Libros del Dr. Zuluan Orion', 'retreats': 'Viajes y Retiros Holísticos con el Dr. Zuluan Orion — Tailandia e India', 'contact': 'Visita Spiritual Balance — Weston, Florida'},
}
DESC = {
 'en': 'Spiritual Balance, Weston, Florida. Dr. Zuluan Orion, originator of Quantum Transformation and cognizer of the Light Codes, guides the soul to purify, unblock its energy and reconnect with the Spirit, supported by Ayurveda, Panchakarma, Rasayana, bioresonance and biofeedback.',
 'es': 'Spiritual Balance, Weston, Florida. El Dr. Zuluan Orion, originador de la Transformación Cuántica y cognizador de los Códigos de Luz, guía al alma a depurarse, desbloquear su energía y reconectar con el Espíritu, con el apoyo de la Ayurveda, el Panchakarma, el Rasayana, la biorresonancia y el biofeedback.',
}

def url(lang, page):
    base = '/es/' if lang == 'es' else '/'
    return base + (page + '/' if page else '')

def fc(lang, page=''):
    return FC + url(lang, page)

def S(n): return '/assets/img/sigil_%02d.png' % n

def head(lang, page):
    other = 'es' if lang == 'en' else 'en'
    navlinks = ''.join('<a href="%s"%s>%s</a>' % (url(lang, p), ' class="on"' if p == page else '', NAV[lang][p]) for p in PAGES)
    navlinks += '<a class="fc" href="https://drzuluanorion.org%s">Dr. Zuluan Orion ↗</a>' % ('/es/' if lang == 'es' else '/')
    navlinks += '<a class="lang" href="%s" hreflang="%s">%s</a>' % (url(other, page), other, 'Español' if lang == 'en' else 'English')
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLES[lang][page]}</title>
<meta name="description" content="{DESC[lang]}">
<link rel="canonical" href="{DOMAIN}{url(lang, page)}">
<link rel="alternate" hreflang="en" href="{DOMAIN}{url('en', page)}">
<link rel="alternate" hreflang="es" href="{DOMAIN}{url('es', page)}">
<meta property="og:title" content="{TITLES[lang][page]}">
<meta property="og:description" content="{DESC[lang]}">
<meta property="og:image" content="{DOMAIN}/assets/img/zuluan_tuning_forks.jpg">
<link rel="icon" href="/assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"HealthAndBeautyBusiness","name":"Spiritual Balance","url":"{DOMAIN}","image":"{DOMAIN}/assets/img/clinic_buddha_waiting_room.jpg","telephone":"+1-954-668-0348","email":"spiritualbalanceinfo@gmail.com","address":{{"@type":"PostalAddress","streetAddress":"1565 North Park Drive, Suite 101","addressLocality":"Weston","addressRegion":"FL","postalCode":"33326","addressCountry":"US"}},"founder":{{"@type":"Person","name":"Dr. Zuluan Orion","url":"https://drzuluanorion.org/"}},"sameAs":["https://drzuluanorion.org/","{FC}","https://www.instagram.com/drzuluanorion/","https://www.facebook.com/zuluanorion/"]}}</script>
</head>
<body>
<header class="site"><div class="wrap">
<a class="brand" href="{url(lang, '')}">SPIRITUAL BALANCE</a>
<button class="menu-btn" onclick="document.querySelector('nav.main').classList.toggle('open')">{'MENU' if lang == 'en' else 'MENÚ'}</button>
<nav class="main">{navlinks}</nav>
</div></header>
<main>
'''

def foot(lang):
    t = {'en': ('Guiding the soul back to its own light.', 'Sister sites', 'The Flame Codex — the sacred language and the Light Codes', 'Dr. Zuluan Orion — the author, his story and his teaching'),
         'es': ('Guiando al alma de regreso a su propia luz.', 'Sitios hermanos', 'El Códice de la Llama — el lenguaje sagrado y los Códigos de Luz', 'Dr. Zuluan Orion — el autor, su historia y su enseñanza')}[lang]
    return f'''</main>
<footer class="site"><div class="wrap">
<a class="brand" href="{url(lang, '')}">SPIRITUAL BALANCE</a>
<p>{t[0]}</p>
<p>1565 North Park Drive, Suite 101 · Weston, Florida 33326 · <a href="tel:+19546680348">(954) 668-0348</a> · <a href="mailto:spiritualbalanceinfo@gmail.com">spiritualbalanceinfo@gmail.com</a></p>
<p><a href="{'/assets/docs/Catalogo_Spiritual_Balance.pdf' if lang == 'en' else '/assets/docs/Catalogo_Spiritual_Balance_ES.pdf'}" download>{'Download our catalogue (PDF)' if lang == 'en' else 'Descarga nuestro catálogo (PDF)'}</a></p>
<p>{t[1]}: <a href="https://drzuluanorion.org{'/es/' if lang == 'es' else '/'}">{t[3]}</a> · <a href="{fc(lang)}">{t[2]}</a></p>
<p>© 2026 Dr. Zuluan Orion · <a href="https://www.instagram.com/drzuluanorion/">Instagram</a> · <a href="https://www.facebook.com/zuluanorion/">Facebook</a> · <a href="https://www.youtube.com/channel/UCM42zxWtUt1xK4cp1bLl1uw">YouTube</a></p>
</div></footer>
</body>
</html>
'''

def hero(title, sub, lede='', sig=1, page=True, btns='', kicker='', img=None):
    return f'''<section class="hero{' page' if page else ' home'}"><div class="wrap">
<img class="sig{' logo' if img else ''}" src="{img or S(sig)}" alt="{'Spiritual Balance' if img else ''}">
{f'<p class="kicker">{kicker}</p>' if kicker else ''}<h1>{title}</h1>
<p class="sub">{sub}</p>
{f'<p class="lede">{lede}</p>' if lede else ''}
{btns}
</div></section>
'''

builtins.url = url; builtins.fc = fc; builtins.S = S; builtins.hero = hero
from content import BODY

def build():
    if WORKSHOP:
        if os.path.exists(OUT): shutil.rmtree(OUT)
        os.makedirs(os.path.join(OUT, 'assets'))
        shutil.copytree(IMG_SRC, os.path.join(OUT, 'assets', 'img'))
        shutil.copytree(os.path.join(HERE, '..', 'web', 'assets', 'docs'), os.path.join(OUT, 'assets', 'docs'))
    else:
        os.makedirs(os.path.join(OUT, 'assets'), exist_ok=True)
    shutil.copy(os.path.join(HERE, 'style.css'), os.path.join(OUT, 'assets', 'style.css'))
    for lang in ('en', 'es'):
        for page in PAGES:
            d = os.path.join(OUT, 'es' if lang == 'es' else '', page)
            os.makedirs(d, exist_ok=True)
            open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(head(lang, page) + BODY[lang][page] + foot(lang))
    open(os.path.join(OUT, '404.html'), 'w', encoding='utf-8').write(head('en', '') + hero('Not found', 'This page does not exist. <a href="/" style="color:#E9D5A6">Return home</a> · <a href="/es/" style="color:#E9D5A6">Volver al inicio</a>') + foot('en'))
    sm = ''.join('<url><loc>%s%s</loc></url>' % (DOMAIN, url(l, p)) for l in ('en', 'es') for p in PAGES)
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s</urlset>' % sm)
    open(os.path.join(OUT, 'robots.txt'), 'w').write('User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n' % DOMAIN)
    print('built', OUT)

if __name__ == '__main__':
    build()

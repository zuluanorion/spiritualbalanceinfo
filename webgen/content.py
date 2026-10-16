# -*- coding: utf-8 -*-
# Page bodies for spiritualbalanceinfo.com. url(), fc(), S(), hero() are injected by build.py.
# Voice: Dr. Zuluan Orion speaking to the reader, first person. No external references.
BODY = {'en': {}, 'es': {}}
I = '/assets/img/'
BK = '/assets/img/books/'

def book(img, title, line='', tag=''):
    top = f'<img src="{BK}{img}.webp?v=3d" alt="{title}" loading="lazy">' if img else f'<div class="ph" style="aspect-ratio:2/3;max-height:340px">{title}</div>'
    return f'<div class="book">{top}<div class="t">{f"<span class=tag>{tag}</span>" if tag else ""}<h4>{title}</h4>{f"<p>{line}</p>" if line else ""}</div></div>'

def gallery(files, cls=''):
    return f'<div class="gallery {cls}">' + ''.join(f'<img src="{I}{f}" alt="" loading="lazy">' for f in files) + '</div>'


TESTI = [
 ("Conocer a Zulu es una gran bendición en mi vida y en la de mi familia.", "Knowing Zulu is a great blessing in my life and in my family's.", "Astrid Ramírez", "Ecuador"),
 ("Zuluan ha sido, es y seguirá siendo un mentor.", "Zuluan has been, is and will always be a mentor.", "Gina Moreno", "Colombia"),
 ("Conocí a Zuluan en un momento difícil de mi vida.", "I met Zuluan at a difficult moment in my life.", "Jennifer Peterson Hunter", "USA"),
 ("En mis años de formación con Zuluan, he transformado mi vida y mi visión de ella, me siento plena y con propósito.", "In my years of training with Zuluan I have transformed my life and the way I see it. I feel whole and full of purpose.", "Diana Collazos", "Colombia"),
 ("Conocer a el Dr Zuluan ha sido de un beneficio tremendo para mí en todo nivel.", "Meeting Dr. Zuluan has been a tremendous benefit to me on every level.", "Sangudy Lowe", "Miami"),
 ("Zuluan is awakened amazing Being.", "", "Kuro", "Hawaii"),
]

def testimonials(lang):
    h = {'en': ('IN THEIR WORDS', 'What people say'), 'es': ('EN SUS PALABRAS', 'Lo que dicen')}[lang]
    cards = ''
    for es, en, name, place in TESTI:
        main = es if (lang == 'es' or not en) else es
        tr = f'<p class="note" style="margin-top:6px">{en}</p>' if (lang == 'en' and en) else ''
        cards += f'<div class="card"><blockquote style="margin:0 0 10px;font-size:21px">“{main}”</blockquote>{tr}<p class="eyebrow" style="margin:12px 0 0">{name} · {place}</p></div>'
    return f'<section class="lav"><div class="wrap"><p class="eyebrow center">{h[0]}</p><h2 class="center">{h[1]}</h2><div class="grid3" style="margin-top:30px">{cards}</div></div></section>\n'

GRACE_ES = ["Soy Grace Orion, graduada en Psicología de Florida International University (FIU), especializada en Transformación Cuántica, Maestra de Reiki, conferencista y autora. Mi vocación es acompañar a las personas a comprender su mundo interior, reconocer los patrones que influyen en su vida y desarrollar una relación más consciente consigo mismas.",
"En mis sesiones trabajo con emociones, creencias y experiencias que pueden influir en la manera en que una persona se percibe, se relaciona y enfrenta sus desafíos. Acompaño procesos de autoconocimiento, manejo del estrés, fortalecimiento de la autoestima y transformación de patrones emocionales, así como momentos de cambio en los que se necesita claridad, orientación y un espacio de escucha.",
"La Transformación Cuántica es el eje de mi práctica. Desde este enfoque, integro la dimensión emocional, física, energética y espiritual como aspectos interrelacionados de la experiencia humana. Mi propósito es que cada persona pueda comprender lo que está viviendo, reconocer sus recursos internos y llevar esa comprensión a cambios concretos en su vida cotidiana.",
"Mi formación en psicología se complementa con más de 30 años de experiencia en Reiki y meditación, además de formación en biofeedback y bioresonancia. Estas herramientas se incorporan de acuerdo con las necesidades y los objetivos de cada proceso, dentro de un acompañamiento cercano y personalizado.",
"Como co-directora de Spiritual Balance, trabajo junto al Dr. Zuluan Orion en una propuesta de bienestar integral. Mi labor se enfoca especialmente en el acompañamiento emocional y el desarrollo de la conciencia personal, ofreciendo un espacio para explorar aquello que necesita atención y cultivar mayor equilibrio, autonomía y sentido de vida."]
GRACE_EN = ["I am Grace Orion, a Psychology graduate of Florida International University (FIU), specialized in Quantum Transformation, a Reiki Master, speaker and author. My calling is to accompany people as they come to understand their inner world, recognize the patterns that shape their lives, and develop a more conscious relationship with themselves.",
"In my sessions I work with the emotions, beliefs and experiences that can influence how a person sees themselves, relates to others and meets their challenges. I accompany processes of self-knowledge, stress management, strengthening self-esteem and transforming emotional patterns, as well as moments of change that call for clarity, guidance and a space to be heard.",
"Quantum Transformation is the axis of my practice. From this approach I integrate the emotional, physical, energetic and spiritual dimensions as interrelated aspects of human experience. My purpose is for each person to understand what they are living through, recognize their inner resources, and carry that understanding into concrete changes in their daily life.",
"My training in psychology is complemented by more than 30 years of experience in Reiki and meditation, as well as training in biofeedback and bioresonance. These tools are brought in according to the needs and goals of each process, within close and personalized accompaniment.",
"As co-director of Spiritual Balance, I work alongside Dr. Zuluan Orion in an integral approach to well-being. My work focuses especially on emotional accompaniment and the development of personal awareness, offering a space to explore what needs attention and to cultivate greater balance, autonomy and meaning in life."]

def grace_home(lang):
    t = {'en': ('CO-DIRECTOR', 'Grace Orion', 'Psychology (FIU) · Quantum Transformation · Reiki Master', GRACE_EN[0], 'Read more'),
         'es': ('CO-DIRECTORA', 'Grace Orion', 'Psicología (FIU) · Transformación Cuántica · Maestra de Reiki', GRACE_ES[0], 'Leer más')}[lang]
    return f'''<section><div class="wrap grid2">
<div>
<p class="eyebrow">{t[0]}</p>
<h2>{t[1]}</h2>
<p class="note" style="font-style:normal;color:var(--violet);font-family:var(--caps);letter-spacing:.06em;font-size:15px">{t[2]}</p>
<p class="lead">{t[3]}</p>
<p><a class="btn" href="{url(lang,'about')}#grace">{t[4]}</a></p>
</div>
<figure><img class="portrait" src="/assets/img/team_woman_portrait.jpg" alt="Grace Orion" style="max-height:620px;width:auto;margin:0 auto"></figure>
</div></section>
'''

def grace_about(lang):
    t = {'en': ('CO-DIRECTOR OF SPIRITUAL BALANCE', 'Psychology (FIU) · Quantum Transformation · Reiki Master · Speaker and author', GRACE_EN, 'HER BOOK', 'RECOGNITION', 'Honored by Lifestyle Plus Magazine for her work with women and young people in personal transformation and Quantum Transformation.'),
         'es': ('CO-DIRECTORA DE SPIRITUAL BALANCE', 'Psicología (FIU) · Transformación Cuántica · Maestra de Reiki · Conferencista y autora', GRACE_ES, 'SU LIBRO', 'RECONOCIMIENTO', 'Premiada por Lifestyle Plus Magazine por su trabajo con las mujeres y con la juventud en transformación personal y Transformación Cuántica.')}[lang]
    paras = ''.join(f'<p{" class=lead" if i == 0 else ""}>{p}</p>' for i, p in enumerate(t[2]))
    return f'''<section class="lav" id="grace"><div class="wrap grid2 top">
<figure><img class="portrait" src="/assets/img/team_woman_portrait.jpg" alt="Grace Orion"></figure>
<div>
<p class="eyebrow">{t[0]}</p>
<h2>Grace Orion</h2>
<p style="color:var(--violet);font-family:var(--caps);letter-spacing:.06em;font-size:15px">{t[1]}</p>
{paras}
<div style="display:flex;gap:22px;align-items:center;margin-top:26px;flex-wrap:wrap">
<img src="/assets/img/books/grace_el_retorno_de_mi_alma.webp" alt="El retorno de mi alma" style="width:150px;filter:drop-shadow(0 14px 18px rgba(30,26,22,.3))">
<div><p class="eyebrow" style="margin:0">{t[3]}</p><h3 style="margin:4px 0 2px">El retorno de mi alma</h3><p style="font-style:italic;margin:0">Cuando el mundo pesa, el alma guía</p></div>
</div>
<div style="display:flex;gap:22px;align-items:center;margin-top:30px;flex-wrap:wrap">
<img src="/assets/img/grace_award_lifestyle.jpg" alt="Grace Orion, Lifestyle Plus Awards" loading="lazy" style="width:190px;aspect-ratio:3/4;object-fit:cover;border:1px solid rgba(200,164,92,.55);box-shadow:0 14px 26px -14px rgba(30,26,22,.5)">
<div style="flex:1;min-width:220px"><p class="eyebrow" style="margin:0">{t[4]}</p><h3 style="margin:4px 0 6px">Lifestyle Plus Awards</h3><p style="margin:0">{t[5]}</p></div>
</div>
</div>
</div></section>
'''


def trip(lang, eyebrow, title, place, paras, stops):
    st = ''.join(f'<li>{s}</li>' for s in stops)
    return f'''<div class="card" style="padding:34px 32px">
<p class="eyebrow">{eyebrow}</p>
<h3 style="margin-top:4px">{title}</h3>
<p style="font-family:var(--caps);letter-spacing:.08em;font-size:14px;color:var(--gold)">{place}</p>
{''.join(f'<p>{p}</p>' for p in paras)}
<ul class="benefits" style="columns:1">{st}</ul>
</div>'''

def retreats(lang):
    if lang == 'en':
        T = dict(intro1="For almost two decades I lived and studied in Asia: twelve and a half years in India and eight in Thailand. Those lands shaped my path: the temples, the masters, the healers, the silence. Now I open those doors to small groups who want to live the journey from the inside.",
                 intro2="These are not tourist trips. They are pilgrimages of the soul: meditation in sacred places, encounters with living traditions, Quantum Transformation along the way, and time to integrate what opens.",
                 up="JUNE 2027", uph="Upcoming journeys", f_e="THAILAND · CHIANG MAI · JUNE 2027", f_t="A spiritual journey through the temples and sacred places of Northern Thailand", f_p="Temples of the Lanna tradition, mountains and waterfalls, meditation with the monks, and the healer Pakkapron, who has channeled the Medicine Buddha for more than thirty years. Places are limited.", f_dl="Download the journey guide",
                 th_e="THAILAND · JUNE 2027", th_t="Holistic retreat in Chiang Mai", th_p="Chiang Mai · Northern Thailand",
                 th=["In the mountains of northern Thailand, among Buddhist temples and forest, we live a holistic retreat of meditation, healing and inner silence.",
                     "One of the heart moments of this journey is our visit to Pakkapron, a very special healer from Chiang Mai who has channeled the Medicine Buddha for more than thirty years, offering healing, Dharma teaching and spiritual guidance. Being in her presence is an experience that stays with you."],
                 th_s=["Meditation in Buddhist temples", "Visit to Pakkapron, who has channeled the Medicine Buddha for more than 30 years", "Quantum Transformation sessions during the journey", "Thai healing traditions, nature and silence"],
                 in_e="INDIA · JUNE 2027", in_t="Pilgrimage to Northern India", in_p="Vrindavan · Mathura · Agra (Taj Mahal) · Jaipur",
                 ind=["A journey through the sacred sites of Northern India, to have a deep spiritual experience and connect with the energy these places have held for thousands of years.",
                      "Along the way we live the activation of the Light Codes: the sacred language of the Flame Codex, received in the places where the soul remembers."],
                 in_s=["Vrindavan and Mathura, the land of Krishna", "The Taj Mahal in Agra", "Jaipur, the pink city", "Temples, meditation and ceremonies in Northern India", "Activation of the Light Codes"],
                 past="WITH THE GROUPS", pasth="Our journeys to Thailand, 2025 and 2026", pastp="In 2025 and 2026 we travelled to Thailand with groups who lived this experience with us: the temples and sacred places of the north, the mountains and waterfalls, the hill-tribe villages, and the healer Pakkapron.",
                 pake="THE HEALER OF CHIANG MAI", pakp="Born in 1946 in the village of Namjum, in the hills of Chiang Mai, Pakkapron discovered her gift when a young girl suffering from seizures arrived at her door. Since then, for more than three decades, she has channeled the energy of the Medicine Buddha to heal, to teach the Dharma and to offer spiritual guidance, freely, to thousands of people from around the world.", pakcap="Dr. Zuluan Orion with Pakkapron in Chiang Mai.", g1="An incorruptible monk of Northern Thailand.", g2="Monks caring for the body of an incorruptible master.", gh="Our groups in Thailand, 2025 and 2026",
                 pdf="Spiritual_Journey_Thailand_EN.pdf", dl="DOWNLOAD THE THAILAND JOURNEY GUIDE (PDF)", dln="PDF · 9 MB",
                 cta="Places are limited. Call for more information and to reserve your place.", call="Call (954) 668-0348", mail="Write to us",
                 fc="The Light Codes that we activate on these journeys are born from the Flame Codex.", fcl="Discover the Flame Codex ↗")
    else:
        T = dict(intro1="Durante casi dos décadas viví y estudié en Asia: doce años y medio en la India y ocho en Tailandia. Esas tierras formaron mi camino: los templos, los maestros, los sanadores, el silencio. Ahora abro esas puertas a grupos pequeños que quieren vivir el viaje desde adentro.",
                 intro2="No son viajes de turismo. Son peregrinaciones del alma: meditación en lugares sagrados, encuentros con tradiciones vivas, Transformación Cuántica en el camino, y tiempo para integrar lo que se abre.",
                 up="JUNIO 2027", uph="Próximos viajes", f_e="TAILANDIA · CHIANG MAI · JUNIO 2027", f_t="Un viaje espiritual por los templos y lugares sagrados del Norte de Tailandia", f_p="Templos de la tradición Lanna, montañas y cascadas, meditación con los monjes, y la sanadora Pakkapron, que canaliza al Buda de la Medicina desde hace más de treinta años. Cupos limitados.", f_dl="Descargar la guía del viaje",
                 th_e="TAILANDIA · JUNIO 2027", th_t="Retiro holístico en Chiang Mai", th_p="Chiang Mai · Norte de Tailandia",
                 th=["En las montañas del norte de Tailandia, entre templos budistas y bosque, vivimos un retiro holístico de meditación, sanación y silencio interior.",
                     "Uno de los momentos del corazón de este viaje es la visita a Pakkapron, una sanadora muy especial de Chiang Mai que canaliza al Buda de la Medicina desde hace más de treinta años, ofreciendo sanación, enseñanza del Dharma y guía espiritual. Estar en su presencia es una experiencia que se queda contigo."],
                 th_s=["Meditación en templos budistas", "Visita a Pakkapron, que canaliza al Buda de la Medicina desde hace más de 30 años", "Sesiones de Transformación Cuántica durante el viaje", "Tradiciones de sanación tailandesas, naturaleza y silencio"],
                 in_e="INDIA · JUNIO 2027", in_t="Peregrinación al Norte de la India", in_p="Vrindavan · Mathura · Agra (Taj Mahal) · Jaipur",
                 ind=["Un recorrido por los lugares sagrados del norte de la India, para tener una vivencia espiritual muy profunda y conectar con la energía que esos lugares han sostenido durante miles de años.",
                      "En el camino vivimos la activación de los Códigos de Luz: el lenguaje sagrado del Códice de la Llama, recibido en los lugares donde el alma recuerda."],
                 in_s=["Vrindavan y Mathura, la tierra de Krishna", "El Taj Mahal en Agra", "Jaipur, la ciudad rosa", "Templos, meditación y ceremonias en el norte de la India", "Activación de los Códigos de Luz"],
                 past="CON LOS GRUPOS", pasth="Nuestros viajes a Tailandia, 2025 y 2026", pastp="En 2025 y 2026 viajamos a Tailandia con grupos que vivieron esta experiencia con nosotros: los templos y lugares sagrados del norte, las montañas y cascadas, las aldeas de las montañas y la sanadora Pakkapron.",
                 pake="LA SANADORA DE CHIANG MAI", pakp="Nacida en 1946 en el pueblo de Namjum, en las montañas de Chiang Mai, Pakkapron descubrió su don cuando una niña que sufría convulsiones llegó a su puerta. Desde entonces, por más de tres décadas, canaliza la energía del Buda de la Medicina para sanar, enseñar el Dharma y ofrecer guía espiritual, sin costo, a miles de personas de todo el mundo.", pakcap="El Dr. Zuluan Orion con Pakkapron en Chiang Mai.", g1="Un monje incorrupto del Norte de Tailandia.", g2="Monjes cuidando el cuerpo de un maestro incorrupto.", gh="Nuestros grupos en Tailandia, 2025 y 2026",
                 pdf="Viaje_Espiritual_por_Tailandia.pdf", dl="DESCARGAR LA GUÍA DEL VIAJE A TAILANDIA (PDF)", dln="PDF · 18 MB",
                 cta="Los cupos son limitados. Llama para más información y para reservar tu lugar.", call="Llamar (954) 668-0348", mail="Escríbenos",
                 fc="Los Códigos de Luz que activamos en estos viajes nacen del Códice de la Llama.", fcl="Conoce el Códice de la Llama ↗")
    return f'''<section class="ba" style="padding:0;text-align:left"><div style="position:relative">
<img src="/assets/img/viajes/grupo_01.jpg" alt="Wat Phra That Doi Suthep, Chiang Mai" style="width:100%;height:min(70vh,620px);object-fit:cover;object-position:center 35%;display:block;opacity:.5">
<div class="wrap" style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;max-width:1120px">
<p class="eyebrow" style="color:var(--gold2)">{T['f_e']}</p>
<h2 style="font-size:clamp(30px,5vw,54px);margin:0 0 12px">{T['f_t']}</h2>
<p style="font-size:clamp(18px,2.2vw,24px);max-width:640px;color:#F1E9FA">{T['f_p']}</p>
<p><a class="btn solid" href="tel:+19546680348">{T['call']}</a> <a class="btn" style="background:rgba(23,19,42,.5)" href="/assets/docs/{T['pdf']}" download>⬇ {T['f_dl']}</a></p>
</div></div></section>
<section><div class="narrow">
<p class="lead">{T['intro1']}</p>
<p>{T['intro2']}</p>
</div></section>
<section class="alt"><div class="wrap">
<p class="eyebrow center">{T['up']}</p><h2 class="center">{T['uph']}</h2>
<div class="grid2 top" style="margin-top:30px">
{trip(lang, T['th_e'], T['th_t'], T['th_p'], T['th'], T['th_s'])}
{trip(lang, T['in_e'], T['in_t'], T['in_p'], T['ind'], T['in_s'])}
</div>
<p class="center" style="margin-top:36px">{T['cta']}</p>
<p class="center"><a class="btn solid" href="tel:+19546680348">{T['call']}</a> <a class="btn" href="mailto:spiritualbalanceinfo@gmail.com">{T['mail']}</a></p>
</div></section>
<section><div class="wrap">
<p class="eyebrow center">{T['past']}</p><h2 class="center">{T['pasth']}</h2>
<p class="center" style="max-width:720px;margin:0 auto 30px">{T['pastp']}</p>
<div class="grid2" style="margin-bottom:40px">
<figure><img class="portrait" src="/assets/img/viajes/th_zuluan_pakkapron.jpg" alt="Dr. Zuluan Orion with Pakkapron" style="max-height:560px;width:auto;margin:0 auto"><figcaption>{T['pakcap']}</figcaption></figure>
<div><p class="eyebrow">{T['pake']}</p><h3 style="margin-top:4px">Pakkapron</h3><p>{T['pakp']}</p></div>
</div>
<div class="gallery tall" style="grid-template-columns:repeat(2,1fr);max-width:900px;margin:0 auto">
<figure><img src="/assets/img/viajes/th_monje_incorrupto.jpg" alt="" loading="lazy" style="aspect-ratio:4/3"><figcaption>{T['g1']}</figcaption></figure>
<figure><img src="/assets/img/viajes/th_monjes_vistiendo.jpg" alt="" loading="lazy" style="aspect-ratio:4/3"><figcaption>{T['g2']}</figcaption></figure>
</div>
<h3 class="center" style="margin-top:50px">{T['gh']}</h3>
<div class="gallery" style="margin-top:20px"><img src="/assets/img/viajes/grupo_02.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_03.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_04.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_05.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_06.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_07.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_08.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_10.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_11.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_12.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_13.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_14.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_15.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_16.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_18.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_19.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_20.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_21.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_22.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_23.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_24.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_25.jpg" alt="" loading="lazy"><img src="/assets/img/viajes/grupo_26.jpg" alt="" loading="lazy"></div>
<div class="center" style="margin-top:40px"><a class="btn solid" style="font-size:16px;padding:18px 34px" href="/assets/docs/{T['pdf']}" download>⬇ {T['dl']}</a><p class="note" style="margin-top:12px">{T['dln']}</p></div>
</div></section>
<section class="dark"><div class="wrap sister">
<img src="{S(10)}" alt="" style="width:180px;filter:drop-shadow(0 0 18px rgba(200,164,92,.35))">
<div><p>{T['fc']}</p><a class="btn" href="{fc(lang,'codex')}">{T['fcl']}</a></div>
</div></section>
'''

def retreats_band(lang):
    t = {'en': ('JOURNEYS & RETREATS · JUNE 2027', 'Travel with me to Thailand and India', 'Holistic retreat in Chiang Mai, Thailand, and a pilgrimage to Vrindavan, Mathura, the Taj Mahal and Jaipur in Northern India, with the activation of the Light Codes.', 'See the journeys'),
         'es': ('VIAJES Y RETIROS · JUNIO 2027', 'Viaja conmigo a Tailandia y a la India', 'Retiro holístico en Chiang Mai, Tailandia, y peregrinación a Vrindavan, Mathura, el Taj Mahal y Jaipur en el norte de la India, con la activación de los Códigos de Luz.', 'Ver los viajes')}[lang]
    return f'''<section class="dark"><div class="narrow center">
<p class="eyebrow" style="color:var(--gold2)">{t[0]}</p>
<h2>{t[1]}</h2>
<p>{t[2]}</p>
<a class="btn solid" href="{url(lang,'retreats')}">{t[3]}</a>
</div></section>
'''


CAT = {'en': ('/assets/docs/Catalogo_Spiritual_Balance.pdf', '8 MB'), 'es': ('/assets/docs/Catalogo_Spiritual_Balance_ES.pdf', '4 MB')}

def catalogue_band(lang):
    t = {'en': ('OUR SERVICES', 'Download our catalogue', 'All our services in one place: biofeedback, bioresonance, light therapies, GDV, Ayurveda, holistic medicine, live blood analysis and bio-terrain analysis.', 'DOWNLOAD THE CATALOGUE (PDF)'),
         'es': ('NUESTROS SERVICIOS', 'Descarga nuestro catálogo', 'Todos nuestros servicios en un solo lugar: biofeedback, biorresonancia, terapias de luz, GDV, Ayurveda, medicina holística, análisis de sangre en vivo y análisis del bioterreno.', 'DESCARGAR EL CATÁLOGO (PDF)')}[lang]
    return f"""<section class="lav"><div class="narrow center">
<p class="eyebrow">{t[0]}</p><h2>{t[1]}</h2><p>{t[2]}</p>
<a class="btn solid" style="font-size:16px;padding:18px 34px" href="{CAT[lang][0]}" download>⬇ {t[3]}</a>
<p class="note" style="margin-top:12px">PDF · {CAT[lang][1]}</p>
</div></section>
"""


def before_after(lang):
    t = {'en': ('THE WORK, SEEN', 'From imbalance to harmony', 'BEFORE', 'Scattered energy, blocked and misaligned centers.', 'AFTER', 'Aligned centers, a calm and luminous field.', 'Before and after: the energy field and chakras out of balance, then aligned and luminous'),
         'es': ('EL TRABAJO, VISTO', 'Del desequilibrio a la armonía', 'ANTES', 'Energía dispersa, centros bloqueados y desalineados.', 'DESPUÉS', 'Centros alineados, un campo sereno y luminoso.', 'Antes y después: el campo energético y los chakras en desequilibrio, y luego alineados y luminosos')}[lang]
    return f"""<section class="ba"><div class="wrap">
<p class="eyebrow" style="color:var(--gold2)">{t[0]}</p><h2>{t[1]}</h2>
<picture><source media="(max-width:760px)" srcset="/assets/img/antes_despues_movil.webp"><img src="/assets/img/antes_despues_pc.webp" alt="{t[6]}" loading="lazy"></picture>
<div class="labels"><div><b>{t[2]}</b><span>{t[3]}</span></div><div><b>{t[4]}</b><span>{t[5]}</span></div></div>
</div></section>
"""


def honors(lang, imgs):
    t = {'en': ('RECOGNITION', 'Honored for his work', 'International recognition for integrating Ayurveda, quantum medicine and consciousness in the service of healing.',
                [('Dhanwantari Award', 'AAPNA · Association of Ayurvedic Professionals of North America · 2025'), ('AAPNA 2025', 'Ayurveda and the Mind, Pennsylvania'), ('Leader in Health Sciences', 'Health Sciences Awards · Santander, Spain · 2022'), ('Lifestyle Plus Awards', 'Lifestyle Plus Magazine')],
                [('60,000+', 'hours of meditation'), ('12½ years', 'in India'), ('8 years', 'in Thailand'), ('12,000+', 'people initiated into meditation')]),
         'es': ('RECONOCIMIENTOS', 'Reconocido por su trabajo', 'Reconocimiento internacional por integrar la Ayurveda, la medicina cuántica y la consciencia al servicio de la sanación.',
                [('Premio Dhanwantari', 'AAPNA · Asociación de Profesionales Ayurvédicos de Norteamérica · 2025'), ('AAPNA 2025', 'Ayurveda and the Mind, Pensilvania'), ('Líder en Ciencias de la Salud', 'Health Sciences Awards · Santander, España · 2022'), ('Lifestyle Plus Awards', 'Lifestyle Plus Magazine')],
                [('60.000+', 'horas de meditación'), ('12½ años', 'en la India'), ('8 años', 'en Tailandia'), ('12.000+', 'personas iniciadas en la meditación')])}[lang]
    figs = ''.join(f'<figure><img src="/assets/img/{im}" alt="{a}" loading="lazy"><figcaption><b>{a}</b><span>{b}</span></figcaption></figure>' for im, (a, b) in zip(imgs, t[3]))
    st = ''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in t[4])
    return f"""<section class="honors"><div class="wrap">
<p class="eyebrow">{t[0]}</p><h2>{t[1]}</h2><p class="sub">{t[2]}</p>
<div class="row">{figs}</div>
<div class="stats">{st}</div>
</div></section>
"""

LBA = ['lba_01.jpg', 'lba_02.jpg', 'lba_03.jpg', 'lba_05.jpg', 'lba_04.jpg']

# =================================================================== ENGLISH
E = BODY['en']

E[''] = hero('Spiritual Balance', 'Quantum Transformation · Ayurveda · Energy Healing',
  'I guide the soul to purify itself, to unblock its energy and to find its spiritual connection again. Everything I offer here serves that one purpose.',
  sig=1, page=False, img='/assets/img/logo_spiritual_balance.webp', kicker='DR. ZULUAN ORION · WESTON, FLORIDA',
  btns=f'<div class="btns"><a class="btn solid" href="{url("en","quantum-transformation")}">Quantum Transformation</a><a class="btn" href="{url("en","contact")}">Visit the clinic</a></div>') + honors('en', ['award_aapna_2025_ceremony.jpg', 'award_aapna_2025.jpg', 'award_siisdet_2022.jpg', 'award_lifestyle.jpg']) + f'''
<section><div class="wrap grid2">
<figure><img class="portrait" src="{I}zuluan_tuning_forks.jpg" alt="Dr. Zuluan Orion in his clinic in Weston, Florida"></figure>
<div>
<p class="eyebrow">WELCOME</p>
<h2>Life was given to us to live it, not to survive it</h2>
<p class="lead">If you have come this far, something in you is already looking for a change.</p>
<p>Maybe it is a pain that hasn't gone away, a sadness that has settled in the body, a pattern that keeps repeating however hard you try. Or maybe nothing is wrong, and you simply feel there is more to you than the life you are living.</p>
<p>For more than two decades I have received people in this clinic with exactly those questions. What I have learned is simple: the soul knows the way home. My work is to help it remember, and to clear what stands in the way.</p>
<p class="signature">— Dr. Zuluan Orion</p>
</div>
</div></section>

<section class="alt"><div class="wrap">
<p class="eyebrow center">THE WORK</p>
<h2 class="center">One purpose, several paths</h2>
<div class="pillar" style="margin:30px 0">
<img src="{S(2)}" alt="">
<p class="eyebrow" style="color:var(--gold2)">THE HEART OF EVERYTHING</p>
<h3>Quantum Transformation</h3>
<p style="max-width:680px;margin:0 auto 18px">The system I created after more than twenty years of practice and healing. It works with the soul directly: going within, through the chakras, to the root where a wound or a pattern was born, and letting Consciousness transform it.</p>
<a class="btn" href="{url('en','quantum-transformation')}">Discover it</a>
</div>
<div class="grid3">
<div class="card"><p class="eyebrow">THE BODY</p><h3>Ayurveda</h3><p>The science of life. Panchakarma to cleanse what the body has been carrying, Rasayana to renew it, and many other therapies chosen for your nature.</p><a class="more" href="{url('en','ayurveda')}">READ →</a></div>
<div class="card"><p class="eyebrow">THE ENERGY</p><h3>Bioresonance &amp; Biofeedback</h3><p>Working with the frequencies of your energy field: the chakras, emotional charges, thought forms and cellular memory.</p><a class="more" href="{url('en','energy')}">READ →</a></div>
<div class="card"><p class="eyebrow">THE MIRROR</p><h3>Evaluations</h3><p>Live blood analysis and energy evaluations: a way to see your inner terrain before we begin, and to watch it change.</p><a class="more" href="{url('en','evaluations')}">READ →</a></div>
</div>
</div></section>

''' + before_after('en') + f'''<section class="dark"><div class="wrap sister">
<img src="{S(10)}" alt="" style="width:200px;filter:drop-shadow(0 0 18px rgba(200,164,92,.35))">
<div>
<p class="eyebrow" style="color:var(--gold2)">THE LIGHT CODES</p>
<h2>Where my work comes from</h2>
<p>I am the cognizer of the Light Codes: a sacred language of syllables and sigils that came to me through a nondual awakening and a long descent of Consciousness into the body. The Light Codes are the child of the Flame Codex, and they live inside the work I do in this clinic.</p>
<p>The Codex has its own site, and my story, my teaching and all my books live on my personal site.</p>
<a class="btn" href="{fc('en')}">Enter The Flame Codex ↗</a> <a class="btn" href="https://drzuluanorion.org/">Dr. Zuluan Orion ↗</a>
</div>
</div></section>

''' + catalogue_band('en') + retreats_band('en') + grace_home('en') + testimonials('en') + f'''<section><div class="wrap">
<p class="eyebrow center">THE CLINIC</p>
<h2 class="center">A quiet place in Weston</h2>
<p class="center" style="max-width:700px;margin:0 auto 30px">A space made for stillness, where you can let go of the day and turn inward.</p>
{gallery(['clinic_buddha_waiting_room.jpg','clinic_session_01.jpg','zuluan_library.jpg','clinic_session_03_diplomas.jpg','tuning_forks_detail.jpg','zuluan_chakra_scan_desk.jpg','clinic_session_02.jpg','team_woman_chakra_scan.jpg','zuluan_outdoor_purple.jpg'])}
<p class="center" style="margin-top:36px"><a class="btn solid" href="{url('en','contact')}">Plan your visit</a></p>
</div></section>
'''

E['quantum-transformation'] = hero('Quantum Transformation', 'The heart of my work', sig=2) + f'''
<section><div class="narrow">
<p class="lead">This process is not only for healing. It is to bring about an awakening in your Being.</p>
<p>I am the originator of Quantum Transformation. It is the system that grew out of my own path: years of meditation, years in India and Thailand, years of sitting with people in healing rooms and seeing the same thing again and again. What feels like reality is often a cage, and beneath the cage something alive is waiting.</p>
<p>Quantum Transformation is the main work I do. Ayurveda, bioresonance, biofeedback and the evaluations all support it. Their purpose is to help the soul purify itself, unblock its energy and reconnect with the Spirit.</p>
<h3>More than a therapy</h3>
<p>Quantum Transformation is more than a therapeutic process for a physical, emotional or psychological ailment. It is a metamorphosis and a liberation. It is spiritual work of integration and alignment, and it opens possibilities where there were limits. You do not only resolve one issue. You awaken, and you begin a living relationship with your own Being.</p>
<blockquote>It is saying to the soul: I don't need to suffer in order to learn.</blockquote>
<h3>The ocean of Consciousness</h3>
<p>I like to describe us as an ocean. On the <strong>surface</strong> the waves of daily life play. Below it lies the <strong>subconscious</strong>, where what we could not process collects like a film of oil that blocks the light. Deeper still is the <strong>unconscious</strong>, where we keep what we have repressed. It stays there, quietly hurting us. And beyond all of it lies the <strong>supraconscious</strong>, the luminous level where time and space are transcended.</p>
<p>Behind every level is the <strong>Observer</strong>. That is your true essence, and the spiritual power that can transform your life lives there. Because the subconscious does not know linear time, we can go into the past and heal in the present.</p>
</div></section>

<section class="alt"><div class="narrow">
<p class="eyebrow">THE PROCESS</p>
<h2>How transformation happens</h2>
<ol class="steps">
<li><b>Going within.</b> Through meditation, intuition and visualization, I take you into a deeper, purer state of relaxation, beyond the thinking mind.</li>
<li><b>The chakras as bridges.</b> Each chakra is a portal to a level of Consciousness inside you. Through them we reach the place where the block was born.</li>
<li><b>Recognizing what weighs.</b> We identify the negative archetype: the emotion, the trauma or the dilemma that keeps repeating in your life.</li>
<li><b>Calling in the missing light.</b> We recognize the positive archetype, the energy your soul needs: safety where there was fear, trust where there was a wound. The angels and the luminous forces accompany this step.</li>
<li><b>Synthesis.</b> The two energies meet and the positive dissolves the negative. The tension dissipates, and a space of release, peace and fullness opens.</li>
<li><b>Integration.</b> Over the following days and weeks what was released settles into your life, until it becomes the new way you live.</li>
</ol>
</div></section>

<section><div class="wrap grid2">
<div>
<p class="eyebrow">IN THE SESSION</p>
<h2>A field of presence</h2>
<p>In a session I am not trying to fix you, and you are not trying to force your own healing. Together we hold a field of presence. In that surrender something larger than both of us acts: Consciousness itself.</p>
<p>The more the mind intervenes, the fewer the results. So we let go. The catharsis often comes on its own, sometimes in the session and sometimes later in dreams, memories and intense experiences that you keep integrating in the days that follow.</p>
<p>I have trained facilitators in this work, and they experience the same thing. When the field is held, the soul knows what to do.</p>
</div>
<figure><img class="portrait" src="{I}zuluan_library.jpg" alt="Dr. Zuluan Orion"></figure>
</div></section>

<section class="lav"><div class="narrow">
<p class="eyebrow">EVERYTHING ELSE, IN SERVICE OF THE SOUL</p>
<h2>The tools that support the work</h2>
<p><a href="{url('en','ayurveda')}"><strong>Ayurveda</strong></a> reads your nature and what has moved it out of balance, and prepares the body to sustain the transformation.</p>
<p><a href="{url('en','energy')}"><strong>Bioresonance</strong></a> works on the energetic and emotional field, releasing charges and cellular memory.</p>
<p><a href="{url('en','energy')}"><strong>Biofeedback</strong></a> shows how your whole system is responding, so the body learns again how to rest.</p>
<p><a href="{url('en','evaluations')}"><strong>Live blood analysis</strong></a> offers a visual mirror of your inner terrain.</p>
<p>Each tool helps to see, to loosen and to sustain. The transformation itself happens in Consciousness.</p>
<p class="center" style="margin-top:30px"><a class="btn solid" href="{url('en','contact')}">Begin your process</a></p>
</div></section>
'''

E['ayurveda'] = hero('Ayurveda', 'The science of life', sig=5) + f'''
<section><div class="wrap grid2">
<div>
<p class="lead">Ayurveda does not look only at a symptom. It looks at you.</p>
<p>Ayurveda is the traditional medicine of India, and it is thousands of years old. I studied it and lived it in India for many years, and it is the ground my clinic stands on. It sees the whole person: your unique nature, your <em>prakriti</em>; the balance of your three vital energies, <em>vata</em>, <em>pitta</em> and <em>kapha</em>; your digestion, your mind and your spirit.</p>
<p>For Ayurveda, health is your natural state. What we call illness begins much earlier, as a quiet imbalance that builds up in the body, in the emotions and in the way we live. In your first consultation I come to know your nature and what has moved it away from its center. From there we design a path made only for you.</p>
</div>
<figure><img class="portrait" src="{I}portrait_prayer.jpg" alt="Dr. Zuluan Orion"></figure>
</div></section>

<section class="alt"><div class="narrow">
<p class="eyebrow">PANCHAKARMA</p>
<h2>The five actions of purification</h2>
<p>Over the years the body keeps what it could not digest: food, emotions, experiences. Ayurveda calls this <strong>ama</strong>. It is a residue that settles in the tissues and channels, dims the digestive fire, clouds the mind and leaves the body heavy and tired.</p>
<p>Panchakarma is Ayurveda's great deep cleanse. It is designed to release that residue from the root and give the body back its original lightness.</p>
<h3>The journey</h3>
<ol class="steps">
<li><b>Preparation (Purvakarma).</b> For several days your body is nourished inside and out with medicated oils and massage (<em>abhyanga</em>), and opened with warmth and herbal steam (<em>swedana</em>). The tissues soften, and what was stored loosens and moves to where it can leave. For many people this stage alone is an experience of deep rest and surrender.</li>
<li><b>The five actions (Pradhanakarma).</b> Tradition describes five pathways of purification. I choose the ones you need according to your nature and your moment: cleansing of the upper tract, gentle intestinal cleansing, medicated enemas with oils and herbal decoctions, <em>nasya</em> (purification through the nose, which clears the head and the senses), and purification of the blood.</li>
<li><b>Return (Paschatkarma).</b> After the cleanse your digestive fire is rekindled step by step with simple, careful food, so that you come back to daily life renewed rather than burdened.</li>
</ol>
<h3>What Panchakarma can do for you</h3>
<ul class="benefits">
<li>A feeling of lightness and clarity</li>
<li>Digestion that comes back to life</li>
<li>More energy and deeper sleep</li>
<li>More luminous skin</li>
<li>A calmer mind</li>
<li>Emotions that weigh less</li>
</ul>
<p>And something harder to name. As the body is cleared, the soul finds room too. Many people tell me that with Panchakarma they let go of layers they had carried for years.</p>
</div></section>

<section><div class="narrow">
<p class="eyebrow">RASAYANA</p>
<h2>The art of renewal</h2>
<p>After cleansing comes nourishing. Rasayana is the branch of Ayurveda devoted to rejuvenation. It strengthens the tissues, renews vitality and nourishes <strong>ojas</strong>, the subtle essence that Ayurveda sees as the foundation of immunity, the light in your skin, the steadiness of your mind and the joy of being alive.</p>
<p>That is why Rasayana comes after Panchakarma. A cleansed body receives nourishment the way freshly turned earth receives a seed.</p>
<h3>How Rasayana is lived</h3>
<ul class="benefits">
<li>Rejuvenating herbs and preparations chosen for your nature</li>
<li>Food that nourishes body and senses</li>
<li>Rasayanas for the mind: clarity, memory, calm</li>
<li><em>Achara Rasayana</em>, the rasayana of conduct</li>
</ul>
<p>Ayurveda teaches that truthfulness, compassion, inner peace and a life lived in harmony rejuvenate as much as any herb. This is where Ayurveda and Quantum Transformation meet.</p>
<h3>What Rasayana can do for you</h3>
<p>More vitality and stamina, a stronger and more flexible body, glowing skin, a clear and steady mind, better sleep, and a deep sense of renewal, as if the body were remembering its youth.</p>
</div></section>

<section class="lav"><div class="narrow center">
<p class="eyebrow">AND MUCH MORE</p>
<h2>A path made for you</h2>
<p>Ayurveda is not one recipe for everyone. Beyond Panchakarma and Rasayana there are many other therapies, and I choose them for your nature and your moment: massage with medicated oils, <em>shirodhara</em> (a continuous stream of warm oil over the forehead that brings a very deep calm), herbal therapies, guidance on food and daily routine, breathing and meditation.</p>
<p>In your consultation we find your path together.</p>
<p><a class="btn solid" href="{url('en','contact')}">Book a consultation</a></p>
</div></section>
'''

E['energy'] = hero('Energy Therapies', 'Bioresonance · Biofeedback · Light · Sound', sig=7) + f'''
<section><div class="narrow">
<figure style="margin:0 0 30px"><img class="portrait" src="/assets/img/energy_bioresonance.jpg" alt="" style="width:100%"></figure>
<p class="eyebrow">BIORESONANCE · ENERGETIC TRANSFERENCE</p>
<h2>Everything that lives, vibrates</h2>
<p class="lead">Every organ, every emotion and every thought has its own frequency. Together they form the field that surrounds and sustains your body.</p>
<p>When that field is in harmony, life moves through you freely. When it holds old charges, such as fear never spoken, grief never cried, or patterns inherited without being chosen, the flow slows down. Over time you feel it as heaviness, tiredness and dis-ease.</p>
<p>Bioresonance works at the level of that field. Through gentle contact at your hands and feet, your body's own frequencies are read and reflected back to it as information. Where there is distortion, the body is offered the resonance of its original harmony. Nothing is forced. Your own consciousness decides what it is ready to let go.</p>
<h3>What we work with</h3>
<ul class="lineage">
<li><b>The energy centers.</b> Balancing the chakras and the subtle channels so that energy can rise and descend without blockage, from the root to the crown.</li>
<li><b>The emotions.</b> Finding the emotional charges held in the body, such as fear, anger, guilt and sadness, and letting them dissolve instead of repeat.</li>
<li><b>Thought forms.</b> Bringing to light the beliefs and mental patterns absorbed from family, culture and past experience, so they lose their hold.</li>
<li><b>Cellular memory.</b> Every cell remembers. Old impressions, some from early childhood and some carried down the family line, can be met and released, so the body no longer has to relive them.</li>
<li><b>The epigenetic layer.</b> Your history does not have to be your destiny. How we live, feel and think shapes how the body expresses what it carries. Working on the energetic blueprint helps the body express its original order instead of its accumulated wounds.</li>
<li><b>Emotional heaviness.</b> When sadness has settled into the body and life has turned grey, this work helps lift that weight, so you can breathe again and find your own way back to joy.</li>
</ul>
<h3>What people often notice</h3>
<p>Lightness and calm, deeper sleep, clearer thinking, emotions that no longer overwhelm, more energy, and a quiet feeling of coming home to yourself.</p>
</div><div class="wrap" style="margin-top:30px">{gallery(['clinic_session_01.jpg','clinic_session_02.jpg','clinic_session_03_diplomas.jpg'], 'tall')}</div></section>

<section class="alt"><div class="wrap grid2">
<figure><img class="portrait" src="{I}zuluan_chakra_scan_desk.jpg" alt="Energy evaluation in the clinic"></figure>
<div>
<p class="eyebrow">BIOFEEDBACK</p>
<h2>The body in conversation</h2>
<p>Your body is always speaking: through the breath, the heartbeat, the skin, the tension in the muscles. Biofeedback lets us listen. Painless sensors follow how your system responds to stress and to calm, moment by moment. When you can see that response, you can learn to guide it.</p>
<p>In the session, biofeedback shows where the nervous system is holding tension and how your whole being responds, physically, emotionally and energetically. It becomes a mirror, and with the mirror comes choice. The breath slows, the heart steadies, and the body remembers how to rest.</p>
<ul class="benefits">
<li>Deep relaxation, release of stored stress</li>
<li>Relief from tension in head, neck and jaw</li>
<li>Calmer sleep</li>
<li>Steadier emotions, less anxiety</li>
<li>Greater awareness of your body</li>
<li>Taking part in your own healing</li>
</ul>
<div class="gallery" style="grid-template-columns:1fr 1fr;margin-top:20px"><img src="/assets/img/eval_chakra_scan.jpg" alt="" loading="lazy"><img src="/assets/img/tuning_forks_detail.jpg" alt="" loading="lazy"></div>
</div>
</div></section>

<section><div class="narrow">
<p class="eyebrow">LIGHT</p>
<h2>Light therapies</h2>
<p>Light is information. In these gentle therapies, light is brought to the body to support its own capacity to regenerate and to restore the flow of energy along the channels and points I work with. They are quiet, painless sessions that combine naturally with the other therapies.</p>
<ul class="lineage">
<li><b>Cold laser and photon transfer.</b> Low-level light that stimulates cellular repair and regeneration, eases pain and tension, supports circulation and lymphatic drainage, and relaxes muscles and joints. Sessions are short, usually between 15 and 30 minutes.</li>
<li><b>Bio-light therapy.</b> Light configurations that clear energy blockages, open the flow through the meridians, the chakras and the nadis, support detoxification on every level, and offer a deeply relaxing, blissful experience.</li>
</ul>
</div></section>

<section class="alt"><div class="wrap grid2">
<div>
<p class="eyebrow">HOLISTIC MEDICINE</p>
<h2>Marma, sound and vibration</h2>
<p>Some of the deepest healing happens through touch and sound. In my sessions I work with:</p>
<ul class="lineage">
<li><b>Marma points.</b> The vital points of Ayurveda, gates of the life force. Working with them sustains the flow of energy, harmonizes body and mind, and revitalizes the whole being.</li>
<li><b>Tuning forks.</b> Precise vibrations that restore harmony to the energy system, invite the body back to its natural balance, and help release heavy thoughts and emotions.</li>
<li><b>Chimes.</b> Clear sounds that cleanse the field of dense energies and open the way to calm and to deeper chakra work.</li>
<li><b>Crystal bowls.</b> Sustained tones that reach the aura and the brain waves, quiet the mind and carry meditation into stillness.</li>
</ul>
</div>
<figure><img class="portrait" src="/assets/img/zuluan_tuning_forks.jpg" alt="Dr. Zuluan Orion with tuning forks"></figure>
</div></section>

<section class="lav"><div class="narrow center">
<h2>One path, three languages</h2>
<p>In my clinic Ayurveda, bioresonance and biofeedback are not separate treatments. They are three ways of listening to the same being. Ayurveda reads your nature and what has moved it out of balance. Bioresonance speaks to the energetic and emotional field. Biofeedback lets the body show both of us how it is responding. All three serve the work of <a href="{url('en','quantum-transformation')}">Quantum Transformation</a>.</p>
<p><a class="btn solid" href="{url('en','contact')}">Book a session</a></p>
</div></section>
'''

E['evaluations'] = hero('Evaluations', 'Seeing the inner terrain', sig=9) + f'''
<section><div class="narrow">
<p class="eyebrow">LIVE BLOOD ANALYSIS</p>
<h2>A living drop, seen with holistic eyes</h2>
<p class="lead">One drop of your blood, seen alive under the microscope, tells a story.</p>
<p>In live blood analysis we look at a drop of fresh blood on a screen, together, in real time. I read it with a holistic eye: the state of the terrain, how the cells move and relate to one another, what the blood shows about digestion, about the burden the body is carrying, about vitality.</p>
<p>For many people it is the first time they actually see their inner world, and that moment of seeing is already part of the transformation. We repeat it over time and watch the terrain change as you change.</p>
</div>
<div class="wrap" style="margin-top:34px">{gallery(LBA, 'tall')}</div>
</section>

<section class="alt"><div class="wrap grid3">
<div class="card"><img src="/assets/img/eval_bioterrain.jpg" alt="Bio-terrain and biochemical analysis" loading="lazy" style="width:100%;aspect-ratio:4/3;object-fit:cover;margin-bottom:18px"><p class="eyebrow">BIO-TERRAIN ANALYSIS</p><h3>The chemistry of balance</h3><p>A reading of your biological terrain through blood, saliva and urine: more than sixty markers of the inner environment where your cells live, such as acid-alkaline balance, stress resilience and detoxification. It shows me where your system is working hard and what it needs to come back to balance.</p></div>
<div class="card"><img src="/assets/img/eval_gdv_kirlian.jpg" alt="" loading="lazy" style="width:100%;aspect-ratio:4/3;object-fit:cover;margin-bottom:18px"><p class="eyebrow">ENERGY FIELD IMAGING</p><h3>GDV and Kirlian</h3><p>Images of the field of light around the body. They show how your energy is distributed and where it is weaker or blocked, so we can follow your chakras and your field as the work progresses.</p></div>
<div class="card"><img src="/assets/img/eval_chakra_scan.jpg" alt="" loading="lazy" style="width:100%;aspect-ratio:4/3;object-fit:cover;margin-bottom:18px"><p class="eyebrow">ENERGY EVALUATION</p><h3>The chakra scan</h3><p>An evaluation of your energy centers that shows me where to begin, so that each session goes straight to what your soul needs now.</p></div>
</div></section>

<section><div class="narrow center">
<p>Evaluations are not an end in themselves. They are a mirror, so that you and I can see where you are and walk the path of <a href="{url('en','quantum-transformation')}">Quantum Transformation</a> together.</p>
<p><a class="btn solid" href="{url('en','contact')}">Schedule an evaluation</a></p>
</div></section>
'''

CRED_EN = '''<table class="cred">
<tr><td>MD in Ayurveda (Vaidya Shiromani / Vachaspati)</td><td>India</td></tr>
<tr><td>Bachelor of Ayurvedic Medicine and Science (B.A.M.S.)</td><td>India</td></tr>
<tr><td>Ph.D. in Natural Medicine — World Organization of Natural Medicine</td><td>2014</td></tr>
<tr><td>Ph.D. in Quantum Medicine</td><td>2014</td></tr>
<tr><td>Doctorate in Humanitarian Services — World Organization of Natural Medicine</td><td>2013</td></tr>
<tr><td>Academic Council member — AAPNA, Association of Ayurvedic Professionals of North America</td><td></td></tr>
<tr><td>Member — NAMA, National Ayurvedic Medical Association</td><td></td></tr>
</table>'''

E['about'] = hero('Dr. Zuluan Orion', 'Originator of Quantum Transformation · Cognizer of the Light Codes', sig=3) + f'''
<section><div class="wrap grid2 top">
<figure><img class="portrait" src="{I}portrait_side.jpg" alt="Dr. Zuluan Orion"></figure>
<div>
<p class="lead">I was born in Bogotá in 1971. I grew up in a hard home, and the emptiness it left in my heart became the beginning of my spiritual path. I needed to find something, though I didn't know what.</p>
<p>That search took me through more than sixty thousand hours of meditation and almost two decades living and studying in Asia: twelve and a half years in India, with yoga, meditation and Ayurvedic medicine, and eight in Thailand, with Buddhism and healing. Along the way an awakening to the Self came, and in nearly thirty years it has not reversed.</p>
<p>Out of that life came the two things I offer. <strong>Quantum Transformation</strong> is the system I created to guide the soul through its own levels of Consciousness, to the root of what hurts, and back to its light. The <strong>Light Codes</strong> are a sacred language of syllables and sigils that I received and recognized, and they live at the heart of the Flame Codex.</p>
<p>For two decades I have brought them together in my clinic in Weston, Florida, with Ayurvedic, natural and quantum medicine, and with people from many countries.</p>
<p class="signature">I am not the source. Consciousness is. My work is to return you to the light you never lost.</p>
</div>
</div></section>

<section class="dark"><div class="wrap">
<div class="stats">
<div><b>60,000+</b><span>hours of meditation</span></div>
<div><b>12½ years</b><span>in India</span></div>
<div><b>8 years</b><span>in Thailand</span></div>
<div><b>20+ years</b><span>caring for people in this clinic</span></div>
</div>
</div></section>

''' + grace_about('en') + f'''<section><div class="wrap sister">
<img src="{S(10)}" alt="" style="width:200px">
<div>
<p class="eyebrow">MY FULL STORY</p>
<h2>Dr. Zuluan Orion</h2>
<p>My masters and lineages, the awakening, the descent of the Flame, my recognitions and all my books are told in full on my personal site. The Light Codes live on the site of the Flame Codex.</p>
<a class="btn solid" href="https://drzuluanorion.org/story/">Read my story ↗</a> <a class="btn" href="{fc('en','codex')}">The Light Codes ↗</a>
</div>
</div></section>

<section class="alt"><div class="wrap">
<div class="grid2 top">
<div>
<p class="eyebrow">MEDICINE</p>
<h2>Studies and credentials</h2>
{CRED_EN}
</div>
<figure><img class="portrait" src="{I}press_tv_studio_01.jpg" alt="Dr. Zuluan Orion on television"><figcaption>Presenting <em>Deshojando el Corazón de la Eternidad</em> on television in Miami.</figcaption></figure>
</div>
<h2 style="margin-top:60px">Recognition</h2>
<div class="awards">
<figure><img src="{I}award_aapna_2025_ceremony.jpg" alt="AAPNA Dhanwantari Award ceremony" loading="lazy"><figcaption>Dhanwantari Award, AAPNA, 2025, for integrating Ayurveda with contemporary science.</figcaption></figure>
<figure><img src="{I}award_aapna_2025.jpg" alt="With the AAPNA award" loading="lazy"><figcaption>AAPNA, 2025.</figcaption></figure>
<figure><img src="{I}award_siisdet_2022.jpg" alt="Health Sciences Awards 2022" loading="lazy"><figcaption>Leader in Research and Health Sciences for the Benefit of Mankind, Health Sciences Awards, Santander, Spain, 2022.</figcaption></figure>
<figure><img src="{I}award_lifestyle.jpg" alt="Lifestyle Plus Magazine Awards" loading="lazy"><figcaption>Lifestyle Plus Magazine Awards.</figcaption></figure>
</div>
<h2 style="margin-top:60px">With Ayurvedic physicians</h2>
<p>Ayurveda is a living tradition, and I share it with Ayurvedic physicians from India.</p>
<figure style="max-width:720px;margin:26px 0"><img class="portrait" src="/assets/img/kerala_dr_reddy_kumar.jpg" alt="Studying Ayurvedic medicine with Dr. Reddy Kumar" loading="lazy"><figcaption>Studying Ayurvedic medicine beside Dr. Reddy Kumar, University of Kerala, India.</figcaption></figure>
<div class="gallery tall" style="grid-template-columns:repeat(3,1fr);max-width:1000px">
<figure><img src="/assets/img/with_dr_shekhar_annambhotla.jpg" alt="With Dr. Shekhar Annambhotla" loading="lazy"><figcaption>With Dr. Shekhar Annambhotla, BAMS, MD (Ayurveda).</figcaption></figure>
<figure><img src="/assets/img/with_dr_suresh_swarnapuri.jpg" alt="With Dr. Suresh Swarnapuri" loading="lazy"><figcaption>With Dr. Suresh Swarnapuri, BAMS, MD (Ayurveda).</figcaption></figure>
<figure><img src="/assets/img/with_dr_shan_lakshmanan.jpg" alt="With Dr. Shan Lakshmanan, Ph.D" loading="lazy"><figcaption>With Dr. Shan Lakshmanan, Ph.D.</figcaption></figure>
</div>
</div></section>
'''

def books_body(lang):
    t = {'en': ('THE LIGHT CODES', 'Codes for the mind, the heart, dreams and energy', 'THE FLAME CODEX', 'The sacred language', 'THE DESCENT', 'The living account', 'HEALING AND MEDITATION', 'Quantum Transformation in books', 'NOVELS AND STORIES', 'Spiritual fiction', 'FORTHCOMING', 'All the books, with their full presentation, are on'),
         'es': ('LOS CÓDIGOS DE LUZ', 'Códigos para la mente, el corazón, los sueños y la energía', 'EL CÓDICE DE LA LLAMA', 'El lenguaje sagrado', 'EL DESCENSO', 'El relato vivo', 'SANACIÓN Y MEDITACIÓN', 'La Transformación Cuántica en libros', 'NOVELAS E HISTORIAS', 'Ficción espiritual', 'PRÓXIMAMENTE', 'Todos los libros, con su presentación completa, están en')}[lang]
    F = t[10]
    return f'''<section><div class="wrap">
<p class="eyebrow">{t[0]}</p><h2>{t[1]}</h2>
<div class="books shelf">
{book('cl_mente','Códigos de Luz para tu Mente','','')}
{book('cl_corazon','Códigos de Luz para tu Corazón','','')}
{book('cl_suenos','Códigos de Luz para tus Sueños','','')}
{book('cl_energia','Códigos de Luz para tu Energía','','')}
{book('meditacion_codigos_luz','Meditación de Códigos de Luz','','')}
</div>
<p class="eyebrow" style="margin-top:60px">{t[2]}</p><h2>{t[3]}</h2>
<div class="books shelf">
{book('codice1','El Códice de la Llama · Vol. I','','')}
{book('codice2','El Códice de la Llama · Vol. II','','')}
{book('arte_angelico_1','El Arte Angélico · Vol. I','','')}
{book('arte_angelico_2','El Arte Angélico · Vol. II','','')}
</div>
<p class="eyebrow" style="margin-top:60px">{t[4]}</p><h2>{t[5]}</h2>
<div class="books shelf">
{book('yoga_descenso_puerta','Yoga del Descenso · Libro Puerta','','')}
{book('yoga_descenso_morada','Yoga del Descenso · Libro de la Morada','','')}
{book('llama_encarnada','La Llama Encarnada','','')}
</div>
<p class="eyebrow" style="margin-top:60px">{t[6]}</p><h2>{t[7]}</h2>
<div class="books shelf">
{book('transformacion_cuantica','Transformación Cuántica')}
{book('transformacion_cuantica_nivel1','Transformación Cuántica · Nivel 1')}
{book('puntos_transformacion_cuantica','Puntos de Transformación Cuántica')}
{book('meditacion_cuantica','Meditación Cuántica')}
{book('el_refugio_del_corazon','El refugio del Corazón')}
{book('deshojando_corazon_eternidad','Deshojando el Corazón de la Eternidad')}
</div>
<p class="eyebrow" style="margin-top:60px">{t[8]}</p><h2>{t[9]}</h2>
<div class="books shelf">
{book('selarin','Selarín')}
{book('dipti_la_invasora_esperada','DIPTI · La invasora esperada')}
{book('zendrick_virtudes_khudday','Zendrick y las virtudes del Khudday')}
{book('zendrick_ii_cinco_virtudes','Zendrick II y las cinco virtudes')}
{book('la_busqueda_del_rey','La búsqueda del rey')}
</div>
<p class="eyebrow" style="margin-top:60px">GRACE ORION</p><h2>{'Her book' if lang=='en' else 'Su libro'}</h2>
<div class="books shelf">
{book('grace_el_retorno_de_mi_alma','El retorno de mi alma','Grace Orion')}
</div>
<hr class="rule">
<p class="center">{t[11]} <a href="https://drzuluanorion.org{'/es/' if lang == 'es' else '/'}books/">drzuluanorion.org ↗</a></p>
</div></section>
'''

E['books'] = hero('Books', 'By Dr. Zuluan Orion', sig=12) + books_body('en')

E['contact'] = hero('Visit', 'Spiritual Balance · Weston, Florida', sig=18) + catalogue_band('en') + f'''
<section><div class="wrap grid2 top">
<div class="visit">
<p class="lead">I'll be glad to receive you.</p>
<p>Write or call to book your first consultation. We'll talk about what brings you here, and together we'll choose where to begin.</p>
<dl>
<dt>ADDRESS</dt><dd>1565 North Park Drive, Suite 101<br>Weston, Florida 33326</dd>
<dt>PHONE</dt><dd><a href="tel:+19546680348">(954) 668-0348</a></dd>
<dt>EMAIL</dt><dd><a href="mailto:spiritualbalanceinfo@gmail.com">spiritualbalanceinfo@gmail.com</a></dd>
<dt>HOURS</dt><dd>Monday to Friday, 9 am – 6 pm<br>Saturday, 9 am – 1 pm</dd>
<dt>LANGUAGES</dt><dd>English and Spanish</dd>
</dl>
<p style="margin-top:28px"><a class="btn solid" href="tel:+19546680348">Call</a> <a class="btn" href="https://maps.google.com/?q=1565+N+Park+Drive+Suite+101+Weston+FL+33326">Directions</a></p>
</div>
<figure><img class="portrait" src="{I}clinic_buddha_waiting_room.jpg" alt="The waiting room at Spiritual Balance" style="max-height:640px;width:auto;margin:0 auto"></figure>
</div></section>
'''

# =================================================================== ESPAÑOL
X = BODY['es']

X[''] = hero('Spiritual Balance', 'Transformación Cuántica · Ayurveda · Sanación Energética',
  'Guío al alma a depurarse, a desbloquear su energía y a reencontrar su conexión espiritual. Todo lo que ofrezco aquí está al servicio de ese único propósito.',
  sig=1, page=False, img='/assets/img/logo_spiritual_balance.webp', kicker='DR. ZULUAN ORION · WESTON, FLORIDA',
  btns=f'<div class="btns"><a class="btn solid" href="{url("es","quantum-transformation")}">Transformación Cuántica</a><a class="btn" href="{url("es","contact")}">Visita la clínica</a></div>') + honors('es', ['award_aapna_2025_ceremony.jpg', 'award_aapna_2025.jpg', 'award_siisdet_2022.jpg', 'award_lifestyle.jpg']) + f'''
<section><div class="wrap grid2">
<figure><img class="portrait" src="{I}zuluan_tuning_forks.jpg" alt="El Dr. Zuluan Orion en su clínica de Weston, Florida"></figure>
<div>
<p class="eyebrow">BIENVENIDO</p>
<h2>La vida se nos dio para vivirla, no para sobrevivirla</h2>
<p class="lead">Si llegaste hasta aquí, algo en ti ya está buscando un cambio.</p>
<p>Quizás es un dolor que no se va, una tristeza que se instaló en el cuerpo, un patrón que se repite por más que lo intentes. O quizás no te pasa nada, y simplemente sientes que eres más que la vida que estás viviendo.</p>
<p>Durante más de dos décadas he recibido en esta clínica a personas con esas mismas preguntas. Lo que he aprendido es sencillo: el alma conoce el camino a casa. Mi trabajo es ayudarla a recordarlo y despejar lo que estorba.</p>
<p class="signature">— Dr. Zuluan Orion</p>
</div>
</div></section>

<section class="alt"><div class="wrap">
<p class="eyebrow center">EL TRABAJO</p>
<h2 class="center">Un propósito, varios caminos</h2>
<div class="pillar" style="margin:30px 0">
<img src="{S(2)}" alt="">
<p class="eyebrow" style="color:var(--gold2)">EL CORAZÓN DE TODO</p>
<h3>Transformación Cuántica</h3>
<p style="max-width:680px;margin:0 auto 18px">El sistema que creé después de más de veinte años de práctica y de sanación. Trabaja directamente con el alma: ir hacia adentro, a través de los chakras, hasta la raíz donde nació una herida o un patrón, y dejar que la Consciencia lo transforme.</p>
<a class="btn" href="{url('es','quantum-transformation')}">Descúbrela</a>
</div>
<div class="grid3">
<div class="card"><p class="eyebrow">EL CUERPO</p><h3>Ayurveda</h3><p>La ciencia de la vida. Panchakarma para limpiar lo que el cuerpo ha venido cargando, Rasayana para renovarlo, y muchas otras terapias elegidas según tu naturaleza.</p><a class="more" href="{url('es','ayurveda')}">LEER →</a></div>
<div class="card"><p class="eyebrow">LA ENERGÍA</p><h3>Biorresonancia y Biofeedback</h3><p>El trabajo con las frecuencias de tu campo energético: los chakras, las cargas emocionales, las formas de pensamiento y la memoria celular.</p><a class="more" href="{url('es','energy')}">LEER →</a></div>
<div class="card"><p class="eyebrow">EL ESPEJO</p><h3>Evaluaciones</h3><p>Análisis de sangre en vivo y evaluaciones energéticas: una forma de ver tu terreno interior antes de empezar, y de verlo cambiar.</p><a class="more" href="{url('es','evaluations')}">LEER →</a></div>
</div>
</div></section>

''' + before_after('es') + f'''<section class="dark"><div class="wrap sister">
<img src="{S(10)}" alt="" style="width:200px;filter:drop-shadow(0 0 18px rgba(200,164,92,.35))">
<div>
<p class="eyebrow" style="color:var(--gold2)">LOS CÓDIGOS DE LUZ</p>
<h2>De dónde viene mi trabajo</h2>
<p>Soy el cognizador de los Códigos de Luz: un lenguaje sagrado de sílabas y sigilos que llegó a mí a través de un despertar no dual y de un largo descenso de la Consciencia en el cuerpo. Los Códigos de Luz son hijos del Códice de la Llama, y viven dentro del trabajo que hago en esta clínica.</p>
<p>El Códice tiene su propio sitio, y mi historia, mi enseñanza y todos mis libros están en mi sitio personal.</p>
<a class="btn" href="{fc('es')}">Entra al Códice de la Llama ↗</a> <a class="btn" href="https://drzuluanorion.org/es/">Dr. Zuluan Orion ↗</a>
</div>
</div></section>

''' + catalogue_band('es') + retreats_band('es') + grace_home('es') + testimonials('es') + f'''<section><div class="wrap">
<p class="eyebrow center">LA CLÍNICA</p>
<h2 class="center">Un lugar sereno en Weston</h2>
<p class="center" style="max-width:700px;margin:0 auto 30px">Un espacio hecho para la quietud, donde puedes soltar el día y volver hacia adentro.</p>
{gallery(['clinic_buddha_waiting_room.jpg','clinic_session_01.jpg','zuluan_library.jpg','clinic_session_03_diplomas.jpg','tuning_forks_detail.jpg','zuluan_chakra_scan_desk.jpg','clinic_session_02.jpg','team_woman_chakra_scan.jpg','zuluan_outdoor_purple.jpg'])}
<p class="center" style="margin-top:36px"><a class="btn solid" href="{url('es','contact')}">Planea tu visita</a></p>
</div></section>
'''

X['quantum-transformation'] = hero('Transformación Cuántica', 'El corazón de mi trabajo', sig=2) + f'''
<section><div class="narrow">
<p class="lead">Este proceso no es solo para sanar. Es para causar un despertar en tu Ser.</p>
<p>Soy el originador de la Transformación Cuántica. Es el sistema que nació de mi propio camino: años de meditación, años en la India y en Tailandia, años sentado junto a personas en salas de sanación, viendo una y otra vez lo mismo. Lo que parece la realidad muchas veces es una jaula, y debajo de la jaula algo vivo está esperando.</p>
<p>La Transformación Cuántica es mi trabajo principal. La Ayurveda, la biorresonancia, el biofeedback y las evaluaciones están a su servicio, para ayudar al alma a depurarse, a desbloquear su energía y a reconectar con el Espíritu.</p>
<h3>Más que una terapia</h3>
<p>La Transformación Cuántica es más que un proceso terapéutico para una dolencia física, emocional o psicológica. Es una metamorfosis y una liberación. Es un trabajo espiritual de integración y alineación que abre posibilidades donde había límites. No solo resuelves un tema. Despiertas, y empiezas una relación viva con tu propio Ser.</p>
<blockquote>Es decirle al alma: no necesito sufrir para aprender.</blockquote>
<h3>El océano de la Consciencia</h3>
<p>Me gusta describirnos como un océano. En la <strong>superficie</strong> juegan las olas del día a día. Debajo está el <strong>subconsciente</strong>, donde se acumula lo que no pudimos procesar, como una capa de aceite que nos tapa la luz. Más hondo está el <strong>inconsciente</strong>, donde guardamos lo que hemos reprimido. Sigue ahí, hiriéndonos en silencio. Y más allá de todo está el <strong>supraconsciente</strong>, el nivel luminoso donde se trascienden el tiempo y el espacio.</p>
<p>Detrás de cada nivel está el <strong>Observador</strong>. Esa es tu verdadera esencia, y ahí vive el poder espiritual que puede transformar tu vida. Como el subconsciente no conoce el tiempo lineal, podemos ir al pasado y sanar en el presente.</p>
</div></section>

<section class="alt"><div class="narrow">
<p class="eyebrow">EL PROCESO</p>
<h2>Cómo ocurre la transformación</h2>
<ol class="steps">
<li><b>Ir hacia adentro.</b> A través de la meditación, la intuición y la visualización, te llevo a un estado de relajación más profundo y más puro, más allá de la mente que piensa.</li>
<li><b>Los chakras como puentes.</b> Cada chakra es un portal a un nivel de Consciencia dentro de ti. A través de ellos llegamos al lugar donde nació el bloqueo.</li>
<li><b>Reconocer lo que pesa.</b> Identificamos el arquetipo negativo: la emoción, el trauma o el dilema que se repite en tu vida.</li>
<li><b>Llamar a la luz que falta.</b> Reconocemos el arquetipo positivo, la energía que tu alma necesita: seguridad donde hubo miedo, confianza donde hubo herida. Los ángeles y las fuerzas luminosas acompañan este paso.</li>
<li><b>Síntesis.</b> Las dos energías se encuentran y la positiva disuelve a la negativa. La tensión se disipa y se abre un espacio de liberación, tranquilidad y plenitud.</li>
<li><b>Integración.</b> En los días y semanas siguientes, lo que se liberó se va asentando en tu vida, hasta volverse tu nueva forma de vivir.</li>
</ol>
</div></section>

<section><div class="wrap grid2">
<div>
<p class="eyebrow">EN LA SESIÓN</p>
<h2>Un campo de presencia</h2>
<p>En una sesión yo no intento arreglarte, y tú no intentas forzar tu sanación. Juntos sostenemos un campo de presencia. En esa entrega actúa algo más grande que los dos: la Consciencia misma.</p>
<p>Entre más intervenga la mente, menos resultados habrá. Por eso soltamos. Muchas veces la catarsis llega sola, a veces en la sesión y a veces después, en sueños, recuerdos y vivencias intensas que sigues integrando en los días siguientes.</p>
<p>He formado facilitadores en este trabajo, y ellos viven lo mismo. Cuando el campo se sostiene, el alma sabe qué hacer.</p>
</div>
<figure><img class="portrait" src="{I}zuluan_library.jpg" alt="Dr. Zuluan Orion"></figure>
</div></section>

<section class="lav"><div class="narrow">
<p class="eyebrow">TODO LO DEMÁS, AL SERVICIO DEL ALMA</p>
<h2>Las herramientas que sostienen el trabajo</h2>
<p><a href="{url('es','ayurveda')}"><strong>La Ayurveda</strong></a> lee tu naturaleza y lo que la sacó de su equilibrio, y prepara al cuerpo para sostener la transformación.</p>
<p><a href="{url('es','energy')}"><strong>La biorresonancia</strong></a> trabaja sobre el campo energético y emocional, liberando cargas y memoria celular.</p>
<p><a href="{url('es','energy')}"><strong>El biofeedback</strong></a> muestra cómo responde todo tu sistema, para que el cuerpo aprenda de nuevo a descansar.</p>
<p><a href="{url('es','evaluations')}"><strong>El análisis de sangre en vivo</strong></a> ofrece un espejo visual de tu terreno interior.</p>
<p>Cada herramienta ayuda a ver, a aflojar y a sostener. La transformación en sí ocurre en la Consciencia.</p>
<p class="center" style="margin-top:30px"><a class="btn solid" href="{url('es','contact')}">Comienza tu proceso</a></p>
</div></section>
'''

X['ayurveda'] = hero('Ayurveda', 'La ciencia de la vida', sig=5) + f'''
<section><div class="wrap grid2">
<div>
<p class="lead">La Ayurveda no mira solo un síntoma. Te mira a ti.</p>
<p>La Ayurveda es la medicina tradicional de la India y tiene miles de años. La estudié y la viví en la India durante muchos años, y es la base sobre la que está mi clínica. Ve a la persona entera: tu naturaleza única, tu <em>prakriti</em>; el equilibrio de tus tres energías vitales, <em>vata</em>, <em>pitta</em> y <em>kapha</em>; tu digestión, tu mente y tu espíritu.</p>
<p>Para la Ayurveda, la salud es tu estado natural. Lo que llamamos enfermedad empieza mucho antes, como un desequilibrio silencioso que se va acumulando en el cuerpo, en las emociones y en la manera de vivir. En tu primera consulta conozco tu naturaleza y lo que la ha alejado de su centro. Desde ahí trazamos un camino hecho solo para ti.</p>
</div>
<figure><img class="portrait" src="{I}portrait_prayer.jpg" alt="Dr. Zuluan Orion"></figure>
</div></section>

<section class="alt"><div class="narrow">
<p class="eyebrow">PANCHAKARMA</p>
<h2>Las cinco acciones de purificación</h2>
<p>Con los años, el cuerpo va guardando lo que no logró digerir: alimentos, emociones, experiencias. La Ayurveda lo llama <strong>ama</strong>. Es un residuo que se asienta en los tejidos y en los canales, apaga el fuego digestivo, nubla la mente y deja el cuerpo pesado y cansado.</p>
<p>El Panchakarma es la gran limpieza profunda de la Ayurveda. Está diseñado para soltar ese residuo desde la raíz y devolverle al cuerpo su ligereza original.</p>
<h3>El camino</h3>
<ol class="steps">
<li><b>Preparación (Purvakarma).</b> Durante varios días tu cuerpo se nutre por dentro y por fuera con aceites medicinales y masajes (<em>abhyanga</em>), y se abre con calor y vapor de hierbas (<em>swedana</em>). Los tejidos se ablandan, y lo guardado se suelta y se dirige hacia donde puede salir. Para muchas personas, esta etapa ya es en sí misma una experiencia de entrega y descanso profundo.</li>
<li><b>Las cinco acciones (Pradhanakarma).</b> La tradición describe cinco vías de purificación. Yo elijo las que tú necesitas según tu naturaleza y tu momento: la limpieza del tracto superior, la limpieza intestinal suave, los enemas medicinales con aceites y decocciones de hierbas, el <em>nasya</em> (la purificación por la nariz, que despeja la cabeza y los sentidos) y la depuración de la sangre.</li>
<li><b>Regreso (Paschatkarma).</b> Después de la limpieza, tu fuego digestivo se reaviva paso a paso con una alimentación sencilla y cuidada, para que vuelvas a la vida diaria renovado y no cargado.</li>
</ol>
<h3>Lo que el Panchakarma puede hacer por ti</h3>
<ul class="benefits">
<li>Ligereza y claridad</li>
<li>Una digestión que vuelve a encenderse</li>
<li>Más energía y un sueño más profundo</li>
<li>Una piel más luminosa</li>
<li>Una mente más serena</li>
<li>Emociones que pesan menos</li>
</ul>
<p>Y algo más difícil de nombrar. Al limpiar el cuerpo, el alma también encuentra espacio. Muchas personas me cuentan que con el Panchakarma soltaron capas que llevaban años cargando.</p>
</div></section>

<section><div class="narrow">
<p class="eyebrow">RASAYANA</p>
<h2>El arte de la renovación</h2>
<p>Después de limpiar, viene nutrir. El Rasayana es la rama de la Ayurveda dedicada al rejuvenecimiento. Fortalece los tejidos, renueva la vitalidad y nutre el <strong>ojas</strong>, la esencia sutil que la Ayurveda considera la base de la inmunidad, la luz de tu piel, la estabilidad de tu mente y la alegría de vivir.</p>
<p>Por eso el Rasayana llega después del Panchakarma. Un cuerpo limpio recibe la nutrición como una tierra recién arada recibe la semilla.</p>
<h3>Cómo se vive el Rasayana</h3>
<ul class="benefits">
<li>Plantas y preparaciones rejuvenecedoras elegidas para tu naturaleza</li>
<li>Una alimentación que nutre el cuerpo y los sentidos</li>
<li>Rasayanas para la mente: claridad, memoria, calma</li>
<li><em>Achara Rasayana</em>, el rasayana de la conducta</li>
</ul>
<p>La Ayurveda enseña que la verdad, la compasión, la paz interior y una vida en armonía rejuvenecen tanto como cualquier planta. Aquí la Ayurveda y la Transformación Cuántica se encuentran.</p>
<h3>Lo que el Rasayana puede hacer por ti</h3>
<p>Más vitalidad y resistencia, un cuerpo más fuerte y flexible, la piel con brillo, una mente clara y estable, un mejor descanso y una sensación profunda de renovación, como si el cuerpo recordara su juventud.</p>
</div></section>

<section class="lav"><div class="narrow center">
<p class="eyebrow">Y MUCHO MÁS</p>
<h2>Un camino hecho para ti</h2>
<p>La Ayurveda no es una receta igual para todos. Además del Panchakarma y el Rasayana hay muchas otras terapias, y las elijo según tu naturaleza y tu momento: masajes con aceites medicinales, <em>shirodhara</em> (un hilo continuo de aceite tibio sobre la frente que lleva a una calma muy profunda), terapias con hierbas, orientación en alimentación y rutinas diarias, respiración y meditación.</p>
<p>En tu consulta encontramos juntos tu camino.</p>
<p><a class="btn solid" href="{url('es','contact')}">Reserva tu consulta</a></p>
</div></section>
'''

X['energy'] = hero('Terapias Energéticas', 'Biorresonancia · Biofeedback · Luz · Sonido', sig=7) + f'''
<section><div class="narrow">
<figure style="margin:0 0 30px"><img class="portrait" src="/assets/img/energy_bioresonance.jpg" alt="" style="width:100%"></figure>
<p class="eyebrow">BIORRESONANCIA · TRANSFERENCIA ENERGÉTICA</p>
<h2>Todo lo que vive, vibra</h2>
<p class="lead">Cada órgano, cada emoción y cada pensamiento tiene su propia frecuencia. Juntos forman el campo que rodea y sostiene tu cuerpo.</p>
<p>Cuando ese campo está en armonía, la vida fluye libremente a través de ti. Cuando guarda cargas antiguas, como el miedo que nunca se dijo, el duelo que nunca se lloró o los patrones heredados sin elegirlos, el flujo se vuelve lento. Con el tiempo lo sientes como pesadez, cansancio y malestar.</p>
<p>La biorresonancia trabaja en el nivel de ese campo. A través de un contacto suave en tus manos y tus pies, se leen las frecuencias propias de tu cuerpo y se le devuelven como información. Donde hay distorsión, se le ofrece al cuerpo la resonancia de su armonía original. Nada se fuerza. Tu propia consciencia decide qué está lista para soltar.</p>
<h3>Con qué trabajamos</h3>
<ul class="lineage">
<li><b>Los centros energéticos.</b> El equilibrio de los chakras y de los canales sutiles, para que la energía suba y descienda sin bloqueos, de la raíz a la corona.</li>
<li><b>Las emociones.</b> Encontrar las cargas emocionales guardadas en el cuerpo, como el miedo, la ira, la culpa y la tristeza, y dejar que se disuelvan en lugar de repetirse.</li>
<li><b>Las formas de pensamiento.</b> Traer a la luz las creencias y los patrones mentales que absorbimos de la familia, la cultura y las experiencias pasadas, para que pierdan su fuerza.</li>
<li><b>La memoria celular.</b> Cada célula recuerda. Las impresiones antiguas, algunas de la primera infancia y otras traídas por la línea familiar, pueden ser encontradas y liberadas, para que el cuerpo ya no tenga que revivirlas.</li>
<li><b>La capa epigenética.</b> Tu historia no tiene por qué ser tu destino. La forma en que vivimos, sentimos y pensamos moldea cómo el cuerpo expresa lo que lleva. Trabajar sobre el plano energético ayuda al cuerpo a expresar su orden original y no sus heridas acumuladas.</li>
<li><b>El peso emocional.</b> Cuando la tristeza se ha asentado en el cuerpo y la vida se ha vuelto gris, este trabajo ayuda a levantar ese peso, para que vuelvas a respirar y encuentres tu propio camino de regreso a la alegría.</li>
</ul>
<h3>Lo que muchas personas notan</h3>
<p>Ligereza y calma, un sueño más profundo, claridad mental, emociones que ya no desbordan, más energía, y una sensación serena de volver a casa, a ti mismo.</p>
</div><div class="wrap" style="margin-top:30px">{gallery(['clinic_session_01.jpg','clinic_session_02.jpg','clinic_session_03_diplomas.jpg'], 'tall')}</div></section>

<section class="alt"><div class="wrap grid2">
<figure><img class="portrait" src="{I}zuluan_chakra_scan_desk.jpg" alt="Evaluación energética en la clínica"></figure>
<div>
<p class="eyebrow">BIOFEEDBACK</p>
<h2>El cuerpo en conversación</h2>
<p>Tu cuerpo siempre está hablando: con la respiración, el latido, la piel, la tensión de los músculos. El biofeedback nos permite escucharlo. Sensores sin dolor siguen cómo responde tu sistema al estrés y a la calma, momento a momento. Cuando puedes ver esa respuesta, puedes aprender a guiarla.</p>
<p>En la sesión, el biofeedback muestra dónde el sistema nervioso guarda tensión y cómo responde todo tu ser, en lo físico, lo emocional y lo energético. Se convierte en un espejo, y con el espejo llega la elección. La respiración se calma, el corazón se serena y el cuerpo recuerda cómo descansar.</p>
<ul class="benefits">
<li>Relajación profunda y liberación del estrés guardado</li>
<li>Alivio de la tensión en cabeza, cuello y mandíbula</li>
<li>Un sueño más tranquilo</li>
<li>Emociones más estables, menos ansiedad</li>
<li>Más conciencia de tu cuerpo</li>
<li>Participar en tu propia sanación</li>
</ul>
<div class="gallery" style="grid-template-columns:1fr 1fr;margin-top:20px"><img src="/assets/img/eval_chakra_scan.jpg" alt="" loading="lazy"><img src="/assets/img/tuning_forks_detail.jpg" alt="" loading="lazy"></div>
</div>
</div></section>

<section><div class="narrow">
<p class="eyebrow">LUZ</p>
<h2>Terapias de luz</h2>
<p>La luz es información. En estas terapias suaves, la luz se lleva al cuerpo para apoyar su propia capacidad de regenerarse y para restablecer el flujo de la energía en los canales y puntos con los que trabajo. Son sesiones tranquilas y sin dolor, que se combinan de forma natural con las demás terapias.</p>
<ul class="lineage">
<li><b>Láser frío y transferencia de fotones.</b> Luz de baja intensidad que estimula la reparación y la regeneración celular, alivia el dolor y la tensión, favorece la circulación y el drenaje linfático, y relaja músculos y articulaciones. Las sesiones son cortas, por lo general de 15 a 30 minutos.</li>
<li><b>Terapia de bioluz.</b> Configuraciones de luz que liberan bloqueos energéticos, abren el flujo por los meridianos, los chakras y los nadis, apoyan la desintoxicación en todos los niveles y ofrecen una experiencia de relajación profunda y dicha.</li>
</ul>
</div></section>

<section class="alt"><div class="wrap grid2">
<div>
<p class="eyebrow">MEDICINA HOLÍSTICA</p>
<h2>Marma, sonido y vibración</h2>
<p>Parte de la sanación más profunda ocurre a través del tacto y del sonido. En mis sesiones trabajo con:</p>
<ul class="lineage">
<li><b>Puntos Marma.</b> Los puntos vitales de la Ayurveda, puertas de la fuerza vital. Trabajar con ellos sostiene el flujo de la energía, armoniza cuerpo y mente y revitaliza todo el ser.</li>
<li><b>Diapasones.</b> Vibraciones precisas que devuelven la armonía al sistema energético, invitan al cuerpo a regresar a su equilibrio natural y ayudan a soltar pensamientos y emociones pesadas.</li>
<li><b>Campanas.</b> Sonidos claros que limpian el campo de energías densas y abren el camino a la calma y a un trabajo más profundo con los chakras.</li>
<li><b>Cuencos de cristal.</b> Tonos sostenidos que llegan al aura y a las ondas cerebrales, aquietan la mente y llevan la meditación a la quietud.</li>
</ul>
</div>
<figure><img class="portrait" src="/assets/img/zuluan_tuning_forks.jpg" alt="El Dr. Zuluan Orion con diapasones"></figure>
</div></section>

<section class="lav"><div class="narrow center">
<h2>Un camino, tres lenguajes</h2>
<p>En mi clínica, la Ayurveda, la biorresonancia y el biofeedback no son tratamientos separados. Son tres formas de escuchar al mismo ser. La Ayurveda lee tu naturaleza y lo que la sacó de su equilibrio. La biorresonancia habla al campo energético y emocional. El biofeedback deja que el cuerpo nos muestre a los dos cómo está respondiendo. Las tres sirven al trabajo de la <a href="{url('es','quantum-transformation')}">Transformación Cuántica</a>.</p>
<p><a class="btn solid" href="{url('es','contact')}">Reserva una sesión</a></p>
</div></section>
'''

X['evaluations'] = hero('Evaluaciones', 'Ver el terreno interior', sig=9) + f'''
<section><div class="narrow">
<p class="eyebrow">ANÁLISIS DE SANGRE EN VIVO</p>
<h2>Una gota viva, vista con ojos holísticos</h2>
<p class="lead">Una sola gota de tu sangre, vista viva bajo el microscopio, cuenta una historia.</p>
<p>En el análisis de sangre en vivo miramos juntos, en una pantalla y en tiempo real, una gota de sangre fresca. Yo la leo con una mirada holística: el estado del terreno, cómo se mueven y se relacionan las células, lo que la sangre muestra sobre la digestión, sobre la carga que el cuerpo está llevando, sobre la vitalidad.</p>
<p>Para muchas personas es la primera vez que realmente ven su mundo interior, y ese momento de ver ya es parte de la transformación. Lo repetimos con el tiempo y vemos cómo el terreno cambia a medida que tú cambias.</p>
</div>
<div class="wrap" style="margin-top:34px">{gallery(LBA, 'tall')}</div>
</section>

<section class="alt"><div class="wrap grid3">
<div class="card"><img src="/assets/img/eval_bioterrain.jpg" alt="Análisis bioquímico y del bioterreno" loading="lazy" style="width:100%;aspect-ratio:4/3;object-fit:cover;margin-bottom:18px"><p class="eyebrow">ANÁLISIS DEL BIOTERRENO</p><h3>La química del equilibrio</h3><p>Una lectura de tu terreno biológico a través de la sangre, la saliva y la orina: más de sesenta marcadores del medio interno donde viven tus células, como el equilibrio ácido-alcalino, la resistencia al estrés y la desintoxicación. Me muestra dónde tu sistema está haciendo un esfuerzo y qué necesita para volver al equilibrio.</p></div>
<div class="card"><img src="/assets/img/eval_gdv_kirlian.jpg" alt="" loading="lazy" style="width:100%;aspect-ratio:4/3;object-fit:cover;margin-bottom:18px"><p class="eyebrow">IMAGEN DEL CAMPO ENERGÉTICO</p><h3>GDV y Kirlian</h3><p>Imágenes del campo de luz que rodea al cuerpo. Muestran cómo se distribuye tu energía y dónde está más débil o bloqueada, para que podamos seguir tus chakras y tu campo a medida que avanza el trabajo.</p></div>
<div class="card"><img src="/assets/img/eval_chakra_scan.jpg" alt="" loading="lazy" style="width:100%;aspect-ratio:4/3;object-fit:cover;margin-bottom:18px"><p class="eyebrow">EVALUACIÓN ENERGÉTICA</p><h3>El escaneo de chakras</h3><p>Una evaluación de tus centros energéticos que me muestra por dónde empezar, para que cada sesión vaya directo a lo que tu alma necesita ahora.</p></div>
</div></section>

<section><div class="narrow center">
<p>Las evaluaciones no son un fin en sí mismas. Son un espejo, para que tú y yo podamos ver dónde estás y recorrer juntos el camino de la <a href="{url('es','quantum-transformation')}">Transformación Cuántica</a>.</p>
<p><a class="btn solid" href="{url('es','contact')}">Agenda una evaluación</a></p>
</div></section>
'''

CRED_ES = '''<table class="cred">
<tr><td>MD en Ayurveda (Vaidya Shiromani / Vachaspati)</td><td>India</td></tr>
<tr><td>Licenciatura en Medicina y Ciencia Ayurvédica (B.A.M.S.)</td><td>India</td></tr>
<tr><td>Ph.D. en Medicina Natural — World Organization of Natural Medicine</td><td>2014</td></tr>
<tr><td>Ph.D. en Medicina Cuántica</td><td>2014</td></tr>
<tr><td>Doctorado en Servicios Humanitarios — World Organization of Natural Medicine</td><td>2013</td></tr>
<tr><td>Miembro del Consejo Académico — AAPNA, Association of Ayurvedic Professionals of North America</td><td></td></tr>
<tr><td>Miembro — NAMA, National Ayurvedic Medical Association</td><td></td></tr>
</table>'''

X['about'] = hero('Dr. Zuluan Orion', 'Originador de la Transformación Cuántica · Cognizador de los Códigos de Luz', sig=3) + f'''
<section><div class="wrap grid2 top">
<figure><img class="portrait" src="{I}portrait_side.jpg" alt="Dr. Zuluan Orion"></figure>
<div>
<p class="lead">Nací en Bogotá en 1971. Crecí en un hogar difícil, y el vacío que dejó en mi corazón se volvió el comienzo de mi camino espiritual. Necesitaba encontrar algo, aunque no sabía qué.</p>
<p>Esa búsqueda me llevó a más de sesenta mil horas de meditación y a casi dos décadas viviendo y estudiando en Asia: doce años y medio en la India, con el yoga, la meditación y la medicina ayurvédica, y ocho en Tailandia, con el budismo y la sanación. En el camino llegó un despertar al Ser que, en casi treinta años, no se ha revertido.</p>
<p>De esa vida nacieron las dos cosas que ofrezco. La <strong>Transformación Cuántica</strong> es el sistema que creé para guiar al alma a través de sus propios niveles de Consciencia, hasta la raíz de lo que duele, y de regreso a su luz. Los <strong>Códigos de Luz</strong> son un lenguaje sagrado de sílabas y sigilos que recibí y reconocí, y viven en el corazón del Códice de la Llama.</p>
<p>Desde hace dos décadas los uno en mi clínica de Weston, Florida, con la medicina ayurvédica, natural y cuántica, y con personas de muchos países.</p>
<p class="signature">Yo no soy la fuente. La Consciencia lo es. Mi trabajo es devolverte a la luz que nunca perdiste.</p>
</div>
</div></section>

<section class="dark"><div class="wrap">
<div class="stats">
<div><b>60.000+</b><span>horas de meditación</span></div>
<div><b>12½ años</b><span>en la India</span></div>
<div><b>8 años</b><span>en Tailandia</span></div>
<div><b>20+ años</b><span>cuidando personas en esta clínica</span></div>
</div>
</div></section>

''' + grace_about('es') + f'''<section><div class="wrap sister">
<img src="{S(10)}" alt="" style="width:200px">
<div>
<p class="eyebrow">MI HISTORIA COMPLETA</p>
<h2>Dr. Zuluan Orion</h2>
<p>Mis maestros y linajes, el despertar, el descenso de la Llama, mis reconocimientos y todos mis libros están contados en detalle en mi sitio personal. Los Códigos de Luz viven en el sitio del Códice de la Llama.</p>
<a class="btn solid" href="https://drzuluanorion.org/es/story/">Lee mi historia ↗</a> <a class="btn" href="{fc('es','codex')}">Los Códigos de Luz ↗</a>
</div>
</div></section>

<section class="alt"><div class="wrap">
<div class="grid2 top">
<div>
<p class="eyebrow">MEDICINA</p>
<h2>Estudios y credenciales</h2>
{CRED_ES}
</div>
<figure><img class="portrait" src="{I}press_tv_studio_01.jpg" alt="El Dr. Zuluan Orion en televisión"><figcaption>Presentando <em>Deshojando el Corazón de la Eternidad</em> en televisión, en Miami.</figcaption></figure>
</div>
<h2 style="margin-top:60px">Reconocimientos</h2>
<div class="awards">
<figure><img src="{I}award_aapna_2025_ceremony.jpg" alt="Ceremonia del Premio Dhanwantari, AAPNA" loading="lazy"><figcaption>Premio Dhanwantari, AAPNA, 2025, por integrar la Ayurveda con la ciencia contemporánea.</figcaption></figure>
<figure><img src="{I}award_aapna_2025.jpg" alt="Con el premio de AAPNA" loading="lazy"><figcaption>AAPNA, 2025.</figcaption></figure>
<figure><img src="{I}award_siisdet_2022.jpg" alt="Health Sciences Awards 2022" loading="lazy"><figcaption>Líder en Investigación y Ciencias de la Salud en Beneficio de la Humanidad, Health Sciences Awards, Santander, España, 2022.</figcaption></figure>
<figure><img src="{I}award_lifestyle.jpg" alt="Lifestyle Plus Magazine Awards" loading="lazy"><figcaption>Lifestyle Plus Magazine Awards.</figcaption></figure>
</div>
<h2 style="margin-top:60px">Con médicos ayurvédicos</h2>
<p>La Ayurveda es una tradición viva, y la comparto con médicos ayurvédicos de la India.</p>
<figure style="max-width:720px;margin:26px 0"><img class="portrait" src="/assets/img/kerala_dr_reddy_kumar.jpg" alt="Estudiando medicina ayurvédica con el Dr. Reddy Kumar" loading="lazy"><figcaption>Estudiando medicina ayurvédica al lado del Dr. Reddy Kumar, Universidad de Kerala, India.</figcaption></figure>
<div class="gallery tall" style="grid-template-columns:repeat(3,1fr);max-width:1000px">
<figure><img src="/assets/img/with_dr_shekhar_annambhotla.jpg" alt="Con el Dr. Shekhar Annambhotla" loading="lazy"><figcaption>Con el Dr. Shekhar Annambhotla, BAMS, MD (Ayurveda).</figcaption></figure>
<figure><img src="/assets/img/with_dr_suresh_swarnapuri.jpg" alt="Con el Dr. Suresh Swarnapuri" loading="lazy"><figcaption>Con el Dr. Suresh Swarnapuri, BAMS, MD (Ayurveda).</figcaption></figure>
<figure><img src="/assets/img/with_dr_shan_lakshmanan.jpg" alt="Con el Dr. Shan Lakshmanan, Ph.D" loading="lazy"><figcaption>Con el Dr. Shan Lakshmanan, Ph.D.</figcaption></figure>
</div>
</div></section>
'''

X['books'] = hero('Libros', 'Del Dr. Zuluan Orion', sig=12) + books_body('es')

X['contact'] = hero('Visítanos', 'Spiritual Balance · Weston, Florida', sig=18) + catalogue_band('es') + f'''
<section><div class="wrap grid2 top">
<div class="visit">
<p class="lead">Será un gusto recibirte.</p>
<p>Escríbeme o llámame para reservar tu primera consulta. Hablaremos de lo que te trae, y juntos elegiremos por dónde empezar.</p>
<dl>
<dt>DIRECCIÓN</dt><dd>1565 North Park Drive, Suite 101<br>Weston, Florida 33326</dd>
<dt>TELÉFONO</dt><dd><a href="tel:+19546680348">(954) 668-0348</a></dd>
<dt>CORREO</dt><dd><a href="mailto:spiritualbalanceinfo@gmail.com">spiritualbalanceinfo@gmail.com</a></dd>
<dt>HORARIO</dt><dd>Lunes a viernes, 9 am – 6 pm<br>Sábados, 9 am – 1 pm</dd>
<dt>IDIOMAS</dt><dd>Español e inglés</dd>
</dl>
<p style="margin-top:28px"><a class="btn solid" href="tel:+19546680348">Llamar</a> <a class="btn" href="https://maps.google.com/?q=1565+N+Park+Drive+Suite+101+Weston+FL+33326">Cómo llegar</a></p>
</div>
<figure><img class="portrait" src="{I}clinic_buddha_waiting_room.jpg" alt="La sala de espera de Spiritual Balance" style="max-height:640px;width:auto;margin:0 auto"></figure>
</div></section>
'''

E['retreats'] = hero('Journeys &amp; Retreats', 'Holistic journeys with Dr. Zuluan Orion', sig=10) + retreats('en')
X['retreats'] = hero('Viajes y Retiros', 'Viajes holísticos con el Dr. Zuluan Orion', sig=10) + retreats('es')

# catalogue download on every service page
for _k in ('quantum-transformation', 'ayurveda', 'energy', 'evaluations'):
    E[_k] += catalogue_band('en'); X[_k] += catalogue_band('es')

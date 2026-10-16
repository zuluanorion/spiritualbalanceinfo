# spiritualbalanceinfo.com

Bilingual site of Spiritual Balance — Dr. Zuluan Orion, Weston, Florida.
English at /, Spanish at /es/. Static files in public/, served by Cloudflare Workers (wrangler.jsonc).
Sister sites: drzuluanorion.org (Dr. Zuluan Orion) · www.theflamecodex.com (the Codex).

## Source
webgen/ holds the generator (Python 3, no extra packages). Cloudflare serves only public/.
Rebuild: `python3 webgen/build.py` rewrites the HTML in public/; the images and PDFs stay as they are.

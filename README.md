# ADITUP — Safety Audit (PWA)

ADITUP is a fully offline HSE safety-audit app: log observations, run risk &
legal assessment, view a 7-chart analytics dashboard, and export
brand-compliant Excel, PowerPoint, and PDF reports — all with no internet
connection and no servers.

This package wraps the app as an **installable Progressive Web App (PWA)**, so
it can be added to a phone or desktop home screen and launched like a native
app, working offline after the first load.

---

## What's in this folder

| File | Purpose |
|------|---------|
| `index.html` | The entire ADITUP app (self-contained) |
| `manifest.webmanifest` | App name, icons, colors, display mode |
| `service-worker.js` | Caches the app so it runs offline |
| `icons/` | App icons (192 / 512 / maskable / Apple) |
| `serve.py` | Tiny local web server (Python 3) |
| `Start ADITUP (Windows).bat` | Double-click launcher for Windows |
| `Start ADITUP (Mac-Linux).command` | Double-click launcher for macOS/Linux |

---

## Important: PWAs must be served over http(s)

A PWA's offline caching and **"Install app"** prompt **only work when the page
is served over `http://` or `https://`** — not when you open `index.html`
directly from disk (`file://`). This is a browser security rule, not an ADITUP
limitation.

You have two ways to satisfy this: run it locally, or host it.

---

## Option A — Run locally (quickest, for testing/personal use)

You need **Python 3** installed (already present on most Macs/Linux; on Windows
get it from https://www.python.org/downloads/ and tick "Add to PATH").

- **Windows:** double-click `Start ADITUP (Windows).bat`
- **macOS / Linux:** double-click `Start ADITUP (Mac-Linux).command`
  (first time on macOS you may need to right-click → Open to bypass Gatekeeper)
- **Or from a terminal:** `python3 serve.py`

Your browser opens `http://localhost:8000/index.html`. To install it as an app,
use the browser's install control:

- **Chrome / Edge (desktop):** the install icon (⊕ or a screen icon) in the
  address bar, or menu → *Install ADITUP*.
- **Android Chrome:** menu → *Add to Home screen* / *Install app*.
- **iOS Safari:** Share → *Add to Home Screen* (iOS doesn't use the manifest
  install prompt, but the app shell still works offline once cached).

Once installed, it runs in its own window, offline.

---

## Option B — Host it (best for sharing with a team)

Upload the **contents of this folder** to any static host. No build step.

- **GitHub Pages:** create a repo, upload these files, enable Pages on the
  branch. Your URL becomes `https://<user>.github.io/<repo>/`.
- **Netlify / Cloudflare Pages / Vercel:** drag-and-drop this folder; you get an
  https URL instantly.
- **Any web server:** copy the folder into the served directory.

Open the hosted URL and install as above. Because the host is https, install and
offline work automatically for anyone you share the link with.

---

## Updating the app

When you change `index.html`, bump the version string in
`service-worker.js`:

```js
const CACHE_VERSION = 'aditup-v1';   // change to 'aditup-v2', etc.
```

Reload the page once (twice on some browsers); the service worker fetches the
new files and discards the old cache.

---

## A note on fonts

The app uses the **Montserrat** font. If the device has it or can reach Google
Fonts on first load, text renders in Montserrat; the service worker then caches
it for offline use. With no internet on first run, the app falls back to the
system sans-serif — fully functional, just a slightly different look until
Montserrat is cached.

---

## Privacy

ADITUP runs entirely on the device. Audit data, photos, and exports never leave
the browser — there is no backend and no analytics. Note that data is held in
the browser session; exporting (Excel/PPT/PDF) is how you save a permanent copy.

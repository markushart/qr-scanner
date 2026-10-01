# 📷 Web QR-Code Scanner

A lightweight, modern, client-side QR code scanner web application built with HTML5, Tailwind CSS, and `html5-qrcode`. Optimized for both desktop and mobile browsers (iOS & Android).

---

## ✨ Features

- **⚡ Fast Live Camera Scanning**: Uses native hardware-accelerated `BarcodeDetector` API when available, falling back to ZXing.
- **📱 Full-Frame Recognition**: Scans QR codes anywhere across the camera feed without forcing strict, tiny viewfinder crops.
- **🔄 Camera Switching**: Automatically enumerates all connected cameras (front/rear, external webcams, virtual cameras) with a live dropdown selector.
- **🖼️ Photo / File Upload**: Tap "Foto / Datei wählen" to scan saved images or use the native smartphone camera with autofocus and flash.
- **🔁 Deduplication & Counter**: Tracks unique codes, avoids accidental duplicate registrations, and counts scanned items.
- **🔗 Clickable URLs & Timestamping**: Automatically turns `http://` and `https://` results into clickable links with German-formatted timestamps.
- **🔊 Visual & Audio Feedback**: Green pulse animation and synthesized audio chime (Web Audio API) on successful scans.
- **🗑️ History Management**: View recent scans or clear the scan list anytime.

---

## 🚀 Live Demo on GitHub Pages

Once deployed on GitHub Pages, the application is automatically served over **trusted HTTPS**, allowing instant camera access on mobile devices (iOS Safari & Android Chrome) without any SSL warnings.

**URL format:**
```text
https://<username>.github.io/<repository-name>/
```

---

## 💻 Running Locally

### Option 1: Local HTTPS Server (Recommended for mobile testing)

Because iOS Safari and Android Chrome require a secure context (`HTTPS`) for camera permissions, run the included Python HTTPS server:

```bash
# 1. Generate local SSL certificate (if not already present):
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=localhost"

# 2. Start the server:
python3 serve_https.py
```

Open the displayed URL (e.g. `https://192.168.x.x:8443`) on your smartphone or desktop browser.

### Option 2: Plain HTTP (Desktop / File Upload testing)

```bash
python3 -m http.server 8000
```
Open `http://localhost:8000` in your desktop browser.

---

## 🛠️ Tech Stack

- **HTML5 & Vanilla JavaScript (ES6+)**
- **[Tailwind CSS](https://tailwindcss.com/)** (via CDN)
- **[html5-qrcode](https://github.com/mebjas/html5-qrcode)** (via CDN)
- **Web Audio API**

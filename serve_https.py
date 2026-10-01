import http.server
import ssl
import socket
import os

PORT = 8443
DIR = os.path.dirname(os.path.abspath(__file__))

def get_ips():
    ips = []
    # Primary outbound IP
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ips.append(s.getsockname()[0])
        s.close()
    except Exception:
        pass
    
    # Common local IPs
    for fallback in ['192.168.178.66', '192.168.178.21']:
        if fallback not in ips:
            ips.append(fallback)
    return ips

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

server_address = ('0.0.0.0', PORT)
httpd = http.server.HTTPServer(server_address, Handler)

cert_file = os.path.join(DIR, "cert.pem")
key_file = os.path.join(DIR, "key.pem")

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=cert_file, keyfile=key_file)
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

ips = get_ips()
print("=" * 60)
print(f"🔒 HTTPS Server aktiv auf Port {PORT}")
print("=" * 60)
print("Öffne auf deinem iPhone im Safari-Browser eine dieser Adressen:\n")
for ip in ips:
    print(f"   👉 https://{ip}:{PORT}/qr_code_scanner.html")
print("\n" + "-" * 60)
print("ℹ️  Hinweis für iOS Safari:")
print("   Da das Zertifikat selbstsigniert ist, zeigt Safari:")
print("   'Diese Verbindung ist nicht privat'.")
print("   Tippe auf: 'Details einblenden' -> 'diese Website besuchen'.")
print("   Danach funktioniert die Kamera einwandfrei!")
print("=" * 60 + "\n")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer gestoppt.")

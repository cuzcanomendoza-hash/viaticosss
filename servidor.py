#!/usr/bin/env python3
"""
Servidor HTTP simple para compartir el sistema de viáticos localmente.
Ejecuta este script para iniciar un servidor web que permite acceder al sistema desde otros dispositivos en la misma red.
"""

import http.server
import socketserver
import socket
import webbrowser
import os

# Puerto por defecto
PORT = 8000

# Obtener la IP local
def get_local_ip():
    """Obtiene la IP local de la máquina"""
    try:
        # Conecta a una dirección externa para obtener la IP local
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Handler personalizado para servir archivos"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(os.path.abspath(__file__)), **kwargs)
    
    def end_headers(self):
        # Agregar headers CORS para permitir acceso desde otros dispositivos
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def log_message(self, format, *args):
        """Personalizar mensajes de log"""
        print(f"[{self.log_date_time_string()}] {format % args}")

def main():
    """Función principal para iniciar el servidor"""
    # Cambiar al directorio del script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Intentar encontrar un puerto disponible
    port = PORT
    while True:
        try:
            with socketserver.TCPServer(("", port), MyHTTPRequestHandler) as httpd:
                local_ip = get_local_ip()
                
                print("=" * 60)
                print("🚀 Servidor de Sistema de Viáticos iniciado")
                print("=" * 60)
                print(f"\n📍 Acceso local:")
                print(f"   http://localhost:{port}")
                print(f"   http://127.0.0.1:{port}")
                print(f"\n🌐 Acceso desde otros dispositivos en la misma red:")
                print(f"   http://{local_ip}:{port}")
                print(f"\n📱 Para compartir con otros:")
                print(f"   1. Asegúrate de que estén en la misma red WiFi")
                print(f"   2. Comparte esta URL: http://{local_ip}:{port}")
                print(f"   3. O escanea el código QR si tienes una herramienta para generarlo")
                print("\n" + "=" * 60)
                print("💡 Presiona Ctrl+C para detener el servidor")
                print("=" * 60 + "\n")
                
                # Abrir navegador automáticamente
                try:
                    webbrowser.open(f'http://localhost:{port}/index.html')
                except:
                    pass
                
                # Iniciar servidor
                httpd.serve_forever()
                
        except OSError as e:
            if e.errno == 48 or e.errno == 98:  # Puerto en uso
                print(f"⚠️  Puerto {port} está en uso. Intentando con {port + 1}...")
                port += 1
            else:
                print(f"❌ Error al iniciar el servidor: {e}")
                break
        except KeyboardInterrupt:
            print("\n\n🛑 Servidor detenido por el usuario.")
            break

if __name__ == "__main__":
    main()

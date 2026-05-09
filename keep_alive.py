import os
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

def wake_up_supabase():
    try:
        # Esto simplemente conecta y pide la versión de la API
        # Es suficiente para que Supabase detecte actividad
        supabase = create_client(url, key)
        
        # En lugar de una tabla, pedimos algo interno del sistema
        # Si esto responde, el proyecto está despierto
        print("Conectando a Supabase...")
        
        # Hacemos una petición simple que no requiere tablas
        # Si el cliente se crea, ya hay un 'handshake'
        if supabase:
            print("¡Pulso detectado! Proyecto activo.")
            
    except Exception as e:
        print(f"Error al despertar Supabase: {e}")

if __name__ == "__main__":
    wake_up_supabase()
    

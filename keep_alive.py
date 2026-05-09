import os
from supabase import create_client

# Estas variables las configuraremos en GitHub, no las pongas aquí directamente
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

def wake_up_supabase():
    try:
        supabase = create_client(url, key)
        # Hacemos una consulta simple a cualquier tabla que tengas (ej. 'personajes')
        # Solo pedimos una fila para no gastar recursos
        response = supabase.table('tu_tabla_aqui').select("*").limit(1).execute()
        print("¡Supabase despertó con éxito!")
    except Exception as e:
        print(f"Error al despertar Supabase: {e}")

if __name__ == "__main__":
    wake_up_supabase()

import pandas as pd
import os

def cargar_productos(path='dataset.csv'):
    """
    Carga el CSV de productos desde la ruta indicada.
    """
    try:
        # Verificar si el archivo existe
        if not os.path.exists(path):
            print(f"Error: Archivo no encontrado en {path}")
            # Crear dataset de ejemplo si no existe
            return crear_dataset_ejemplo()
        
        df = pd.read_csv(path)
        print(f"Productos cargados: {len(df)} registros")
        return df
    except Exception as e:
        print(f"Error al cargar productos: {e}")
        return crear_dataset_ejemplo()

def crear_dataset_ejemplo():
    """Crea un dataset de ejemplo si no existe el archivo"""
    data = {
        'id': [1, 2, 3, 4, 5, 6, 7, 8],
        'nombre_producto': [
            'Camisa Azul', 'Zapatillas Rojas', 'Pantalón Negro', 
            'Smartphone Phone 17', 'Audífonos Inalámbricos', 
            'Reloj Inteligente', 'Zapatos Formales', 'Gorra Casual'
        ],
        'categoria': ['Ropa', 'Calzado', 'Ropa', 'Electrónica', 
                     'Electrónica', 'Electrónica', 'Calzado', 'Ropa'],
        'precio': [50, 120, 70, 500, 80, 200, 150, 25],
        'descripcion': [
            'Camisa de algodón, talla M',
            'Zapatillas deportivas, talla 42',
            'Pantalón formal de tela, talla L',
            'Teléfono con 128GB de memoria',
            'Audífonos bluetooth con cancelación de ruido',
            'Reloj con monitor de actividad y notificaciones',
            'Zapatos de cuero elegantes',
            'Gorra de algodón ajustable'
        ],
        'imagen': [
            'https://via.placeholder.com/200x200/007BFF/FFFFFF?text=Camisa',
            'https://via.placeholder.com/200x200/DC3545/FFFFFF?text=Zapatillas',
            'https://via.placeholder.com/200x200/343A40/FFFFFF?text=Pantalon',
            'https://via.placeholder.com/200x200/28A745/FFFFFF?text=Smartphone',
            'https://via.placeholder.com/200x200/6C757D/FFFFFF?text=Audifonos',
            'https://via.placeholder.com/200x200/FFC107/000000?text=Reloj',
            'https://via.placeholder.com/200x200/17A2B8/FFFFFF?text=Zapatos',
            'https://via.placeholder.com/200x200/6F42C1/FFFFFF?text=Gorra'
        ]
    }
    return pd.DataFrame(data)

def filtrar_por_categoria(df, categoria):
    if categoria is None:
        return df
    return df[df['categoria'].str.contains(categoria, case=False, na=False)]

def filtrar_por_precio(df, min_precio=None, max_precio=None):
    if min_precio is not None:
        df = df[df['precio'] >= min_precio]
    if max_precio is not None:
        df = df[df['precio'] <= max_precio]
    return df

def recomendar_producto(df, categoria=None, min_precio=None, max_precio=None, n=3):
    filtrado = df.copy()
    
    if categoria:
        filtrado = filtrar_por_categoria(filtrado, categoria)
    
    filtrado = filtrar_por_precio(filtrado, min_precio, max_precio)
    
    if filtrado.empty:
        filtrado = df  # fallback si no hay coincidencias
    
    # Mezclar y tomar n productos
    return filtrado.sample(min(n, len(filtrado))).to_dict(orient='records')
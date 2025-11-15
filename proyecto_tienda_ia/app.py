import streamlit as st
import pandas as pd

# --- Configuración de la página con fondo blanco ---
st.set_page_config(
    page_title="StyleShop - Ecommerce Elegante", 
    layout="wide", 
    page_icon="🛍️",
    initial_sidebar_state="collapsed"
)

# --- Forzar fondo blanco ---
st.markdown("""
<style>
    /* Fondo blanco para toda la aplicación */
    .stApp {
        background-color: white;
    }
    
    /* Eliminar cualquier fondo oscuro */
    .main {
        background-color: white;
    }
    
    /* Header principal */
    .main-title {
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 1rem;
        padding: 1rem;
    }
    
    /* Cambiar color de todas las letras a azul oscuro */
    .stMarkdown, .stSubheader, .stWrite, .stText {
        color: #2c3e50 !important;
    }
    
    /* Color específico para subtítulos */
    .stSubheader {
        color: #34495e !important;
        font-weight: 600;
    }
    
    /* Color para textos normales */
    .stWrite {
        color: #2c3e50 !important;
    }
    
    /* Tarjetas de productos */
    .product-card {
        border: 1px solid #e0e0e0;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        background: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        text-align: center;
        height: 480px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.12);
    }
    
    /* Imágenes con tamaño fijo y borde - SIN ENCABEZADOS */
    .product-image-container {
        width: 100%;
        height: 200px;
        border-radius: 10px;
        overflow: hidden;
        margin-bottom: 1rem;
        border: 2px solid #f0f0f0;
        background: #f8f9fa;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .product-image {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    
    /* Chatbot styles */
    .chat-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px 15px 0 0;
        text-align: center;
    }
    .chat-container {
        border: 1px solid #e0e0e0;
        border-top: none;
        border-radius: 0 0 15px 15px;
        padding: 1.5rem;
        background-color: #fafafa;
        height: 500px;
        overflow-y: auto;
        margin-bottom: 1rem;
    }
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 10px 15px;
        border-radius: 18px 18px 5px 18px;
        margin: 8px 0;
        max-width: 80%;
        margin-left: auto;
        font-size: 0.9rem;
    }
    .bot-message {
        background: white;
        color: #2c3e50;
        padding: 10px 15px;
        border-radius: 18px 18px 18px 5px;
        margin: 8px 0;
        max-width: 80%;
        border: 1px solid #e0e0e0;
        font-size: 0.9rem;
    }
    
    /* Botones */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    
    /* Precio */
    .price-tag {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-weight: bold;
        font-size: 1.2rem;
        display: inline-block;
        margin: 0.5rem 0;
    }
    
    /* Categoría */
    .category-badge {
        background: #e9ecef;
        color: #2c3e50;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.8rem;
        display: inline-block;
        margin-bottom: 0.5rem;
        font-weight: 500;
    }
    
    /* Filtros section */
    .filter-section {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        border: 1px solid #e0e0e0;
    }
    
    /* Texto de descripción del producto */
    .product-description {
        color: #2c3e50;
        font-size: 0.9rem;
        line-height: 1.4;
    }
    
    /* Títulos de productos */
    .product-title {
        color: #2c3e50;
        font-weight: 600;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# --- Datos de productos con imágenes que SÍ funcionan ---
def crear_productos():
    # Usar imágenes de Unsplash que siempre funcionan
    productos_data = {
        'id': range(1, 13),
        'nombre_producto': [
            'Camisa Elegante Azul', 
            'Zapatillas Running Pro', 
            'Jeans Slim Fit', 
            'iPhone 14 Pro',
            'Audífonos Sony WH', 
            'Apple Watch Series', 
            'Zapatos de Cuero', 
            'Gorra Nike Classic',
            'Laptop Gaming ASUS',
            'Tablet Samsung',
            'Cámara Canon',
            'Teclado Mecánico'
        ],
        'categoria': ['Ropa', 'Calzado', 'Ropa', 'Electrónica', 'Electrónica', 'Electrónica', 'Calzado', 'Ropa', 'Electrónica', 'Electrónica', 'Electrónica', 'Electrónica'],
        'precio': [49, 129, 69, 999, 299, 399, 159, 29, 899, 449, 799, 89],
        'descripcion': [
            'Camisa de algodón premium color azul marino',
            'Zapatillas profesionales para running y entrenamiento',
            'Jeans ajustados de alta calidad, color azul oscuro',
            'iPhone 14 Pro 256GB, cámara profesional',
            'Audífonos con cancelación de ruido activa',
            'Smartwatch con monitor de salud y GPS',
            'Zapatos formales de cuero genuino italiano',
            'Gorra deportiva Nike, ajustable y cómoda',
            'Laptop gaming RTX 3060, 16GB RAM, 1TB SSD',
            'Tablet Samsung S8, S-Pen incluido, 128GB',
            'Cámara DSLR Canon EOS 90D, 32.5MP',
            'Teclado mecánico gaming RGB, switches azules'
        ],
        'imagen': [
            "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=300&h=200&fit=crop",  # Camisa
            "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=300&h=200&fit=crop",    # Zapatillas
            "https://images.unsplash.com/photo-1542272604-787c3835535d?w=300&h=200&fit=crop",    # Jeans
            "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=300&h=200&fit=crop", # iPhone
            "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=300&h=200&fit=crop", # Audífonos
            "https://images.unsplash.com/photo-1579586337278-3f436c25d4a5?w=300&h=200&fit=crop", # Apple Watch
            "https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?w=300&h=200&fit=crop", # Zapatos
            "https://images.unsplash.com/photo-1588850561407-ed78c282e89b?w=300&h=200&fit=crop", # Gorra
            "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=300&h=200&fit=crop", # Laptop
            "https://images.unsplash.com/photo-1558618666-fcd25856cd63?w=300&h=200&fit=crop",   # Tablet
            "https://images.unsplash.com/photo-1515376721779-7db6951ea88b?w=300&h=200&fit=crop", # Cámara
            "https://images.unsplash.com/photo-1541140532154-b024d705b90a?w=300&h=200&fit=crop"  # Teclado
        ]
    }
    return pd.DataFrame(productos_data)

# --- Funciones del sistema ---
def recomendar_productos(df, categoria=None, precio_max=None):
    productos_filtrados = df.copy()
    
    if categoria and categoria != "Todas":
        productos_filtrados = productos_filtrados[productos_filtrados['categoria'] == categoria]
    
    if precio_max:
        productos_filtrados = productos_filtrados[productos_filtrados['precio'] <= precio_max]
    
    if len(productos_filtrados) == 0:
        return df.head(3).to_dict('records')
    
    return productos_filtrados.sample(min(3, len(productos_filtrados))).to_dict('records')

# --- Cargar productos ---
productos = crear_productos()

# --- Header Principal ---
st.markdown('<div class="main-title">🛍️ StyleShop</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center; color: #2c3e50; font-size: 1.2rem; margin-bottom: 2rem;">Descubre productos increíbles con nuestro asistente inteligente</div>', unsafe_allow_html=True)

# --- Layout Principal ---
col_productos, col_chatbot = st.columns([7, 3])

with col_productos:
    # --- Sección de Filtros ---
    st.markdown('<div class="filter-section">', unsafe_allow_html=True)
    st.markdown("### 🔍 Encuentra tu producto ideal")
    
    col_f1, col_f2, col_f3 = st.columns(3)
    
    with col_f1:
        categorias = ["Todas"] + sorted(productos['categoria'].unique().tolist())
        categoria_filtro = st.selectbox("**Categoría**", categorias)
    
    with col_f2:
        precio_max = int(productos['precio'].max())
        precio_max_filtro = st.slider("**Precio máximo**", 0, precio_max, precio_max, format="$%d")
    
    with col_f3:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔄 Reiniciar Filtros", use_container_width=True):
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # --- Grid de Productos ---
    st.markdown("### 🎯 Productos Destacados")
    
    # Aplicar filtros
    productos_filtrados = productos.copy()
    if categoria_filtro != "Todas":
        productos_filtrados = productos_filtrados[productos_filtrados['categoria'] == categoria_filtro]
    
    productos_filtrados = productos_filtrados[productos_filtrados['precio'] <= precio_max_filtro]
    
    # Mostrar cantidad de productos
    st.markdown(f"**{len(productos_filtrados)} productos encontrados**")
    
    # Grid de productos 3 columnas
    if len(productos_filtrados) > 0:
        cols = st.columns(3)
        for idx, (_, producto) in enumerate(productos_filtrados.iterrows()):
            with cols[idx % 3]:
                
                
                # Contenedor de imagen SIN ENCABEZADOS
                st.markdown(f'''
                <div class="product-image-container">
                    <img src="{producto["imagen"]}" class="product-image" alt="{producto['nombre_producto']}">
                </div>
                ''', unsafe_allow_html=True)
                
                # Información del producto
                st.markdown(f'<div class="category-badge">{producto["categoria"]}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="product-title">{producto["nombre_producto"]}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="price-tag">${producto["precio"]}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="product-description">{producto["descripcion"]}</div>', unsafe_allow_html=True)
                
                # Botones de acción
                col_btn1, col_btn2 = st.columns(2)
                with col_btn1:
                    if st.button("🛒 Carrito", key=f"cart_{producto['id']}"):
                        st.success(f"✅ {producto['nombre_producto']} agregado al carrito!")
                with col_btn2:
                    if st.button("💖 Favorito", key=f"fav_{producto['id']}"):
                        st.info(f"⭐ {producto['nombre_producto']} agregado a favoritos!")
                
                st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("No se encontraron productos con los filtros seleccionados.")

with col_chatbot:
    # --- Chatbot Asistente ---
    st.markdown('<div class="chat-header">', unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center;'>
        <div style='font-size: 2.5rem; margin-bottom: 0.5rem;'>🤖</div>
        <h3 style='margin: 0; color: white;'>Asistente Virtual</h3>
        <p style='margin: 0; opacity: 0.9; font-size: 0.9rem;'>¡Hola! ¿En qué puedo ayudarte?</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Contenedor del chat
    st.markdown('<div class="chat-container" id="chatContainer">', unsafe_allow_html=True)
    
    # Inicializar historial del chat
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = [
            {"role": "bot", "message": "¡Hola! 👋 Soy tu asistente de StyleShop."},
            {"role": "bot", "message": "Puedo ayudarte a encontrar productos perfectos para ti."},
            {"role": "bot", "message": "**Ejemplos:**"},
            {"role": "bot", "message": "• 'Zapatillas deportivas hasta $150'"},
            {"role": "bot", "message": "• 'Teléfonos smartphones'"},
            {"role": "bot", "message": "• 'Ropa casual'"}
        ]
    
    # Mostrar historial del chat
    for chat in st.session_state.chat_history:
        if chat["role"] == "user":
            st.markdown(f'<div class="user-message">{chat["message"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-message">{chat["message"]}</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Entrada de mensaje
    user_input = st.text_input(
        "Escribe tu consulta...", 
        key="chat_input",
        placeholder="Ej: Necesito un smartphone hasta $500..."
    )
    
    # Botones del chat
    col_c1, col_c2 = st.columns(2)
    
    with col_c1:
        if st.button("📤 Enviar", use_container_width=True) and user_input:
            # Agregar mensaje del usuario
            st.session_state.chat_history.append({"role": "user", "message": user_input})
            
            # Procesar consulta
            consulta = user_input.lower()
            categoria_detectada = None
            precio_max_detectado = None
            
            # Detectar categoría
            categorias_map = {
                'electronica': 'Electrónica', 'electronicos': 'Electrónica', 'tecnologia': 'Electrónica',
                'telefono': 'Electrónica', 'smartphone': 'Electrónica', 'iphone': 'Electrónica',
                'audifonos': 'Electrónica', 'laptop': 'Electrónica', 'tablet': 'Electrónica',
                'ropa': 'Ropa', 'camisa': 'Ropa', 'pantalon': 'Ropa', 'jeans': 'Ropa',
                'calzado': 'Calzado', 'zapatilla': 'Calzado', 'zapato': 'Calzado', 'tenis': 'Calzado'
            }
            
            for keyword, categoria in categorias_map.items():
                if keyword in consulta:
                    categoria_detectada = categoria
                    break
            
            # Detectar precio
            palabras = consulta.split()
            for i, palabra in enumerate(palabras):
                if palabra in ['$', 'precio', 'hasta', 'maximo', 'máximo', 'menos'] and i + 1 < len(palabras):
                    try:
                        precio_str = palabras[i + 1].replace('$', '').replace(',', '')
                        precio_max_detectado = float(precio_str)
                        break
                    except:
                        continue
            
            # Buscar recomendaciones
            recomendaciones = recomendar_productos(productos, categoria_detectada, precio_max_detectado)
            
            # Respuesta del bot
            if categoria_detectada or precio_max_detectado:
                if categoria_detectada and precio_max_detectado:
                    respuesta = f"Encontré estos productos de **{categoria_detectada}** hasta **${precio_max_detectado}**:"
                elif categoria_detectada:
                    respuesta = f"Encontré estos productos de **{categoria_detectada}**:"
                else:
                    respuesta = f"Encontré estos productos hasta **${precio_max_detectado}**:"
                
                st.session_state.chat_history.append({"role": "bot", "message": respuesta})
                
                for prod in recomendaciones:
                    prod_info = f"• **{prod['nombre_producto']}** - ${prod['precio']}"
                    st.session_state.chat_history.append({"role": "bot", "message": prod_info})
                
                st.session_state.chat_history.append({"role": "bot", "message": "¿Te interesa alguno de estos productos?"})
            else:
                st.session_state.chat_history.append({
                    "role": "bot", 
                    "message": "Puedo ayudarte a encontrar productos específicos. Por ejemplo: 'zapatillas hasta $100' o 'teléfonos smartphones'"
                })
            
            st.rerun()
    
    with col_c2:
        if st.button("🗑️ Limpiar", use_container_width=True):
            st.session_state.chat_history = [
                {"role": "bot", "message": "¡Conversación reiniciada! ¿En qué puedo ayudarte hoy?"}
            ]
            st.rerun()

# --- Footer ---
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #2c3e50; padding: 2rem;'>
    <h4 style='color: #2c3e50;'>StyleShop - Tu experiencia de compra premium</h4>
    <p style='color: #2c3e50;'>🚚 Envío gratis en compras mayores a $100 | 🔒 Pago 100% seguro | 📞 Soporte 24/7</p>
    <div style='margin-top: 1rem;'>
        <small style='color: #2c3e50;'>© 2024 StyleShop. Todos los derechos reservados.</small>
    </div>
</div>
""", unsafe_allow_html=True)
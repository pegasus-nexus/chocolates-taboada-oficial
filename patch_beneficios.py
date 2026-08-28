import re

with open('src/pages/beneficios.astro', 'r', encoding='utf-8') as f:
    content = f.read()

replacement = """const apiUrl = import.meta.env.PUBLIC_API_URL || "https://sales-system-production-f30c.up.railway.app/api/v1";
let rewards = [];
try {
    const res = await fetch(`${apiUrl}/fidelizacion/catalog`);
    const data = await res.json();
    if (data && data.web_config && data.web_config.rewards) {
        rewards = data.web_config.rewards.filter(r => r.is_active);
    }
} catch (e) {
    console.error("Error fetching rewards:", e);
}

if (rewards.length === 0) {
    rewards = [
        { id:'trufa', title:'Chocolate Amargo', tag:'Regalo VIP', desc:'Pieza maestra de cacao belga.', img:'/img/chocolate_amargo_beneficio.webp', validity: '2 Semanas' },
        { id:'choco', title:'Trufas de Chocolate', tag:'Exclusivo', desc:'70% cacao amazónico.', img:'/img/trufas_beneficio.webp', validity: '2 Semanas' },
        { id:'cupon2', title:'Gesto 2%', tag:'Cortesía', desc:'Descuento especial de bienvenida.', img:'/img/descuento_porcentaje.webp', validity: 'Un mes' },
        { id:'choco3', title:'Gesto 3%', tag:'Exclusivo', desc:'70% cacao amazónico en tu compra.', img:'/img/descuento_porcentaje.webp', validity: '2 Semanas' },
        { id:'cupon4', title:'Gesto 4%', tag:'Cortesía', desc:'Descuento especial por compras.', img:'/img/descuento_porcentaje.webp', validity: '1 Semana' },
    ];
}"""

# Use regex to find and replace the hardcoded rewards array
pattern = re.compile(r"const rewards = \[\s*\{.*?\},\s*\];", re.DOTALL)
content = pattern.sub(replacement, content)

with open('src/pages/beneficios.astro', 'w', encoding='utf-8') as f:
    f.write(content)

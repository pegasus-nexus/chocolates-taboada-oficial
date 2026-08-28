import os

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    orig = content
    # The user specifically highlighted these exact corruptions
    reps = {
        'Â¡Hola': '¡Hola',
        'LÃmite': 'Límite',
        'L\ufffdmite': 'Límite',
        'VÃ¡lido': 'Válido',
        'V\ufffdlido': 'Válido',
        'mÃ¡s': 'más',
        'm\ufffds': 'más',
        'amazÃƒÂ³nico': 'amazónico',
        'amazÃ³nico': 'amazónico',
        'amaz\ufffdnico': 'amazónico',
        'ÃƒÂ°Ã…Â¸Ã¢â‚¬Å“Ã‚Â': '📍',
        'Ã°Å¸â€œÂ ': '📍',
        'CortesÃa': 'Cortesía',
        'Cortes\ufffda': 'Cortesía',
        'Â·': '·',
        '\ufffd': '·'  # Wait, replacing all \ufffd with dot might break things. I'll be careful.
    }
    
    for bad, good in reps.items():
        if bad != '\ufffd':
            content = content.replace(bad, good)
            
    # Fix some common \ufffd cases based on typical words
    content = content.replace('im\ufffdgenes', 'imágenes')
    content = content.replace('Cortes\ufffda', 'Cortesía')
    content = content.replace('amaz\ufffdnico', 'amazónico')
    content = content.replace('m\ufffds', 'más')
    content = content.replace('L\ufffdmite', 'Límite')
    content = content.replace('V\ufffdlido', 'Válido')
    content = content.replace('pesta\ufffda', 'pestaña')
    content = content.replace('Comunidad Taboada \ufffd Beneficios Exclusivos', 'Comunidad Taboada · Beneficios Exclusivos')
    content = content.replace('📍 \ufffd SOLO V', '📍 SOLO V')
    content = content.replace('\ufffd SOLO V', '📍 SOLO V')

    if content != orig:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filepath}")

for root, _, files in os.walk('src'):
    for file in files:
        if file.endswith(('.astro', '.tsx', '.ts')):
            fix_file(os.path.join(root, file))

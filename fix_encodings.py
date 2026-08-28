import os

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Specific targeted replacements for mangled text
    replacements = {
        'Â¡': '¡',
        'LÃmite': 'Límite',
        'VÃ¡lido': 'Válido',
        'mÃ¡s': 'más',
        'amazÃƒÂ³nico': 'amazónico',
        'amazÃ³nico': 'amazónico',
        'ÃƒÂ°Ã…Â¸Ã¢â‚¬Å“Ã‚Â': '📍',
        'Ã°Å¸â€œÂ ': '📍',
        'Â·': '·',
        'imÃ¡genes': 'imágenes',
        'CortesÃa': 'Cortesía',
        'pestaÃ±a': 'pestaña',
        'MÃ¡s': 'Más',
        'CÃ³digo': 'Código',
        'Ãº': 'ú',
        'Ã³': 'ó',
        'Ã­': 'í',
        'Ã¡': 'á',
        'Ã©': 'é',
        'Ã±': 'ñ',
        'Ãš': 'Ú',
        'Ã“': 'Ó',
        'Ã\x8d': 'Í',
        'Ã\x81': 'Á',
        'Ã‰': 'É',
        'Ã‘': 'Ñ'
    }

    for bad, good in replacements.items():
        content = content.replace(bad, good)
        
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print(f"Fixed {filepath}")

def main():
    folder = 'c:/Users/rodri/Desktop/chocolates-taboada-oficial/src'
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(('.astro', '.tsx', '.ts', '.jsx', '.js', '.html')):
                fix_file(os.path.join(root, file))

if __name__ == '__main__':
    main()

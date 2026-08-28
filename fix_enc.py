import sys

def fix_encoding():
    file_path = 'src/pages/beneficios.astro'
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='latin-1') as f:
            content = f.read()

    # Fix the corrupted characters
    replacements = {
        'Â¡': '¡',
        'CÃ³DIGO': 'CÓDIGO',
        'VÃ¡lido': 'Válido',
        'mÃ¡s': 'más',
        'Cortesia': 'Cortesía',
        'VÃ LIDO': 'VÁLIDO',
        'pestaÃ±a': 'pestaña'
    }
    
    for corrupted, correct in replacements.items():
        content = content.replace(corrupted, correct)

    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        f.write(content)
    
    print('Encoding fixed')

if __name__ == '__main__':
    fix_encoding()

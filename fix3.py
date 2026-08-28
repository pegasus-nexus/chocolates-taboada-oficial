import os

def fix_bytes(filepath):
    with open(filepath, 'rb') as f:
        b = f.read()
    
    orig = b
    
    # Specific targeted replacements for mangled bytes
    reps = {
        b'\xef\xbf\xbdHola': b'\xc2\xa1Hola',
        b'L\xef\xbf\xbdmite': b'L\xc3\xadmite',
        b'm\xef\xbf\xbds': b'm\xc3\xa1s',
        b'V\xef\xbf\xbdlido': b'V\xc3\xa1lido',
        b'\xef\xbf\xbd SOLO V': b'\xf0\x9f\x93\x8d SOLO V',
        b'Comunidad Taboada \xef\xbf\xbd Beneficios Exclusivos': b'Comunidad Taboada \xc2\xb7 Beneficios Exclusivos',
        b'im\xef\xbf\xbdgenes': b'im\xc3\xa1genes',
        b'Cortes\xef\xbf\xbda': b'Cortes\xc3\xada',
        b'amaz\xef\xbf\xbdnico': b'amaz\xc3\xb3nico',
        b'pesta\xef\xbf\xbdna': b'pesta\xc3\xb1a',
        b'pesta\xef\xbf\xbda': b'pesta\xc3\xb1a'
    }

    for bad, good in reps.items():
        b = b.replace(bad, good)
        
    if b != orig:
        with open(filepath, 'wb') as f:
            f.write(b)
        print(f"Fixed {filepath}")

for root, _, files in os.walk('src'):
    for file in files:
        if file.endswith(('.astro', '.tsx', '.ts')):
            fix_bytes(os.path.join(root, file))

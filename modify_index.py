import re
import sys

def modify_index_astro(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add import Products from "../components/Products.astro";
    if 'import Products from' not in content:
        content = content.replace('import Footer from "../components/Footer.astro";', 'import Footer from "../components/Footer.astro";\nimport Products from "../components/Products.astro";')

    # 2. Remove const categories = [...] and const products = [...]
    content = re.sub(r'const categories = \[.*?\];\s*const products = \[.*?\];', '', content, flags=re.DOTALL)

    # 3. Replace the <section id="cajas-especiales">...</section> with <Products />
    section_pattern = r'<section\s+id="cajas-especiales".*?</section>'
    content = re.sub(section_pattern, '<Products />', content, flags=re.DOTALL)
    
    # 4. Remove the script block related to categories and products that was in index.astro
    # The script block we want to remove starts with "const cards = document.querySelectorAll('.product-card');" or similar.
    # Actually, we can just let it be if it doesn't hurt, but it's better to remove it.
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Done")

if __name__ == '__main__':
    modify_index_astro(sys.argv[1])

import re
import sys

def cleanup_index_script(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update updateCity to dispatch cityChanged event
    # Find updateCity function
    if 'document.dispatchEvent(new CustomEvent(\'cityChanged\', { detail: { city } }));' not in content:
        content = content.replace("localStorage.setItem('selected_city', city);", 
            "localStorage.setItem('selected_city', city);\n        window.dispatchEvent(new CustomEvent('cityChanged', { detail: { city } }));")

    # 2. Remove filterProducts calls in updateCity
    content = content.replace("filterProducts();", "// filterProducts();")
    
    # 3. Remove the const cards, seeMoreBtn, etc. that were removed
    # Just comment out the lines that might cause errors if they don't exist
    content = content.replace("const cards = document.querySelectorAll('.product-card');", "// const cards = document.querySelectorAll('.product-card');")
    content = content.replace("const catButtons = document.querySelectorAll('.cat-btn');", "// const catButtons = document.querySelectorAll('.cat-btn');")
    content = content.replace("const seeMoreBtn = document.getElementById('see-more-btn');", "// const seeMoreBtn = document.getElementById('see-more-btn');")
    content = content.replace("const seeMoreContainer = document.getElementById('see-more-container');", "// const seeMoreContainer = document.getElementById('see-more-container');")
    content = content.replace("const noProductsMsg = document.getElementById('no-products-msg');", "// const noProductsMsg = document.getElementById('no-products-msg');")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Done")

if __name__ == '__main__':
    cleanup_index_script(sys.argv[1])

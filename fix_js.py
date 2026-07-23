import sys

def fix_index(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Just declare seeMoreBtn and cards as empty/null at the top to avoid ReferenceErrors
    content = content.replace("// const cards = document.querySelectorAll('.product-card');", "const cards = [];")
    content = content.replace("// const catButtons = document.querySelectorAll('.cat-btn');", "const catButtons = [];")
    content = content.replace("// const seeMoreBtn = document.getElementById('see-more-btn');", "const seeMoreBtn = null;")
    content = content.replace("// const seeMoreContainer = document.getElementById('see-more-container');", "const seeMoreContainer = null;")
    content = content.replace("// const noProductsMsg = document.getElementById('no-products-msg');", "const noProductsMsg = null;")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Fixed JS references")

if __name__ == '__main__':
    fix_index(sys.argv[1])

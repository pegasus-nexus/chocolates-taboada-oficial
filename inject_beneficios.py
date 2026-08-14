import re

with open(r'c:\Users\rodri\Desktop\chocolates-taboada-oficial\src\pages\beneficios.astro', 'r', encoding='utf-8') as f:
    content = f.read()

with open(r'c:\Users\rodri\Desktop\chocolates-taboada-oficial\script_beneficios.txt', 'r', encoding='utf-8') as f:
    newScript = f.read()

# Replace ticket-container block
replacement_container = '''<section class="welcome-section" style="margin-top: 40px; margin-bottom: 20px;">
      <h2 style="font-family: var(--font-serif); font-size: 3.5rem; color: #FAF5F0; margin-bottom: 10px; font-weight: 700; letter-spacing: -0.02em;">Beneficios</h2>
      <div class="ticket-container" id="ticket-container">
        <!-- Injected dynamically from fetchBenefit script -->
      </div>
    </section>'''

content = re.sub(r'<div class="ticket-container".*?</section>', replacement_container, content, flags=re.DOTALL)

# Inject the script at the end of the file before </body> or at the end
content += '\n' + newScript + '\n'

with open(r'c:\Users\rodri\Desktop\chocolates-taboada-oficial\src\pages\beneficios.astro', 'w', encoding='utf-8') as f:
    f.write(content)

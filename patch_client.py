import re

with open('src/pages/beneficios.astro', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

script_injection = """
<script>
  document.addEventListener("DOMContentLoaded", async () => {
    try {
      const apiUrl = "http://localhost:8000/api/v1";
      const res = await fetch(`${apiUrl}/fidelizacion/catalog`);
      if (res.ok) {
        const data = await res.json();
        if (data.web_config && data.web_config.rewards) {
          const dynamicRewards = data.web_config.rewards.filter(r => r.is_active);
          if (dynamicRewards.length > 0) {
            // Replace the HTML of the rewards container dynamically
            const container = document.querySelector('.rewards-grid');
            if (container) {
              container.innerHTML = '';
              dynamicRewards.forEach((product) => {
                const html = `
                  <div class="ticket-wrapper" id="ticket-${product.id}">
                    <div class="ticket">
                      <div class="ticket-main">
                        <div class="ticket-img">
                          <img src="${product.img}" alt="${product.title}" width="75" height="75" style="object-fit: contain; width: 100%; height: 100%; filter: drop-shadow(0 6px 12px rgba(0,0,0,0.15)); border-radius: 12px;" />
                        </div>
                        <div class="ticket-info">
                          <span class="ticket-tag" style="display:inline-block; margin-bottom:10px; font-size:0.7rem; font-weight:800; letter-spacing:0.12em; text-transform:uppercase; color:#8f6c49; border-bottom: 2px solid #8f6c49; padding-bottom:3px;">${product.tag}</span>
                          <h3 style="font-family: var(--font-serif); font-size: 2.4rem; font-weight: 700; color: #2A1612; margin: 0 0 10px; line-height: 1;">${product.title}</h3>
                          <p style="font-size: 1rem; color: #42200D; margin: 0; font-weight: 500;">${product.desc}</p>
                        </div>
                      </div>
                      <div class="ticket-divider">
                        <div class="hole hole-start" style="width:24px; height:24px; background-color:var(--cafe-profundo); border-radius:50%; position:absolute; left:-12px; top:-12px;"></div>
                        <div class="dash-line" style="border-left: 3px dashed rgba(42,22,18,0.15); height:100%;"></div>
                        <div class="hole hole-end" style="width:24px; height:24px; background-color:var(--cafe-profundo); border-radius:50%; position:absolute; left:-12px; bottom:-12px;"></div>
                      </div>
                      <div class="ticket-stub" style="width:140px; background:linear-gradient(135deg, #F3ECE3 0%, #E8DFD3 100%); display:flex; flex-direction:column; align-items:center; justify-content:center; gap:20px; padding:30px 20px; border-radius: 0 24px 24px 0;">
                        <div class="stub-barcode" style="font-family:'Courier New', monospace; font-size:1.5rem; letter-spacing:4px; font-weight:bold; color:rgba(42,22,18,0.25); transform:rotate(-90deg); margin:20px 0;">|||| || |||</div>
                        <span class="stub-label" style="font-size:0.65rem; font-weight:800; color:#8f6c49; letter-spacing:0.05em; text-align:center;">${product.validity}</span>
                        <button class="btn-redeem" onclick="abrirModal('${product.id}')" style="background:#8f6c49; color:#FAF5F0; border:none; padding:10px 18px; border-radius:12px; font-weight:800; font-size:0.85rem; letter-spacing:0.08em; cursor:pointer; transition:all 0.3s ease; box-shadow:0 8px 15px rgba(143,108,73,0.3); width:100%;">CANJEAR</button>
                      </div>
                    </div>
                  </div>
                `;
                container.innerHTML += html;
              });
            }
          }
        }
      }
    } catch (e) {
      console.error(e);
    }
  });
</script>
"""

content = content.replace("</AppLayout>", script_injection + "\n</AppLayout>")

with open('src/pages/beneficios.astro', 'w', encoding='utf-8') as f:
    f.write(content)

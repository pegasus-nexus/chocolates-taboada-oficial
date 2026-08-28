const fs = require('fs');
let content = fs.readFileSync('src/pages/beneficios.astro', 'utf8');

// Fix encoding issues
content = content.replace(/CÃ³digo/g, 'Código');
content = content.replace(/CortesÃ­a/g, 'Cortesía');
content = content.replace(/podrÃ¡s/g, 'podrás');
content = content.replace(/Ã°Å¸â€œÂ /g, '📍');
content = content.replace(/VÃ LIDO/g, 'VÁLIDO');
content = content.replace(/AnimaciÃ³n/g, 'Animación');
content = content.replace(/subtÃ­tulo/g, 'subtítulo');
content = content.replace(/Ã­conos/g, 'íconos');
content = content.replace(/LÃ­mite/g, 'Límite');
content = content.replace(/VÃ¡lido/g, 'Válido');
content = content.replace(/mÃ¡s/g, 'más');
content = content.replace(/demÃ¡s/g, 'demás');
content = content.replace(/Â¡Hola/g, '¡Hola');
content = content.replace(/â€¢/g, '•');
content = content.replace(/CÃ³DIGO/g, 'CÓDIGO');

const newBanner = \
      <div id="member-code-banner" style="display: none; margin-bottom: 30px; margin-top: 10px; width: 340px; height: 215px; background: linear-gradient(135deg, #2A1612 0%, #1a0e0c 100%); border-radius: 16px; padding: 24px; position: relative; box-shadow: 0 20px 40px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.1); border: 1px solid rgba(220,176,65,0.3); overflow: hidden; flex-direction: column; justify-content: space-between;">
        <!-- Shine effect -->
        <div style="position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: linear-gradient(to bottom right, rgba(255,255,255,0) 0%, rgba(255,255,255,0.05) 40%, rgba(255,255,255,0) 50%); transform: rotate(30deg); pointer-events: none;"></div>
        
        <!-- Top row: Logo and Chip -->
        <div style="display: flex; justify-content: space-between; align-items: flex-start; position: relative; z-index: 1;">
          <div style="font-family: var(--font-serif); font-size: 1.2rem; font-weight: bold; color: #dcb041; letter-spacing: 0.05em; font-style: italic;">Taboada Black</div>
          <!-- EMV Chip -->
          <div style="width: 42px; height: 32px; background: linear-gradient(135deg, #ffd700 0%, #daa520 100%); border-radius: 6px; position: relative; overflow: hidden; box-shadow: inset 0 0 4px rgba(0,0,0,0.3);">
             <div style="position: absolute; top: 50%; left: 0; right: 0; height: 1px; background: rgba(0,0,0,0.2);"></div>
             <div style="position: absolute; left: 50%; top: 0; bottom: 0; width: 1px; background: rgba(0,0,0,0.2);"></div>
             <div style="position: absolute; top: 25%; left: 25%; right: 25%; bottom: 25%; border: 1px solid rgba(0,0,0,0.2); border-radius: 3px;"></div>
          </div>
        </div>

        <!-- Middle row: Member Code -->
        <div style="position: relative; z-index: 1; margin-top: auto; margin-bottom: 20px;">
          <span style="color: rgba(255,255,255,0.5); font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.15em; display: block; margin-bottom: 6px;">MEMBER ID / CÓDIGO</span>
          <span id="member-code-value" style="font-family: 'Courier New', monospace; font-size: 1.65rem; color: #f6d98d; font-weight: bold; letter-spacing: 0.18em; text-shadow: 0 2px 4px rgba(0,0,0,0.5);"></span>
        </div>

        <!-- Bottom row: Name & VIP -->
        <div style="display: flex; justify-content: space-between; align-items: flex-end; position: relative; z-index: 1;">
          <div style="text-transform: uppercase; color: white; font-size: 0.85rem; font-weight: 600; letter-spacing: 0.1em;" id="member-card-name">MIEMBRO EXCLUSIVO</div>
          <div style="display: flex; align-items: center; gap: 4px;">
            <svg class="w-5 h-5 text-[#dcb041]" fill="currentColor" viewBox="0 0 24 24" style="width:20px;height:20px;"><path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z"></path></svg>
            <span style="color: #dcb041; font-size: 0.8rem; font-weight: 800; font-style: italic; letter-spacing: 0.05em;">VIP</span>
          </div>
        </div>
      </div>
\;

content = content.replace(/<div id="member-code-banner".*?<\/div>/s, newBanner);
fs.writeFileSync('src/pages/beneficios.astro', content);
console.log('Fixed completely');

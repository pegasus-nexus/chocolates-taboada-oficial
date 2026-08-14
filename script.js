    document.addEventListener("DOMContentLoaded", () => {
      const fetchWebConfig = async () => {
        try {
          const apiUrl = import.meta.env.PUBLIC_API_URL || "http://localhost:10000/api/v1";
          const response = await fetch(\\/fidelizacion/catalog\);
          if (response.ok) {
            const data = await response.json();
            if (data.status === "success" && data.web_config) {
              const wc = data.web_config;
              const subEl = document.getElementById("hero-subtitle");
              const titleEl = document.getElementById("hero-title");
              const descEl = document.getElementById("hero-description");
              
              if (wc.hero_subtitle && subEl && subEl.textContent !== wc.hero_subtitle)
                subEl.textContent = wc.hero_subtitle;
              if (wc.hero_title && titleEl && titleEl.textContent !== wc.hero_title)
                titleEl.textContent = wc.hero_title;
              if (wc.hero_description && descEl && descEl.textContent !== wc.hero_description)
                descEl.textContent = wc.hero_description;

              const bgElement = document.getElementById("hero-bg-cover");
              if (bgElement) {
                const currentCity = localStorage.getItem("taboada_selected_city") || "cochabamba";
                window.dispatchEvent(
                  new CustomEvent("cityChanged", {
                    detail: { city: currentCity },
                  }),
                );
              }

              // Render featured products
              if (wc.featured_products && wc.featured_products.length > 0 && data.productos) {
                const destacadosContainer = document.getElementById("destacados-container");
                if (destacadosContainer) {
                  let html = '';
                  wc.featured_products.forEach((id, index) => {
                    const product = data.productos.find(p => p.id === id);
                    if (product) {
                      const isReverse = index % 2 !== 0;
                      const currentCity = localStorage.getItem('taboada_selected_city') || 'cochabamba';
                      const currentPrice = product.precios && product.precios[currentCity] ? product.precios[currentCity] : 0;
                      
                      html += \
                      <div class="product-card bg-[#18090d]/35 backdrop-blur-md border border-white/10 rounded-[2rem] p-6 md:p-8 flex flex-col \ items-center gap-8 shadow-2xl transition-all duration-500 group cursor-pointer" style="-webkit-backdrop-filter: blur(12px);" data-id="\" data-name="\" data-size="Unidad" data-img="\" data-desc="\" data-price-cochabamba="\" data-price-lapaz="\">
                        <div class="md:w-[42%] flex items-center justify-center relative overflow-hidden">
                          <img src="\" alt="\" class="object-contain w-full h-full max-h-56 relative z-10 drop-shadow-[0_15px_25px_rgba(0,0,0,0.6)] group-hover:scale-105 transition-transform duration-500" />
                        </div>
                        <div class="md:w-[58%] flex flex-col justify-center text-left \">
                          <h3 class="text-4xl md:text-5xl font-serif font-bold text-white mb-2 drop-shadow-sm">Bs. \</h3>
                          <h4 class="text-xl md:text-2xl font-bold text-[#dcb041] mb-1 font-serif tracking-wide">\</h4>
                          <p class="text-white/80 text-sm leading-relaxed mb-6 font-sans">Destacado exclusivo de la temporada.</p>
                          <div class="flex flex-wrap items-center gap-3 mt-auto">
                            <span class="bg-black/40 border border-white/15 text-white/80 text-xs font-semibold px-4 py-2 rounded-full font-sans tracking-wide">Destacado</span>
                            <button type="button" class="add-to-cart-btn bg-[#dcb041] hover:bg-white text-[#1C0C12] text-xs font-extrabold px-5 py-2.5 rounded-full transition-all duration-300 shadow-lg hover:scale-105 cursor-pointer flex items-center gap-2" data-id="\" data-name="\" data-size="Unidad" data-img="\" data-desc="\" data-price-cochabamba="\" data-price-lapaz="\">
                              <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15.75 10.5V6a3.75 3.75 0 10-7.5 0v4.5m11.356-1.993l1.263 12c.07.665-.45 1.243-1.119 1.243H4.25a1.125 1.125 0 01-1.12-1.243l1.264-12A1.125 1.125 0 015.513 7.5h12.974c.576 0 1.059.435 1.119 1.007zM8.625 10.5a.375.375 0 11-.75 0 .375.375 0 01.75 0zm7.5 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z"></path></svg>
                              <span>Añadir al Carrito</span>
                            </button>
                            <button type="button" class="direct-buy-btn bg-black/50 hover:bg-black/70 border border-white/20 text-white text-xs font-bold px-5 py-2.5 rounded-full transition-all duration-300 shadow-md hover:scale-105 text-center cursor-pointer flex items-center gap-2" data-name="\" data-size="Unidad" data-price-cochabamba="\" data-price-lapaz="\">
                              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"></path></svg>
                              <span>Comprar <span class="text-sm">?</span></span>
                            </button>
                          </div>
                        </div>
                      </div>
                      \;
                    }
                  });
                  if (html) {
                    destacadosContainer.innerHTML = html;
                    
                    // Reattach event listeners to new buttons!
                    // Assuming there's a global function or we just wait for the main script to re-bind them
                    // Since it's Astro, there is a global initCart() maybe? 
                    // Let's trigger a custom event
                    window.dispatchEvent(new CustomEvent('cartButtonsUpdated'));
                  }
                }
              }
            }
          }
        } catch (err) {}
      };

      if ("requestIdleCallback" in window) {
        requestIdleCallback(fetchWebConfig, { timeout: 1500 });
      } else {
        setTimeout(fetchWebConfig, 100);
      }
    });

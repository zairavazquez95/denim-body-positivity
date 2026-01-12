import pandas as pd
import matplotlib.pyplot as plt
import time
from scipy.stats import pearsonr
from pytrends.request import TrendReq


pytrends = TrendReq(hl='es-MX', tz=360, retries=5, backoff_factor=0.5)

keywords = [
    "baggy jeans", 
    "skinny jeans", 
    "low rise jeans",
    "body positivity", 
    "ozempic",
    "pilates aesthetic", 
    "calorie deficit"
]

def fetch_all_signals(kw_list):
    all_series = []
    print("🚀 Iniciando descarga de señales (Paciencia: hay pausas de seguridad)...")
    
    for kw in kw_list:
        success = False
        attempts = 0
        while not success and attempts < 2:
            try:
                print(f"📥 Obteniendo data de: {kw}...")
                pytrends.build_payload([kw], timeframe="2019-01-01 2025-12-31", geo="US")
                df = pytrends.interest_over_time()
                
                if not df.empty:
                    all_series.append(df[kw])
                    success = True
                    time.sleep(10) 
                else:
                    print(f"⚠️ No hay datos suficientes para: {kw}")
                    success = True # Saltamos a la siguiente
            except Exception as e:
                attempts += 1
                print(f"❌ Error/Bloqueo en '{kw}': {e}")
                print("⏳ Esperando 60 segundos para 'enfriar' la IP...")
                time.sleep(60)
                
    if not all_series:
        return pd.DataFrame()
    return pd.concat(all_series, axis=1)

df_raw = fetch_all_signals(keywords)

if not df_raw.empty:

    df_smooth = df_raw.rolling(window=12).mean().dropna()
    norm = (df_smooth - df_smooth.min()) / (df_smooth.max() - df_smooth.min()) * 100

    corr_matrix = norm.corr()
    
    print("\n" + "="*60)
    print("      REPORT STRATEGY: INTERPRETACIÓN DE SEÑALES")
    print("="*60)

    def interpretar(r):
        if r > 0.7: return "CORRELACIÓN FUERTE POSITIVA (Tendencias hermanas)"
        if r > 0.3: return "CORRELACIÓN MODERADA"
        if r < -0.7: return "CORRELACIÓN INVERSA FUERTE (Efecto reemplazo)"
        if r < -0.3: return "CORRELACIÓN INVERSA MODERADA"
        return "SIN CORRELACIÓN CLARA"

    tesis = [
        ("skinny jeans", "ozempic", "Skinny Jeans vs. Ozempic"),
        ("ozempic", "body positivity", "Ozempic vs. Body Positivity"),
        ("baggy jeans", "body positivity", "Baggy Jeans vs. Body Positivity"),
        ("low rise jeans", "pilates aesthetic", "Low Rise vs. Pilates Aesthetic")
    ]

    for k1, k2, titulo in tesis:
        if k1 in norm.columns and k2 in norm.columns:
            r = corr_matrix.loc[k1, k2]
            print(f"▶ {titulo}:")
            print(f"   {interpretar(r)} | Coeficiente r = {r:.2f}\n")

    plt.style.use('bmh')
    fig, ax = plt.subplots(figsize=(15, 9), facecolor='#FDFCF9')
    ax.set_facecolor('#FDFCF9')

    colores = {
        'baggy jeans': '#2C3E50', 'skinny jeans': '#7F8C8D', 
        'low rise jeans': '#F1C40F', 'body positivity': '#E74C3C', 
        'ozempic': '#16A085', 'pilates aesthetic': '#8E44AD', 
        'calorie deficit': '#D35400'
    }

    for col in norm.columns:
        es_principal = col in ['ozempic', 'body positivity']
        ax.plot(norm[col], 
                label=col.upper(), 
                color=colores.get(col, '#000000'), 
                linewidth=4 if es_principal else 2,
                alpha=1.0 if es_principal else 0.5,
                linestyle='-' if es_principal else '--')

    ax.set_title("STYLE SIGNALS: cuerpo y moda (2019-2026)", 
                 fontsize=20, fontweight='bold', pad=30, color='#2C3E50', font='Playfair Display')
    ax.set_ylabel("Interés Relativo Normalizado (0-100)", fontsize=12)
    ax.legend(loc='upper left', frameon=False, ncol=2)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.show()

    plt.savefig("fashion_trends_chart.png", dpi=300)
    print("Chart saved as fashion_trends_chart.png")
    plt.show()

    norm.to_csv('style_signals_final_report.csv')
    print("Proceso terminado. Gráfica generada y datos guardados en CSV.")
    

else:
    print("No se pudo generar el reporte. Verifica tu conexión o intenta con menos keywords.")
 

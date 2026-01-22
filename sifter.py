import os
import random
from datetime import datetime
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# DISCIPLINED PRODUCT LIST (No Test Items)
PRODUCTS = [
    ["Herman Miller Aeron Chair", "h_mD_3iYvC8", "https://amzn.to/3sn62xX"],
    ["Apple Studio Display", "MvT03E_8i7k", "https://amzn.to/4pVZPVx"],
    ["Samsung Odyssey Neo G9 Monitor", "m31u_mshmEU", "https://amzn.to/45SDcKi"],
    ["Logitech MX Creative Console", "p500P8-5XNo", "https://amzn.to/4b7Clch"],
    ["BenQ ScreenBar Halo", "m4m9WnF8_S4", "https://amzn.to/3VjLVPL"],
    ["Sony WH-1000XM5 Headphones", "UZvUH8tejj8", "https://amzn.to/4jVxwoK"],
    ["Keychron Q6 Pro Keyboard", "7C_hE0-E6_M", "https://amzn.to/43fD3N8"],
    ["Elgato Stream Deck MK.2", "jT2eiBaFYJU", "https://amzn.to/3Seekqd"]
]

def run_sifter():
    product_name, yt_id, aff_link = random.choice(PRODUCTS)
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    prompt = f"Write an elite 250-word review for the {product_name}. Focus on aesthetic and performance. No headers."
    
    try:
        response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        
        post_content = f"""---
layout: post
title: "TheSift: {product_name} Analysis"
date: {date_str}
youtube_id: "{yt_id}"
---

{response.text}

---

<div style="text-align: center; margin: 40px 0;">
    <a href="{aff_link}" class="buy-button" target="_blank" rel="noopener noreferrer">Check Current Price on Amazon</a>
</div>
"""
        clean_name = product_name.lower().replace(" ", "-")
        filename = f"_posts/{date_str}-{clean_name}.md"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(post_content)
        print(f"✅ Sifted: {product_name}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    run_sifter()

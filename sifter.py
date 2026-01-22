import os
import random
from datetime import datetime
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# DISCIPLINED PRODUCT LIST (Premium Only)
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
    
    prompt = f"Write an elite 250-word review for the {product_name}. Focus on industrial design, performance, and craftsmanship. No headers."
    
    try:
        response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        
        # Site URL for sharing logic
        base_url = "https://174hz.github.io/thesift"
        post_url = f"{base_url}/{date_str}-{product_name.lower().replace(' ', '-')}.html"
        
        post_content = f"""---
layout: post
title: "TheSift: {product_name} Analysis"
date: {date_str}
youtube_id: "{yt_id}"
---

{response.text}

---

<div style="text-align: center; margin: 50px 0; padding: 40px; border: 1px solid var(--border-color); border-radius: 4px;">
    <h4 style="text-transform: uppercase; font-size: 0.7rem; letter-spacing: 2px; margin-bottom: 20px;">Acquisition</h4>
    <a href="{aff_link}" class="buy-button" style="display: inline-block; padding: 15px 30px; background: var(--text-color); color: var(--bg-color) !important; text-decoration: none; font-weight: 800; font-size: 0.8rem; text-transform: uppercase; border-radius: 4px;" target="_blank">Check Price on Amazon</a>
    
    <div style="margin-top: 40px;">
        <h4 style="text-transform: uppercase; font-size: 0.6rem; letter-spacing: 2px; color: var(--muted-text); margin-bottom: 15px;">Instantly Share This Analysis</h4>
        <div style="display: flex; justify-content: center; gap: 20px;">
            <a href="https://twitter.com/intent/tweet?text=Analysis: {product_name}&url={post_url}" target="_blank" style="color: var(--text-color); text-decoration: none; font-size: 0.75rem; font-weight: 700;">X</a>
            <a href="https://www.facebook.com/sharer/sharer.php?u={post_url}" target="_blank" style="color: var(--text-color); text-decoration: none; font-size: 0.75rem; font-weight: 700;">Facebook</a>
            <a href="https://www.linkedin.com/sharing/share-offsite/?url={post_url}" target="_blank" style="color: var(--text-color); text-decoration: none; font-size: 0.75rem; font-weight: 700;">LinkedIn</a>
        </div>
    </div>
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

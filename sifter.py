import os
import random
from datetime import datetime
from google import genai

# 1. SETUP: Connect to the Gemini AI
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 2. THE MASTER CATALOG: Verified YouTube IDs and Direct Amazon Links
PRODUCTS = [
    ["Herman Miller Aeron Chair", "h_mD_3iYvC8", "https://amzn.to/3sn62xX"],
    ["Apple Studio Display", "MvT03E_8i7k", "https://amzn.to/4pVZPVx"],
    ["Samsung Odyssey Neo G9 Monitor", "m31u_mshmEU", "https://amzn.to/45SDcKi"],
    ["Logitech MX Creative Console", "p500P8-5XNo", "https://amzn.to/4b7Clch"],
    ["BenQ ScreenBar Halo", "m4m9WnF8_S4", "https://amzn.to/3VjLVPL"],
    ["Epson EcoTank Pro ET-5850", "DovL9lFkI0s", "https://amzn.to/4sT006G"],
    ["Logitech MX Master 3S Mouse", "twbL6619v-4", "https://amzn.to/4qXqSRc"],
    ["Sony WH-1000XM5 Headphones", "UZvUH8tejj8", "https://amzn.to/42O7I3Z"],
    ["Keychron Q6 Pro Keyboard", "7C_hE0-E6_M", "https://amzn.to/43fD3N8"],
    ["Elgato Stream Deck MK.2", "jT2eiBaFYJU", "https://amzn.to/3Seekqd"]
]

def run_sifter():
    # Selection logic
    product_name, yt_id, aff_link = random.choice(PRODUCTS)
    
    # IMPORTANT: .strip() removes hidden spaces that break Amazon links
    aff_link = aff_link.strip() 
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    # Prompt for authoritative, high-end content
    prompt = (
        f"Write a 250-word elite tech review for the {product_name}. "
        "Focus on craftsmanship, long-term value, and productivity benefits for a professional setup. "
        "Include 3-4 bullet points of high-level technical specifications. "
        "The tone should be authoritative but conversational. Do not use Markdown headers like # or ## in the body."
    )
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=prompt
        )
        
        # Build Markdown - Added target="_blank" to the anchor tag below
        post_content = f"""---
layout: post
title: "TheSift: Is the {product_name} Worth the Investment?"
date: {date_str}
youtube_id: "{yt_id}"
---

{response.text}

---

### The Sift Verdict
The **{product_name}** represents a premium standard in modern workspace tech.

<div style="text-align: center; margin: 40px 0;">
    <a href="{aff_link}" class="buy-button" target="_blank">Check Current Price on Amazon</a>
</div>

*As an Amazon Associate, I earn from qualifying purchases.*
"""

        # Sanitize filename (lowercase, no dots, no spaces)
        clean_name = product_name.lower().replace(" ", "-").replace(".", "")
        filename = f"_posts/{date_str}-{clean_name}.md"
        
        os.makedirs('_posts', exist_ok=True)
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(post_content)
            
        print(f"✅ Sifted and Verified: {product_name}")
        
    except Exception as e:
        print(f"❌ Error during sift: {e}")

if __name__ == "__main__":
    run_sifter()

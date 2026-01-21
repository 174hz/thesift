import os
import random
from datetime import datetime
from google import genai

# 1. SETUP: Connect to the Gemini AI
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 2. YOUR CATALOG: The high-ticket products you chose
# Format: ["Product Name", "YouTube ID", "Affiliate Link"]
PRODUCTS = [
    ["Herman Miller Aeron Chair", "8332532177075038213", "https://amzn.to/49zgnxI"],
    ["Apple Studio Display", "15844307808690829027", "https://amzn.to/4pVZPVx"],
    ["Samsung Odyssey Neo G9 Monitor", "3472987686007558214", "https://amzn.to/45SDcKi"],
    ["Logitech MX Creative Console", "2027506961957546871", "https://amzn.to/4b7Clch"],
    ["BenQ ScreenBar Halo", "15081320089479402942", "https://amzn.to/49SjeR7"],
    ["Epson EcoTank Pro ET-5850", "3286438268970062756", "https://amzn.to/4sT006G"],
    ["Logitech MX Master 3S Mouse", "twbL6619v-4", "https://amzn.to/4qXqSRc"],
    ["Sony WH-1000XM5 Headphones", "UZvUH8tejj8", "https://amzn.to/42O7I3Z"],
    ["TP-Link Deco XE75 Pro Mesh System", "OkBmKQcteC4", "https://amzn.to/3P1jR6h"],
    ["Elgato Stream Deck MK.2", "jT2eiBaFYJU", "https://amzn.to/3OJWqJv"]
]

def run_sifter():
    # Pick one product at random
    product_name, yt_id, aff_link = random.choice(PRODUCTS)
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    # Prompt optimized for professional, high-ticket "Sift" voice
    prompt = (
        f"Write a 250-word elite tech review for the {product_name}. "
        "Focus on craftsmanship, long-term value, and productivity benefits for a professional setup. "
        "Include 3-4 bullet points of high-level technical specifications. "
        "The tone should be authoritative but conversational."
    )
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=prompt
        )
        
        # Build Markdown with UI classes for the new style.css
        post_content = f"""---
layout: post
title: "TheSift: Is the {product_name} Worth the Investment?"
date: {date_str}
youtube_id: "{yt_id}"
---

{response.text}

---

### The Sift Verdict
The **{product_name}** represents a premium standard in modern workspace tech. If you are building a setup designed for peak performance, this is an essential addition.

<div style="text-align: center; margin: 40px 0;">
    <a href="{aff_link}" class="buy-button">Check Current Price on Amazon</a>
</div>

*As an Amazon Associate, I earn from qualifying purchases.*
"""

        clean_name = product_name.lower().replace(" ", "-")
        filename = f"_posts/{date_str}-{clean_name}.md"
        
        os.makedirs('_posts', exist_ok=True)
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(post_content)
            
        print(f"✅ Successfully sifted: {product_name}")
        
    except Exception as e:
        print(f"❌ Error during sift: {e}")

if __name__ == "__main__":
    run_sifter()

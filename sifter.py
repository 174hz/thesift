import os
import random
from datetime import datetime
from google import genai

# 1. Setup AI Client
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 2. Your "Money-Maker" Catalog
# Add more products here! Format: [Product Name, YouTube ID, Amazon Link]
PRODUCTS = [
    ["Logitech MX Master 3S", "twbL6619v-4", "https://amzn.to/3S-Master"],
    ["Logitech MX Mechanical Keyboard", "1y9mSRE6F28", "https://amzn.to/MX-Mech"],
    ["Sony WH-1000XM5 Headphones", "fuO_9p6Wl90", "https://amzn.to/Sony-XM5"],
    ["Elgato Stream Deck MK.2", "vG97C0z9L2E", "https://amzn.to/StreamDeck"],
    ["BenQ ScreenBar Halo", "tUa3oDk1m9M", "https://amzn.to/BenQ-Halo"],
    ["Everlasting Comfort Seat Cushion", "8_6q-Xf6Y_I", "https://amzn.to/EverComfort"]
]

def run_sifter():
    # Pick a random product so the site stays fresh
    product_name, yt_id, aff_link = random.choice(PRODUCTS)
    
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    prompt = f"Write a professional 150-word blog review for the {product_name}. Highlight 3 technical specs. Use a helpful, 'productivity-guru' tone."
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=prompt
        )
        
        post_content = f"""---
layout: post
title: "TheSift: Why the {product_name} is a Game Changer"
date: {date_str}
youtube_id: "{yt_id}"
---

{response.text}

---
### Featured Gear
* **Top Pick:** [{product_name}]({aff_link})

*As an Amazon Associate, I earn from qualifying purchases.*
"""
        # Save the file with the date and product name
        filename = f"_posts/{date_str}-{product_name.lower().replace(' ', '-')}.md"
        os.makedirs('_posts', exist_ok=True)
        
        with open(filename, "w") as f:
            f.write(post_content)
        print(f"Success: Posted review for {product_name}!")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_sifter()

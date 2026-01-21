import os
import random
from datetime import datetime
from google import genai

# 1. SETUP: Connect to the Gemini AI
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 2. YOUR CATALOG: The high-ticket products you chose
PRODUCTS = [
    ["Herman Miller Aeron Chair", "8332532177075038213", "https://amzn.to/49zgnxI"],
    ["Apple Studio Display", "15844307808690829027", "https://amzn.to/4pVZPVx"],
    ["Samsung Odyssey Neo G9 Monitor", "3472987686007558214", "https://amzn.to/45SDcKi"],
    ["Logitech MX Creative Console", "2027506961957546871", "https://amzn.to/4b7Clch"],
    ["BenQ ScreenBar Halo", "15081320089479402942", "https://amzn.to/49SjeR7"],
    ["Epson EcoTank Pro ET-5850", "3286438268970062756", "https://amzn.to/4sT006G"],
    ["Logitech MX Master 3S Mouse", "twbL6619v-4", "https://amzn.to/4qXqSRc"]
]

def run_sifter():
    # Pick one product at random
    product_name, yt_id, aff_link = random.choice(PRODUCTS)
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    prompt = (
        f"Write a 200-word professional tech review for the {product_name}. "
        "Focus on why it is the best choice for a high-end productivity setup. "
        "Include 3 bullet points of key specs."
    )
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=prompt
        )
        
        post_content = f"""---
layout: post
title: "TheSift: Is the {product_name} Worth the Investment?"
date: {date_str}
youtube_id: "{yt_id}"
---

{response.text}

---

### Sift Verdict
If you are looking to upgrade your setup, the **{product_name}** is a top-tier contender. 

* **Check Price on Amazon:** [{product_name}]({aff_link})

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

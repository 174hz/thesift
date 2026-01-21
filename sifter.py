import os
from google import genai

# 1. Setup with the NEW 2026 library
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def run_sifter():
    # 2. Use the most modern model name
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents="Write a 150-word blog post about the Logitech MX Master 3S mouse. Focus on ergonomics. Include 3 bullet points."
    )
    
    post_content = f"""---
layout: post
title: "TheSift: Why the MX Master 3S is a Productivity Legend"
date: 2026-01-21
youtube_id: "twbL6619v-4"
---

{response.text}

---
### Featured Gear
* **Top Pick:** [Logitech MX Master 3S](https://amzn.to/example)

*As an Amazon Associate, I earn from qualifying purchases.*
"""
    os.makedirs('_posts', exist_ok=True)
    with open("_posts/2026-01-21-ai-sift.md", "w") as f:
        f.write(post_content)
    print("Success: AI Post Created!")

if __name__ == "__main__":
    run_sifter()

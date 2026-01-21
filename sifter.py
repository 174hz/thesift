import os
import google.generativeai as genai

# Setup AI - Using a stable model version
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-pro')

def run_sifter():
    # Targeted prompt for high-value affiliate content
    prompt = "Write a 150-word blog post about the Logitech MX Master 3S mouse. Focus on ergonomics and productivity. Include 3 bullet points and a 'Why Buy' section."
    
    response = model.generate_content(prompt)
    
    post_content = f"""---
layout: post
title: "Sifted: The Ultimate Office Mouse (MX Master 3S)"
date: 2026-01-21
youtube_id: "twbL6619v-4"
---

{response.text}

---
### Featured Gear
* **Top Choice:** [Logitech MX Master 3S](https://amzn.to/3S-example)

*Disclosure: As an Amazon Associate, I earn from qualifying purchases.*
"""
    # Ensure the folder exists and save
    if not os.path.exists('_posts'):
        os.makedirs('_posts')
        
    with open("_posts/2026-01-21-ai-sift.md", "w") as f:
        f.write(post_content)
    print("AI Post Created Successfully!")

if __name__ == "__main__":
    run_sifter()

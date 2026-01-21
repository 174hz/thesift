import os
import google.generativeai as genai

# Setup AI - Using the 'latest' tag to avoid 404 errors
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash-latest')

def run_sifter():
    prompt = "Write a 150-word blog post about the Logitech MX Master 3S mouse. Focus on why it's a top-tier productivity tool. Include 3 bullet points."
    
    response = model.generate_content(prompt)
    
    post_content = f"""---
layout: post
title: "TheSift: Why the MX Master 3S Rules the Desk"
date: 2026-01-21
youtube_id: "twbL6619v-4"
---

{response.text}

---
### Featured Gear
* **Check Price:** [Logitech MX Master 3S](https://amzn.to/example)

*As an Amazon Associate, I earn from qualifying purchases.*
"""
    os.makedirs('_posts', exist_ok=True)
    with open("_posts/2026-01-21-ai-sift.md", "w") as f:
        f.write(post_content)
    print("Success: AI post generated.")

if __name__ == "__main__":
    run_sifter()

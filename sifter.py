import os
import google.generativeai as genai

# 1. Setup the AI Brain
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

def run_sifter():
    # 2. We ask the AI to generate a high-value review for a top product
    prompt = """Write a 150-word engaging blog post about the Logitech MX Master 3S mouse. 
    Focus on why it's the best for office productivity. 
    Include 3 bullet points for key features and a 'Who Is This For?' section.
    End with a reminder to check the links below."""
    
    response = model.generate_content(prompt)
    
    # 3. This format tells Jekyll how to display the video and the text
    post_content = f"""---
layout: post
title: "The Ultimate Productivity Tool: MX Master 3S Review"
date: 2026-01-21
youtube_id: "twbL6619v-4"
---

{response.text}

---
### Suggested Gear
* **Top Pick:** [Logitech MX Master 3S](https://amzn.to/3S-example)
* **Budget Option:** [Logitech M720 Triathlon](https://amzn.to/m720-example)

*Disclosure: As an Amazon Associate, I earn from qualifying purchases.*
"""
    # 4. Save the file
    with open("_posts/2026-01-21-ai-sift.md", "w") as f:
        f.write(post_content)

if __name__ == "__main__":
    run_sifter()

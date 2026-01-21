import os

# 1. This is where you tell the robot what to look for
NICHE_KEYWORDS = "Best Amazon Kitchen Gadgets 2026"

def create_test_post():
    # This creates a file that Jekyll can read
    post_content = """---
layout: post
title: "Automated Sift: Cool Gadgets"
date: 2026-01-21
youtube_id: "dQw4w9WgXcQ"
---

### Why we Sifted this:
This video shows some of the best-rated gadgets this month. 
Check out our affiliate links below to support the site!
"""
    # This saves the file into your _posts folder automatically
    with open("_posts/2026-01-21-auto-post.md", "w") as f:
        f.write(post_content)
    print("Post created successfully!")

if __name__ == "__main__":
    create_test_post()

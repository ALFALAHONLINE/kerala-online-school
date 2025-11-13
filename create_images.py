#!/usr/bin/env python3
"""Create placeholder images for AL-FALAH-ONLINE website"""

from PIL import Image, ImageDraw, ImageFont
import os

# Create assets directory if it doesn't exist
assets_dir = "src/assets"
os.makedirs(assets_dir, exist_ok=True)

# Color scheme from design system
PRIMARY_COLOR = (158, 128, 97)  # Approximated from hsl(158, 50%, 38%)
WHITE = (255, 255, 255)
DARK_TEXT = (77, 26, 39)  # Approximated from hsl(30, 10%, 15%)

def create_hero_image():
    """Create hero students placeholder image"""
    img = Image.new('RGB', (1200, 800), PRIMARY_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Add gradient effect
    for i in range(800):
        alpha = int(255 * (i / 800))
        color = (
            int(PRIMARY_COLOR[0] + (255 - PRIMARY_COLOR[0]) * (i / 800) * 0.3),
            int(PRIMARY_COLOR[1] + (255 - PRIMARY_COLOR[1]) * (i / 800) * 0.3),
            int(PRIMARY_COLOR[2] + (255 - PRIMARY_COLOR[2]) * (i / 800) * 0.3)
        )
        draw.line([(0, i), (1200, i)], fill=color)
    
    # Add text
    try:
        # Try to use a system font, fallback to default
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        font = ImageFont.load_default()
    
    text = "AL-FALAH-ONLINE\nIslamic Education"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (1200 - text_width) // 2
    y = (800 - text_height) // 2
    
    draw.text((x, y), text, fill=WHITE, font=font, align="center")
    
    img.save(f"{assets_dir}/herostudents.jpg", "JPEG", quality=85)
    print(f"✓ Created {assets_dir}/herostudents.jpg")

def create_pattern():
    """Create pattern background"""
    img = Image.new('RGB', (400, 400), WHITE)
    draw = ImageDraw.Draw(img)
    
    # Draw pattern
    for i in range(0, 400, 40):
        for j in range(0, 400, 40):
            draw.rectangle([i, j, i+20, j+20], fill=PRIMARY_COLOR, outline=PRIMARY_COLOR)
    
    img.save(f"{assets_dir}/pattern-bg.jpg", "JPEG", quality=85)
    print(f"✓ Created {assets_dir}/pattern-bg.jpg")

def create_placeholder(name, width=1200, height=600):
    """Create generic placeholder image"""
    img = Image.new('RGB', (width, height), PRIMARY_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Add gradient
    for i in range(height):
        alpha = int(255 * (i / height))
        color = (
            int(PRIMARY_COLOR[0] + (255 - PRIMARY_COLOR[0]) * (i / height) * 0.2),
            int(PRIMARY_COLOR[1] + (255 - PRIMARY_COLOR[1]) * (i / height) * 0.2),
            int(PRIMARY_COLOR[2] + (255 - PRIMARY_COLOR[2]) * (i / height) * 0.2)
        )
        draw.line([(0, i), (width, i)], fill=color)
    
    # Add text label
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    
    bbox = draw.textbbox((0, 0), name, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    draw.text((x, y), name, fill=WHITE, font=font)
    
    filename = name.lower().replace(" ", "-").replace("&", "").strip()
    filepath = f"{assets_dir}/{filename}.jpg"
    img.save(filepath, "JPEG", quality=85)
    print(f"✓ Created {filepath}")

# Create images
print("Creating placeholder images...")
create_hero_image()
create_pattern()

# Create other placeholders
placeholders = [
    ("Class Experience", 1000, 600),
    ("Islamic Studies", 1000, 600),
    ("Student Collaboration", 1000, 600),
    ("Achievement Progress", 1000, 600),
    ("Virtual Teacher Student", 1200, 800),
    ("Bismillah", 600, 400),
    ("Hero Students", 1200, 800),
    ("Teacher Student 2", 1000, 700),
]

for name, width, height in placeholders:
    try:
        create_placeholder(name, width, height)
    except Exception as e:
        print(f"✗ Error creating {name}: {e}")

print("\nDone! All placeholder images created.")

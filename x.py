from PIL import Image, ImageDraw, ImageFont
import os
from math import sin, cos, pi

def create_connectiva_logo():
    # Create a new image with a white background
    size = (800, 800)
    background_color = (255, 255, 255)
    logo = Image.new('RGBA', size, background_color)
    draw = ImageDraw.Draw(logo)
    
    # Define colors
    primary_color = (41, 128, 185)  # Blue
    secondary_color = (52, 152, 219)  # Lighter blue
    
    # Draw connecting circles representing social connectivity
    center_x, center_y = size[0] // 2, size[1] // 2
    radius = 200
    circle_size = 40
    num_circles = 6
    
    # Draw connecting lines
    for i in range(num_circles):
        angle = 2 * pi * i / num_circles
        x1 = center_x + radius * cos(angle)
        y1 = center_y + radius * sin(angle)
        
        for j in range(i + 1, num_circles):
            angle2 = 2 * pi * j / num_circles
            x2 = center_x + radius * cos(angle2)
            y2 = center_y + radius * sin(angle2)
            draw.line([(x1, y1), (x2, y2)], fill=secondary_color, width=3)
    
    # Draw circles at intersection points
    for i in range(num_circles):
        angle = 2 * pi * i / num_circles
        x = center_x + radius * cos(angle)
        y = center_y + radius * sin(angle)
        draw.ellipse([x - circle_size//2, y - circle_size//2, 
                      x + circle_size//2, y + circle_size//2], 
                     fill=primary_color)
    
    # Draw central circle
    draw.ellipse([center_x - circle_size, center_y - circle_size,
                  center_x + circle_size, center_y + circle_size],
                 fill=primary_color)
    
    # Save the logo
    output_path = 'connectiva_logo.png'
    logo.save(output_path, 'PNG')
    print(f"Logo saved as {output_path}")

if __name__ == "__main__":
    create_connectiva_logo()

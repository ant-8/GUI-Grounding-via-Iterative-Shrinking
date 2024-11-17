import json
from PIL import Image, ImageDraw, ImageFont
import re

def extract_tuple_from_string(input_string):
    # Find all patterns that match float or integer x, y followed by a closing parenthesis
    matches = re.findall(r'(\d+(?:\.\d+)?),\s*(\d+(?:\.\d+)?)[\)\]]', input_string)
    if matches:
        # Select the last match and convert to floats
        x, y = float(matches[-1][0]), float(matches[-1][1])
        return (x, y)
    else:
        return None


def render_quadrants_with_numbers(image):
    """
    Divides the image into 4 quadrants with clear white borders and black outlines,
    numbers each quadrant at their midpoints, and returns the rendered image and
    the cropped/resized quadrant images with their quadrant IDs.

    Parameters:
        image (PIL.Image): The input image to render quadrants on.

    Returns:
        tuple: A new image with quadrants divided by borders and numbered,
               and a list of cropped/resized quadrant images with numbers.
    """
    image = image.resize((1024, 1024))
    rendered_image = image.copy()
    draw = ImageDraw.Draw(rendered_image)

    # Get the image dimensions
    width, height = image.size
    mid_x = width // 2
    mid_y = height // 2

    # Define the bounding boxes for each quadrant
    quadrants = [
        ((0, 0, mid_x, mid_y), 0),  # Top-left
        ((mid_x, 0, width, mid_y), 1),  # Top-right
        ((0, mid_y, mid_x, height), 2),  # Bottom-left
        ((mid_x, mid_y, width, height), 3)  # Bottom-right
    ]

    # Draw white borders with black outlines
    outline_width = 2  # Thickness of the black outline
    draw.line([(mid_x, 0), (mid_x, height)], fill="blue", width=outline_width)
    draw.line([(0, mid_y), (width, mid_y)], fill="blue", width=outline_width)

    # Number each quadrant at its midpoint with white text and black stroke
    font_size = min(width, height) // 15  # Adjust font size based on image size
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()  # Fallback to default if specific font not available

    quadrant_images = []

    for (bbox, number) in quadrants:
        x1, y1, x2, y2 = bbox
        mid_point = ((x1 + x2) // 2, (y1 + y2) // 2)

        # Draw black stroke by placing text slightly offset in all directions
        for offset in [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (0, 1), (-1, 0), (0, -1)]:
            draw.text((mid_point[0] + offset[0], mid_point[1] + offset[1]), str(number), font=font, fill="white", anchor="mm")

        # Draw the main white number text
        draw.text(mid_point, str(number), font=font, fill="black", anchor="mm")

        # Crop and resize the quadrant image
        quadrant_image = image.crop((x1, y1, x2, y2)).resize((1024, 1024))

        # Draw the quadrant ID in the middle of the cropped image
        quadrant_draw = ImageDraw.Draw(quadrant_image)
        quadrant_mid_point = (1024 // 2, 1024 // 2)
        for offset in [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (0, 1), (-1, 0), (0, -1)]:
            quadrant_draw.text((quadrant_mid_point[0] + offset[0], quadrant_mid_point[1] + offset[1]),
                               str(number), font=font, fill="white", anchor="mm")
        quadrant_draw.text(quadrant_mid_point, str(number), font=font, fill="black", anchor="mm")

        # Add the cropped image to the list
        quadrant_images.append(quadrant_image)

    return rendered_image, quadrant_images

def load_screenspot_ds():
    result = {}
    
    for mode in ['desktop', 'mobile', 'web']:
        with open(f'./screenspot/screenspot_{mode}.json', 'r') as f:
            data = json.load(f)
            
        entries = {
            "text": [],
            "icon": []
        }
        
        for x in data:
            row = {
                "image": Image.open(f"./screenspot/images/{x['img_filename']}"),
                "target": x["instruction"],
                "bbox": x["bbox"],
                "data_type": x["data_type"]
            }
            entries[row["data_type"]].append(row)
    
        result[mode] = entries
    return result

def render_crosshair_center(image):
    rendered_image = image.copy()
    draw = ImageDraw.Draw(rendered_image)
    width, height = image.size

    # Calculate the center coordinates
    center_x = width // 2
    center_y = height // 2

    line_color = "blue"
    line_width = 3

    # Draw vertical and horizontal lines intersecting at the center
    draw.line([(center_x, 0), (center_x, height)], fill=line_color, width=line_width)
    draw.line([(0, center_y), (width, center_y)], fill=line_color, width=line_width)

    return rendered_image

def render_crosshair(image, x, y):
    rendered_image = image.copy()
    draw = ImageDraw.Draw(rendered_image)
    width, height = image.size

    line_color = "blue"
    line_width = 2

    draw.line([(x, 0), (x, height)], fill=line_color, width=line_width)
    draw.line([(0, y), (width, y)], fill=line_color, width=line_width)

    return rendered_image

def draw_bbox_on_image(image, bbox_coords, color='blue', width=3):
    image = image.copy()
    draw = ImageDraw.Draw(image)
    draw.rectangle(bbox_coords, outline=color, width=width)
    return image

def is_in_bbox(bbox, x, y):
    x_min, y_min, width, height = bbox
    x_max = x_min + width
    y_max = y_min + height
    
    return x_min <= x <= x_max and y_min <= y <= y_max

def get_bbox_midpoint(bbox):
    x_min, y_min, width, height = bbox
    x_mid = x_min + (width / 2)
    y_mid = y_min + (height / 2)
    
    return (x_mid, y_mid)
import os
from PIL import Image, ImageSequence
from collections import Counter
import csv

def rgb_to_hex(rgb):
	return "#%02x%02x%02x" % rgb

def extract_pixels(img):
	pixels = []
	if img.format == "GIF":
		for frame in ImageSequence.Iterator(img):
			frame = frame.convert("RGBA")
			for r, g, b, a in frame.getdata():
				pixels.append((r, g, b) if a > 0 else "Transparent")
	elif img.mode == "RGBA":
		for r, g, b, a in img.getdata():
			pixels.append((r, g, b) if a > 0 else "Transparent")
	else:
		pixels = list(img.convert("RGB").getdata())
	return pixels

images_folder = "images"
outputs_folder = "outputs"

os.makedirs(images_folder, exist_ok=True)
os.makedirs(outputs_folder, exist_ok=True)

valid_exts = (".bmp", ".gif", ".jpeg", ".jpg", ".png")
images = [f for f in os.listdir(images_folder) if f.lower().endswith(valid_exts)]

if not images:
	print(f"⚠️ No images found in the '{images_folder}' folder. Place your images there and run again.")
else:
	for img_name in images:
		image_path = os.path.join(images_folder, img_name)
		base_name = img_name.replace(".", "_")
		img = Image.open(image_path)
		pixels = extract_pixels(img)
		total_pixels = len(pixels)
		color_counts = Counter(pixels)
		hex_colors = []
		for color, count in color_counts.most_common():
			percent = count / total_pixels * 100
			hex_colors.append((color if color == "Transparent" else rgb_to_hex(color), count, percent))
			txt_output = os.path.join(outputs_folder, f"{base_name}.txt")
			with open(txt_output, "w", encoding="utf-8") as f:
				f.write(f"Dimensions: {img.width} x {img.height}\n")
				f.write(f"Total Pixels: {total_pixels}\n\n")
				f.write("Hex | Count | Percentage\n")
				for hex_color, count, percent in hex_colors:
					f.write(f"{hex_color} | {count} | {percent:.2f}%\n")
			csv_output = os.path.join(outputs_folder, f"{base_name}.csv")
			with open(csv_output, "w", newline="", encoding="utf-8") as f:
				writer = csv.writer(f)
				writer.writerow(["Hex Color", "Count", "Percentage"])
				for hex_color, count, percent in hex_colors:
					writer.writerow([hex_color, count, f"{percent:.2f}%"])
	print(f"✅ Done! Check the '{outputs_folder}/' folder.")

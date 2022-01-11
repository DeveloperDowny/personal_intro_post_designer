from PIL import Image, ImageDraw


def add_wrapped_to_img(bg_img, wrapped_text, height, x, y_value, final_name, body_font, extra=6):
    for i, line in enumerate(wrapped_text):
        gap = height + extra
        y = y_value + i * gap
        add_text(bg_img, line, x, y, body_font, final_name, "#FFFFFF")


def add_text(my_image, title_text, x, y, title_font, f_name, color):
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((x, y), title_text, fill=color, font=title_font)


def save_img(img, f_name):
    img.save(f"{f_name}.png")


def add_overlay(img1, imgName=""):
    img2 = Image.open(r"spit_overlay.png")
    img1 = img1.resize(img2.size)
    img1.paste(img2, (0, 0), mask=img2)
    img1.save(imgName)

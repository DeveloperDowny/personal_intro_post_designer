import os
import textwrap
from PIL import Image, ImageFont

import img_util
import string_util

# setting font weights
h_body = 30
h_fresher = 22

# setting positions for adding text to photos
y_value = 80
x_value = 605


def design_post(insta_id, full_name, intro, branch, file, app):  # photo should not be here
    static_folder = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])

    title_font = ImageFont.truetype(
        static_folder + "/" + r'fonts/PlayfairDisplay-VariableFont_wght.ttf', 38)
    body_font = ImageFont.truetype(static_folder + "/" + r"fonts/Lato-Regular.ttf", h_body)
    fresher_font = ImageFont.truetype(static_folder + "/" + r"fonts/Lato-Italic.ttf", h_fresher)

    intro = string_util.remove_emojis(intro)
    wrapped_text = textwrap.wrap(intro, width=29)
    final_file_safe_name = string_util.make_file_safe_name(full_name)
    if insta_id == None:
        final_name = app.config['UPLOAD_FOLDER'] + "/" + final_file_safe_name + "_" + "no_insta_id" + ".png"
    else:
        final_name = app.config['UPLOAD_FOLDER'] + "/" + final_file_safe_name + "_" + string_util.make_file_safe_name(
            insta_id) + ".png"

    bg_img = Image.open(file)

    # editing the image below
    img_util.add_overlay(bg_img, final_name)
    bg_img = Image.open(final_name)
    img_util.add_wrapped_to_img(
        bg_img, wrapped_text, h_body, x_value, y_value, final_name, body_font)
    img_util.add_text(bg_img, full_name, x_value, 595,
                      title_font, final_name, "#FFFFFF")
    fresher_text = f"Studying {branch} at SPIT, batch 2021-25"
    fresher_text_wrapped = textwrap.wrap(fresher_text, width=42)
    img_util.add_wrapped_to_img(bg_img, fresher_text_wrapped, h_fresher, x_value, 650, final_name, fresher_font,
                                extra=5)
    bg_img.save(final_name)

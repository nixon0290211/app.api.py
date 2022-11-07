from PIL import Image


def paste_frame(file):
    frame_path = "images/frame.png"
    output_path = "images/out.png"
    img = Image.open(file)
    frame = Image.open(frame_path)
    resized_frame = frame.resize((img.width, img.height))
    img.paste(resized_frame, (0, 0), resized_frame)
    img.save(output_path)
    return output_path

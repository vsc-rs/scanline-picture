from PIL import Image

def create_image_with_transparent_rows(input_image_path, output_image_path):
    # Otvorite originalnu sliku
    original_image = Image.open(input_image_path)
    width, height = original_image.size

    # Kreirajte novu sliku sa transparentnom pozadinom
    new_image = Image.new("RGBA", (width, height + (height // 5)), (0, 0, 0, 0))

    # Kopirajte redove iz originalne slike u novu sliku
    new_height = 0
    for y in range(height):
        if y % 5 == 0 and y != 0:  # Dodajte transparentan red nakon svake 5. linije
            new_height += 1  # Povećajte visinu nove slike za jedan red
        new_image.paste(original_image.crop((0, y, width, y + 1)), (0, new_height))
        new_height += 1  # Povećajte visinu nove slike za jedan red

    # Sačuvajte novu sliku
    new_image.save(output_image_path)

# Primer korišćenja
create_image_with_transparent_rows("slika1.png", "slika2.png")

# slika1.png is an original picture, while slika2.png is a result picture!


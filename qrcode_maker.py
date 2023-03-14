import qrcode
import time
import os
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer


URL = "www.thompsonguitar.studio"
LOGO_PATH = "images/TGS-logo-large-no-bg.png"
OUTPUT_DIR = "output"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=3,
)
qr.add_data(URL)
qr.make(fit=True)

images = [
    qr.make_image(fill_color="black", back_color="white"),
    qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer()),
    qr.make_image(
        image_factory=StyledPilImage,
        embeded_image_path="images/TGS-logo-large-no-bg.png",
    ),
]


def create_logo_qrcode(version, size):
    if not 1 <= version <= 40:
        print(f"Version of {version} outside of the accepted range [1,40]")
    elif not 1 <= size <= 25:
        print(f"Size of {size} outside of range [1,25]")

    qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=size,
        border=3,
    )
    qr.add_data(URL)
    qr.make(fit=True)
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        embeded_image_path=LOGO_PATH,
    )
    filename = f"qrcode-boxsize-{size}-ver-{version}"
    img.save(f"{OUTPUT_DIR}/rounded-with-logo/{filename}.png")


def create_embedded_qrcode(version, size, img_path, output_folder):
    # check for valid qrcode params
    if not 1 <= version <= 40:
        print(f"Version of {version} outside of the accepted range [1,40]")
    elif not 1 <= size <= 25:
        print(f"Size of {size} outside of range [1,25]")
    # confirm output folder existence or create it
    if output_folder not in os.listdir(OUTPUT_DIR):
        os.mkdir(f"{OUTPUT_DIR}/{output_folder}")

    qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=size,
        border=3,
    )

    # link to website
    qr.add_data(URL)
    qr.make(fit=True)
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        embeded_image_path=img_path,
    )

    filename = f"qrcode-boxsize-{size}-ver-{version}-image-{time.time()}"
    img.save(f"{OUTPUT_DIR}/{output_folder}/{filename}.png")


def main():
    if OUTPUT_DIR not in os.listdir():
        os.mkdir(OUTPUT_DIR)
    versions = [1, 5, 10]
    sizes = [20, 22, 24, 25]
    image = LOGO_PATH  # put the path to your image here
    save_folder = "logo"  # put the name of the subdirectory in output/ here where the image set will be stored
    for ver in versions:
        for size in sizes:
            create_embedded_qrcode(ver, size, image, save_folder)


if __name__ == "__main__":
    main()

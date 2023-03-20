from wifi_qrcode_generator.generator import wifi_qrcode
from getpass import getpass
from pathlib import Path



if __name__ == '__main__':
    wifi_name = input("Enter Wifi APN: ").strip()
    wifi_pass = getpass(f"Enter password for '{wifi_name}': ")
    print(wifi_name, wifi_pass)

    qr_code = wifi_qrcode(wifi_name, False, 'WPA', wifi_pass)

    breakpoint()
    # Save the image as PNG file
    qr_code.make_image().save("wifi.png")
    print(f"QR Code saved at: {Path('wifi.png').absolute()}")
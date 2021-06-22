from pyfiglet import figlet_format

def print_art(text):
    ascii_art = figlet_format(text)
    return ascii_art

print(print_art("Hello coder"))

from pygments import highlight
from pygments import lexers
from pygments.formatters.img import ImageFormatter
from pygments.styles import get_style_by_name
from pathlib import Path
from argparse import ArgumentParser

WORK_DIR = Path("static")
IMAGE_NAME = "code.png"
FILE_NAME = "main.py"

parser = ArgumentParser("Code to image")
parser.add_argument("-f", "--filename", type=str)
parser.add_argument("-d", "--direction", type=str)
parser.add_argument("-i", "--image", type=str, default="code.png")

args = parser.parse_args()
try:
    WORK_DIR = Path(args.direction)
except:
    ...
IMAGE_NAME = args.image
FILE_NAME = args.filename if args.filename else "main.c"

print(WORK_DIR.absolute())

lexer = lexers.get_lexer_for_filename(FILE_NAME)


source = """
#include <stdio.h>

int main() {
    printf("Hello, World");
    return 0;
}
"""
try:
    with open(WORK_DIR / FILE_NAME, "r") as f:
        source = f.read()
except:
    ...
formatter = ImageFormatter(full = True, style = get_style_by_name('dracula'), line_number_bg="#ccc", font_size=20, line_numbers=False)
open(WORK_DIR / "images" / IMAGE_NAME, 'wb').write(highlight(source, lexer, formatter))
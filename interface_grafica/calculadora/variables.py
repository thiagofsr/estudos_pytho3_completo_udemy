from pathlib import Path

ROOT_DIR = Path(__file__).parent # isso pq a pasta esta na mesma peasta desse arquivo
FILES_DIR = ROOT_DIR / 'files' # pasta onde se eoncorntrar os arquivos
WINDOW_ICON_PATH = FILES_DIR / 'icon.png'  # caminho do arquivo que esta o icone 

#sizes
BIG_FONT_SIZE = 40
MEDIUM_FONT_SIZE = 24
SMALL_FONT_SIZE = 18
TEXT_MARGIN = 15
MIMINUM_WIDTH = 500


# Colors
PRIMARY_COLOR = '#1e81b0'
DARKER_PRIMARY_COLOR = '#16658a'
DARKEST_PRIMARY_COLOR = '#115270'
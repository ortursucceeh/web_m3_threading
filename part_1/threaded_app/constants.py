CYRILLIC_SYMBOLS = " абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = (
    "_", "a", "b", "v", "g", "d", "e", "e", "j", "z",
    "i", "j", "k", "l", "m", "n", "o", "p", "r", "s",
    "t", "u", "f", "h", "ts", "ch", "sh", "sch", "",
    "y", "", "e", "yu", "ya", "je", "i", "ji", "g"
)
IGNORE_FOLDERS = ("images", "videos", "documents", "audios", "archives")
TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


EXTENSIONS = {
    "images": ['JPEG', 'PNG', 'JPG', 'SVG'],
    "videos": ['AVI', 'MP4', 'MOV', 'MKV'],
    "documents": ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX', 'PPT'],
    "audios": ['MP3', 'OGG', 'WAV', 'AMR'],
    "archives": ['ZIP', 'GZ', 'TAR']
}

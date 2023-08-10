from .Dictionary import Dictionary
from aqt import mw
from aqt.operations.note import update_note
from aqt.utils import showInfo


def query(editor):
    dictionary = Dictionary()
    word = editor.note.fields[0]
    phoneticSymbol, result = dictionary.query(word)
    editor.note.fields[1] = phoneticSymbol
    editor.note.fields[2] = result
    if result == "":
        showInfo(f"未查询到{word}")
    else:
        showInfo("查询成功")
    update_note(parent=mw, note=editor.note)
    '''
    note_type()
    {'id': 1691572198981, 'name': 'English Vocabulary', 'type': 0, 'mod': 1691577272, 'usn': 10, 'sortf': 0, 'did': None, 'tmpls': [{'name': 'Card 1', 'ord': 0, 'qfmt': '{{word}}', 'afmt': '{{content}}\n\n', 'bqfmt': '', 'bafmt': '', 'did': None, 'bfont': '', 'bsize': 0}], 'flds': [{'name': 'word', 'ord': 0, 'sticky': False, 'rtl': False, 'font': 'Arial', 'size': 20, 'description': '', 'plainText': False, 'collapsed': False, 'excludeFromSearch': False}, {'name': 'content', 'ord': 1, 'sticky': False, 'rtl': False, 'font': 'Arial', 'size': 20, 'description': '', 'plainText': False, 'collapsed': False, 'excludeFromSearch': False}], 'css': '.card {\n    font-family: arial;\n    font-size: 20px;\n    text-align: center;\n    color: black;\n    background-color: white;\n}\n', 'latexPre': '\\documentclass[12pt]{article}\n\\special{papersize=3in,5in}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amssymb,amsmath}\n\\pagestyle{empty}\n\\setlength{\\parindent}{0in}\n\\begin{document}\n', 'latexPost': '\\end{document}', 'latexsvg': False, 'req': [[0, 'any', [0]]], 'originalStockKind': 1}
    '''

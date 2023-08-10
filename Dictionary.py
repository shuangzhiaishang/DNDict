import sqlite3
import os.path


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_dir = (BASE_DIR + '\\CambridgeDictionary.db')


class Dictionary:
    def __init__(self):
        self.con = sqlite3.connect(db_dir)
        # cur = self.con.cursor()
        # print(cur.execute("SELECT * FROM dictionary").fetchone())
        # print(cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table'  ''').fetchone())
        #cur.execute('insert into dictionary values (?, ?, ?, ?, ?)', ['fuck', '1', '2', '3', '4'])
        #self.con.commit()

    def query(self, word):
        cur = self.con.cursor()
        res = cur.execute("SELECT * FROM dictionary WHERE word = '%s'" % word)
        rows = res.fetchall()

        if len(rows) == 0:
            return None, None

        result = '<hr>'
        phoneticSymbol = ""
        for i, row in enumerate(rows):
            if i == 0:
                phoneticSymbol = row[1]
            result += f'''<br>{row[-1]}</br><br><b><span class="definition" style="color: #336DF4">{row[2]}</span></b></br>
            '''
            if row[3] is not None:
                examples = row[3].split("@")
                for example in examples:
                    result += f"<br>{example}</br>"
            result += "<hr>"

        return phoneticSymbol, result


if __name__ == "__main__":
    d = Dictionary()
    s, result = d.query("refutation")
    if result is None:
        print('not found')
    print(result)

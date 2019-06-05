import sqlite3

database = 'ACF.sqlite'
conn = sqlite3.connect(database)

"""
    Versículos a serem listados
    Livro abreviado, capítulo, versículo início, versículo fim.
"""
verses = [('Is', 7, 14, 14),
          ('Is', 9, 6, 6),
          ('Lc', 1, 31, 31),
          ('Lc', 2, 6, 7),
          ('At', 17, 31, 31),
          ('Gl', 4, 4, 4),
          ('Fp', 2, 7, 8),
          ('1Tm', 2, 5, 5),
          ('Hb', 4, 15, 15),
          ('Hb', 7, 24, 25)]

cursor = conn.cursor()

sql = """SELECT text 
         FROM verse 
            INNER JOIN book ON book.id = verse.book_id 
         WHERE book.abbreviation = ? 
            AND verse.chapter = ? 
            AND verse.verse BETWEEN ? AND ?;
      """

for v in verses:
    text = "".join([row[0] for row in cursor.execute(sql, v)])

    print("\n{book} {ch}:{v1}{v2}\n{text}"
            .format(
                book=v[0], 
                ch=v[1], 
                v1=v[2], 
                v2='-' + str(v[3]) if v[2] != v[3] else '', 
                text=text))

cursor.close()
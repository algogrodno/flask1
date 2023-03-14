import sqlite3


def get_arts(y:int = 1948):
    conn = sqlite3.connect('Artistc.db')
    cur = conn.cursor()


    
    cur.execute("SELECT * FROM artists WHERE `Birth Year` = (?)", [y])
    arts = cur.fetchall()
    if arts:
        txt = ""
        for art in arts:
            
            #txt += "<p style='padding:10px; border:1px solid'>" + " - ".join(map(str,art[1:])) + "</p>\n"
            txt += "<p style='padding:10px; border:1px solid'>" + art[1] + "</p>\n"
        return txt
    else: 
        return "<h2 style='color:red'> Данных не найдено </h2>"


print(get_arts())
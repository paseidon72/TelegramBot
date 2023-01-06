import sqlite3

base = sqlite3.connect('new.db')
cur = base.cursor()

# base.execute('CREATE TABLE IF NOT EXISTS {}(login PRIMARY KEY, password)'.format('data'))
# base.commit()
#
# cur.execute('INSERT INTO data VALUES(?, ?)', ('jon23', '5465fh'))
# base.commit()
# cur.execute('INSERT INTO data VALUES(?, ?)', ('yan65', '9776tg'))
# base.commit()
# r = cur.execute('SELECT * FROM data').fetchall()
# r = cur.execute('SELECT password FROM data WHERE login == ?', ('jon23',)).fetchall()
# cur.execute('UPDATE data SET password == ? WHERE login == ?', ('9776tg', 'yan65'))
# cur.execute('UPDATE data SET password == ? WHERE password == ?', ('9776tg', 'password'))
# cur.execute('DELETE FROM data WHERE login == ?', ('jon23',))
base.execute('DROP TABLE IF EXISTS data')
base.commit()
base.close()

#encoding:utf-8

import sqlite3


def fix_1():
    """
      在java_ee那个表没有title=java_ee，importance =9
    """
    con = sqlite3.connect('source.db')
    c = con.cursor()
    sql_get_all = 'select * from java_ee'
    sql_inset_one = 'insert into java_ee values(?,?,?,?,?,?)'
    sql_delete_all = 'delete from java_ee'
    data = [(100, u'Java EE', '', 9, 1, 1)]
    for row in c.execute(sql_get_all):
        data.append(row)
    print data
    # c.execute(sql_inset_one, data)
    c.execute(sql_delete_all)
    c.executemany(sql_inset_one, data)
    con.commit()
    con.close()
    print "fix finished"


fix_1()



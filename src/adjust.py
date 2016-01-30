# -*- coding: UTF-8 -*-
import sqlite3 as lite
import sys
from pylab import *







def plot_counts(db_name) :
    con=lite.connect(db_name)
    with con :
        cur = con.cursor()
	s = "SELECT times FROM depurated"
	cur.execute(s)
	items = cur.fetchall()
    items = [i[0] for i in items]
    items=sort(items)
    plot(items,'bo')
    show()
	

		
	    
	    
plot_counts('train.db')

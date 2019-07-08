import sqlite3
def connect():
    conn=sqlite3.connect("bus.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS busadmin(serviceno INTEGER PRIMARY KEY,busname text,source text,destination text,depo text,frequency text,passallowed text)")
    conn.commit()
    conn.close()

def insert(serviceno,busname,source,destination,depo,frequency,passallowed):
    conn = sqlite3.connect("bus.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO busadmin VALUES(?,?,?,?,?,?,?)",(serviceno,busname,source,destination,depo,frequency,passallowed))
    conn.commit()
    conn.close()
def view():
    conn = sqlite3.connect("bus.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM busadmin")
    rows=cur.fetchall()
    conn.close()
    return rows
def search(source="",destination=""):
    conn = sqlite3.connect("bus.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM busadmin WHERE source=? AND destination=?",(source,destination))
    rows=cur.fetchall()
    conn.close()
    return rows
def update(serviceno,busname,source,destination,depo,frequency,passallowed):
    conn = sqlite3.connect("bus.db")
    cur = conn.cursor()
    cur.execute("UPDATE busadmin SET busname=?,source=?,destination=?,depo=?,frequency=?,passallowed=? WHERE serviceno=? ",(busname,source,destination,depo,frequency,passallowed,serviceno))
    conn.commit()
    conn.close()
def delete(serviceno):
    conn = sqlite3.connect("bus.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM busadmin WHERE serviceno=?",(serviceno,))
    conn.commit()
    conn.close()


connect()
#insert(8899,"KNR TRAVELS","BADVEL","REKKAMANU","BDL","DAILY","NO")
#print(search("kadapa","hyderabad"))
#update(1240,"KNR","HYDERABAD","KADAPA","HYD","WEEKEND","YES")
#delete()
print(view())
import sqlite3

sqlite_file = 'db.sqlite'
nutrimi_user_table_name = 'nutrimi_users'
id_column = 'username'
new_column = 'unique_column'
column_type = 'TEXT' # INTEGER, TEXT, NULL, REAL, BLOB
index_name = 'unique_index'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

def add_column_db(self):
    pass

# Adding a new column
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=nutrimi_user_table_name, cn=new_column, ct=column_type))

def update_db(self):
    pass

c.execute("UPDATE {tn} SET {cn}={ncn} WHERE {idc}={nidc}"\
        .format(tn=nutrimi_user_table_name, idc=id_column, cn=new_column))
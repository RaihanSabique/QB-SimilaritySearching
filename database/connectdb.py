import mysql.connector
import pandas as pd
from pprint import pprint


class dataReader:
    data_dict = {}
    df = pd.DataFrame()

    def __init__(self):
        db = mysql.connector.connect(user='raihan', password='123456',
                                      host='localhost',
                                      database='q_bank')
        cursor = db.cursor()
        # Execute SQL select statement
        cursor.execute("SELECT mcqid,qtitle,op1,op2,op3,op4,answer FROM simmcq;")
        print(db)
        print(cursor.column_names)
        #print(cursor.fetchall())
        simmcq=cursor.fetchall()
        #idx=0
        for d in simmcq:
            #print(d[1:])
            self.data_dict.setdefault(d[0],d[1:])
            #idx+=1
        #print(data_dict)
        #self.multmcq_index=idx

        cursor.execute("SELECT mcqid,qtitle,op1,op2,op3 FROM mulmcq;")
        print(db)
        print(cursor.column_names)
        #print(cursor.fetchall())
        mulmcq=cursor.fetchall()
        for d in mulmcq:
            #print(d)
            self.data_dict.setdefault(d[0],d[1:])
            #idx+=1
        #pprint(self.data_dict)
        # Commit your changes if writing
        # In this case, we are only reading data
        # db.commit()
        #print('hello')
        # Get the number of rows in the resultset
        db.close()

    def get_data(self):
        return self.data_dict


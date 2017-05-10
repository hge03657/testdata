import random
import string

TRAN1_COUNT=10000
TRAN1_NAME="TRAN1"
TRAN2_COUNT=10000
TRAN2_NAME="TRAN2"
CUST_COUNT=10000
CUST_NAME="CUSTOMER"

custkey = [ "CUST_{0}".format(i) for i in range(0,CUST_COUNT)]
custattr1 = [ "CUST_A1_{0}".format(i) for i in range(0,10)]
custattr2 = [ "CUST_A2_{0}".format(i) for i in range(0,100)]
tran1attr1 = [ "TRAN1_A1_{0}".format(i) for i in range(0,10)]
trab1attr2 = [ "TRAN1_A2_{0}".format(i) for i in range(0,100)]

custcols = ["CUSTID"] + ["CUSTATTR{0}".format(i) for i in range(1,50)]
t1cols = ["TRAN1ID"] + ["TRAN1ATTR{0}".format(i) for i in range(1,50)]
t2cols = ["TRAN2ID"] + ["TRAN2ATTR{0}".format(i) for i in range(1,50)]

def randstr(l):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(l)])

def mktable(table, cols):
    coldef = ["{0} VARCHAR(30)".format(c) for c in cols]
    print("CREATE TABLE " + table + " (" +
          ",".join(coldef) +
          " , CONSTRAINT " + table + "_PK PRIMARY KEY (" + cols[0] + "));")

def instable(table, cols, idpre, attr1, attr2, count):
    for id in range(1,count+1):
        data0 = ["{0}{1}".format(idpre,id), random.choice(attr1), random.choice(attr2)]
        data1 = [ randstr(30) for i in range(3,len(cols))]
        sql = "INSERT INTO {0}(".format(table);
        sql += ",".join(cols) + ") VALUES ('"
        sql += "','".join(data0 + data1)
        sql += "');"
        print(sql)


def insertcust():
    for k in custkey:
        a1 = random.choice(custattr1)
        a2 = random.choice(custattr2)
        print("INSERT INTO {0}(CUSTCODE,CUSTNAME,CUSTATTR1,CUSTATTR2) VALUES('{1}','CUSTNAME OF {1}','{2}','{3}');".format(CUST_NAME, k, a1, a2))

def mktran():
    print("""CREATE TABLE {0} (
        ID INTEGER,
        CUSTCODE VARCHAR,
        PIECE INTEGER,
        CONSTRAINT {0}_PK PRIMARY KEY (ID)
        );""".format(TRAN_NAME)
        )

def inserttran():
    for i in range(0,TRAN_COUNT):
        cust = random.choice(custkey)
        print("INSERT INTO {0}(ID,CUSTCODE,PIECE) VALUES({1},'{2}','{3}');".format(TRAN_NAME, i, cust, random.randint(1, 100)))

def dropall():
    for t in [CUST_NAME, TRAN1_NAME, TRAN2_NAME]:
        print("DROP TABLE {0};".format(t))

if __name__ == '__main__':
    dropall()
    print("BEGIN;")
    mktable(CUST_NAME, custcols)
    mktable(TRAN1_NAME, t1cols)
    mktable(TRAN2_NAME, t2cols)
    instable(CUST_NAME, custcols, "CUSTID_", custattr1, custattr2, 10000)
    instable(TRAN1_NAME, t1cols, "TRAN1ID_", tran1attr1, tran1attr2, 10000)
    instable(TRAN1_NAME, t2cols, "TRAN2ID_", tran2attr1, tran2attr2, 10000)
    #insertcust()
    #mktran()
    #inserttran()
    print("COMMIT;")

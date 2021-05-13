# author : @akash kumar
#-------------------------------------------------------
#import lib..........
import mysql.connector
from mysql.connector import Error
#------------------------------------------------------

try:
    #connect to database
    connection = mysql.connector.connect(host='localhost',
                                         database='company_detail',
                                         user='root',
                                         password='')
    
    #select *from department;
    """
    +------+----------------------+--------------+-----------------+
    | ID   | NAME                 | COMPANY_CODE | TOTAL_EMPLOYEES |
    +------+----------------------+--------------+-----------------+
    |    1 | Engineering & Techno | A101         |             100 |
    |    2 | Sales,Services & Sup | B102         |             110 |
    |    3 | Marketing & Communic | C103         |             120 |
    |    4 | Business Strategy    | D104         |             130 |
    |    5 | Marketing & Communic | E105         |             140 |
    +------+----------------------+--------------+-----------------+
    """
    #--------------------------------------------------------------------
    #select table
    sql_select_Query1 = "select  TOTAL_EMPLOYEES from department"
    cursor = connection.cursor()
    #execute query.......
    cursor.execute(sql_select_Query1)
    #fetch data from databas--
    records1 = cursor.fetchall()
    #store records2 tuple data in list b[]
    b=[]
    i=0
    for row in records1:
        a=list(records1[i])
        b.append(a[0])
        i+=1
    #---------------------------------------------------------------------
    #select *from company;
    """
    +------+-----------+-------------+-----------------+
    | CODE | NAME      | COUNTRY     | TOTAL_EMPLOYEES |
    +------+-----------+-------------+-----------------+
    | A101 | GOOGLE    | India       |             500 |
    | B102 | MICROSOFT | Australia   |            1000 |
    | C103 | GOOGLE    | India       |             250 |
    | D104 | MICROSOFT | Australia   |             600 |
    | E105 | KPMG      | Netherlands |             100 |
    +------+-----------+-------------+-----------------+
    """
    #--------------------------------------------------------------------
    sql_select_Query2 = "select  COUNTRY from COMPANY"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query2)
    records2 = cursor.fetchall()
    #----------------------------------------------------------------------
    #store records2 tuple data in list bb[]
    i=0
    bb=[]
    for rom in records2:
        aa=list(records2[i])
        bb.append(aa[0])
        i+=1
    #----------------------------------------------------------------------
    ans=0
    for i in range(len(bb)):
        if bb[i]=='India':
            ans+=b[i]
    print("sum of the employees of all department where the country is india is : ",end="")
    print(ans)
    #----------------------------------------------------------------------
except Error as e:
    print("Error reading data from MySQL table", e)
    #-------------------------------Thank you------------------------------

import psycopg2

try:
    connect_str = "dbname='jack' user='jack' host='localhost' " + \
                  "password='password'"
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()
    # create a new table with a single column called "name"
    cursor.execute("select deck from tb_entity where phone ilike '6314131686';")
    # run a SELECT statement - no data in there, but we can try it
    rows = cursor.fetchall()
    print(rows)
except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)


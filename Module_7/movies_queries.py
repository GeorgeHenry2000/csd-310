import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "kurtiscobainus",
    "password": "Musiclife18",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print("\n Database user {} connected to MySQL on host {}". format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")
    query = "SELECT * from studio"
    # execute the operation stored in the query variable using the execute() method
    cursor.execute(query)
    # fetchall() method fetches all rows from the last executed statement on the cursor.
    result = cursor.fetchall()
    print("--DISPLAYING Studio RECORDS--")
    # loop through the rows and print required columns
    for row in result:
        print("Studio ID:", row[0])
        print("Studio Name:", row[1])
        print(" ")

    # display genere records
    query = "SELECT * from genre"
    cursor.execute(query)
    result = cursor.fetchall()
    print("--DISPLAYING Genre RECORDS--")
    for row in result:
        print("Genre ID:", row[0])
        print("Genre Name:", row[1])
        print(" ")
    # display  films whose runtime is less than 2 hours(120 minutes)
    query = "SELECT film_name,film_runtime from film where film_runtime<120 "
    cursor.execute(query)
    result = cursor.fetchall()
    print("--DISPLAYING Short Film RECORDS--")
    for row in result:
        print("Film Name:", row[0])
        print("Runtime:", row[1])
        print(" ")
    # display directors info in the order of their name
    query = "SELECT film_name,film_director from film order by film_director "
    cursor.execute(query)
    result = cursor.fetchall()
    print("--DISPLAYING Director RECORDS in Order--")
    for row in result:
        print("Film Name:", row[0])
        print("Director:", row[1])
        print(" ")
    # close the cursor
    cursor.close()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
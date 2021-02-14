import sqlite3

DATABASE = './data/main.db'


def main(database=DATABASE):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    # create meters table
    cursor.execute('''
CREATE TABLE IF NOT EXISTS registers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nmi TEXT,
    meter_serial_number TEXT,
    register_id TEXT)''')

    # create readings table
    cursor.execute('''
CREATE TABLE IF NOT EXISTS readings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    register_id INTEGER,
    reading TEXT,
    read_date_time TEXT,
    usage TEXT,
    uom TEXT,
    flow_file TEXT)''')

    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()

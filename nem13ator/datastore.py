import sqlite3
import logging


class DataStore:
    '''Performs datbase operations'''

    def __init__(self, database, flow_file):
        self.database = database
        self.flow_file = flow_file

    def add_reading(self, reading):
        try:
            register = self.get_register(
                nmi=reading['NMI'],
                meter_serial_number=reading['MeterSerialNumber'],
                register_id=reading['RegisterID'])

            if register:
                logging.debug('Register already exists')
            else:
                register = self.add_new_register(
                    nmi=reading['NMI'],
                    meter_serial_number=reading['MeterSerialNumber'],
                    register_id=reading['RegisterID'])

            self.add_new_reading(
                    register_id=register,
                    reading=reading['CurrentRegisterRead'],
                    read_date_time=reading['CurrentRegisterReadDateTime'],
                    usage=reading['Quantity'],
                    uom=reading['UOM'],
                    flow_file=self.flow_file)
        except sqlite3.OperationalError as e:
            logging.fatal('Database error: {}'.format(e))
            raise RuntimeError('Database error: {}'.format(e))

    def get_register(self, nmi, meter_serial_number, register_id):
        '''Returns internal register record ID'''

        register_record = None

        try:
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()

            sql = '''
 SELECT id FROM registers
 WHERE
    nmi = ? AND
    meter_serial_number = ? AND
    register_id = ?'''

            cursor.execute(sql, (nmi, meter_serial_number, register_id))
            register_record = cursor.fetchone()[0]

            connection.close()
        except TypeError as e:
            logging.info('Register not found: {}'.format(nmi))

        return register_record

    def add_new_register(self, nmi, meter_serial_number, register_id):
        '''Add a new register record and return ID'''

        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        sql = '''
INSERT INTO registers(nmi, meter_serial_number, register_id)
VALUES (?, ?, ?);'''
        cursor.execute(sql, (nmi, meter_serial_number, register_id))
        register_record = cursor.lastrowid

        connection.commit()
        connection.close()
        logging.info('Register added for NMI: {}'.format(nmi))

        return register_record

    def add_new_reading(self, register_id, reading, read_date_time, usage, uom,
                        flow_file):
        '''Add a new reading'''

        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        sql = '''
INSERT INTO readings(
    register_id, reading, read_date_time, usage, uom, flow_file)
VALUES (?, ?, ?, ?, ?, ?)'''
        cursor.execute(sql, (
            register_id, reading, read_date_time, usage, uom, flow_file))

        connection.commit()
        connection.close()
        logging.info('Reading added for register_id: {}'.format(register_id))

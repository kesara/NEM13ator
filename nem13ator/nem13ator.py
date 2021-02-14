import csv
import logging
import os.path

FIELDS = 'RecordIndicator,NMI,NMIConfiguration,RegisterID,NMISuffix,MDMDataStreamIdentifier,MeterSerialNumber,DirectionIndicator,PreviousRegisterRead,PreviousRegisterReadDateTime,PreviousQualityMethod,PreviousReasonCode,PreviousReasonDescription,CurrentRegisterRead,CurrentRegisterReadDateTime,CurrentQualityMethod,CurrentReasonCode,CurrentReasonDescription,Quantity,UOM,NextScheduledReadDate,UpdateDateTime,MSATSLoadDateTime'.split(',')   # noqa


class NEM13ator:
    '''AEMO NEM13 file processor'''

    def __init__(self, file_path):
        if os.path.isfile(file_path):
            self.file_path = file_path
        else:
            logging.critical('NEM13 file does not exists')
            raise FileNotFoundError('{} does not exists.'.format(file_path))

    def process(self):
        '''Process NEM13 file'''

        with open(self.file_path) as flow_file:
            reader = csv.reader(flow_file)
            result = []
            for row in reader:
                result.append(self._process_row(row))
            return result

    def _process_row(self, row):
        '''Process NEM13 file rows'''

        try:
            record_indicator = int(row[0])
            if record_indicator == 100:
                logging.info('Skipping header row: {}'.format(
                    record_indicator))
            elif record_indicator == 250:
                logging.info(
                        'Processing accumulation meter data row: {}'.format(
                            record_indicator))
                return self._process_nem_data(row)
            elif record_indicator == 550:
                logging.info('Skipping B2B details row: {}'.format(
                    record_indicator))
            elif record_indicator == 900:
                logging.info('Skipping end of data row: {}'.format(
                    record_indicator))
            else:
                raise ValueError('Unknown record indicator: {}'.format(
                    record_indicator))
        except ValueError as e:
            logging.warning('Row error: {}'.format(e))
        except Exception as e:
            logging.error(e)

    def _process_nem_data(self, row):
        '''Process NEM Data Details Row'''
        return dict(zip(FIELDS, row))

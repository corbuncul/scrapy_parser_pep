from collections import defaultdict
import csv
import datetime as dt
import os

from pep_parse.constants import BASE_DIR, DATETIME_FORMAT, HEADER, RESULTS_DIR


class PepParsePipeline:
    """Pipeline для подсчета статистики по документам PEP."""

    def __init__(self):
        self.file_path = os.path.join(BASE_DIR, RESULTS_DIR)
        if not os.path.isdir(self.file_path):
            os.mkdir(self.file_path)

    def open_spider(self, spider):
        """Начальные установки для сохранения статистики."""
        self.results = HEADER
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        """Сбор статистики по статусам документов PEP."""
        status = item['status']
        self.statuses[status] += 1
        return item

    def close_spider(self, spider):
        """Сохранение результатов собранной статистики в файл CSV."""
        self.results.extend(self.statuses.items())
        self.results.append(('Total', sum(self.statuses.values())))
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        csv_file = os.path.join(self.file_path, file_name)
        with open(csv_file, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(self.results)

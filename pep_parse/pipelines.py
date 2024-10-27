import csv
import datetime as dt


class PepParsePipeline:
    def open_spider(self, spider):
        self.total = 0
        self.results = [('Статус', 'Количество')]
        self.statuses = {}

    def process_item(self, item, spider):
        status = item['status']
        self.statuses[status] = self.statuses.get(status, 0) + 1
        self.total += 1
        return item

    def close_spider(self, spider):
        self.results += self.statuses.items()
        self.results += [('Total', self.total)]
        now = dt.datetime.now()
        now_formatted = now.strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = f'results/{file_name}'
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(self.results)

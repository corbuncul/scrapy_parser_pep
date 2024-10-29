"""Костанты парсера."""

from pathlib import Path


BOT_NAME = 'pep_parse'

SPIDER_MODULE = 'spiders'

NAME_SPIDER_PEP = 'pep'

ALLOWED_DOMAINS_PEP = ['peps.python.org']

START_URLS_PEP = [f'https://{domein}/' for domein in ALLOWED_DOMAINS_PEP]

BASE_DIR = Path(__file__).resolve().parent.parent

RESULTS_DIR = 'results'

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

HEADER = [('Статус', 'Количество')]

FIELD_NUMBER = 'number'

FIELD_NAME = 'name'

FIELD_STATUS = 'status'

FIELDS = [FIELD_NUMBER, FIELD_NAME, FIELD_STATUS]

PATTERN = rf'^PEP (?P<{FIELD_NUMBER}>\d+) . (?P<{FIELD_NAME}>.+)\s\|\s.+$'

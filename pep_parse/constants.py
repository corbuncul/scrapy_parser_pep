"""Костанты парсера."""

from pathlib import Path


NAME_SPIDER_PEP = 'pep'

ALLOWED_DOMAINS_PEP = ['peps.python.org']

START_URLS_PEP = ['https://peps.python.org/']

BASE_DIR = Path(__file__).resolve().parent.parent

RESULTS_DIR = 'results'

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

HEADER = [('Статус', 'Количество')]

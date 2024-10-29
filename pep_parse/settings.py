from pep_parse.constants import BOT_NAME, FIELDS, RESULTS_DIR, SPIDER_MODULE


SPIDER_MODULES = [f'{BOT_NAME}.{SPIDER_MODULE}']

NEWSPIDER_MODULE = f'{BOT_NAME}.{SPIDER_MODULE}'

ITEM_PIPELINES = {
    f'{BOT_NAME}.pipelines.PepParsePipeline': 300,
}

FEEDS = {
    RESULTS_DIR + '/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': FIELDS,
        'overwrite': True,
    },
}

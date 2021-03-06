# Scrapy settings for rwscrapper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

# Bot name and version
BOT_NAME = 'rwscrapper'
BOT_VERSION = '1.0'

# Spiders directory
SPIDER_MODULES = ['rwscrapper.spiders']
NEWSPIDER_MODULE = 'rwscrapper.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

# Spider name
RWSPIDER_NAME = 'rw_spider'

# Spider initial seed file
START_SEED_FILE = 'rwscrapper/config/seed.txt'

# Spider allowed domanins file
ALLOWED_DOMAINS_FILE = 'rwscrapper/config/allowed_domains.txt'

# Spider pipelines
ITEM_PIPELINES = [
    'rwscrapper.pipelines.NormalizeTextPipeline', \
    'rwscrapper.pipelines.RomanianTextPipeline', \
    'rwscrapper.pipelines.PhraseSplitterPipeline', \
    'rwscrapper.pipelines.SentenceLevelProcessingPipeline', \
    'rwscrapper.pipelines.WordLevelProcessingPipeline', \
    'rwscrapper.pipelines.DbCommunicatorPipeline', \
]

# Warning messages
NORMALIZED_TEXT_VOID = "Item dropped due to normalized text void"
PROCESSED_TEXT_VOID = "Item dropped due to processed text void"
FOREIGN_LANGUAGE_TEXT = "Item dropped: The text is in other language"
TEXT_CANNOT_BE_SPLITTED = "Item dropped: The text cannot be splitted"
NO_ROMANIAN_PHRASE = "Item dropped: No romanian phrase found"
NO_NEW_WORD = 'Item dropped: No new words found'

# Scores
ROMANIAN_THRESHOLD = 1.78
ROMANIAN_THRESHOLD_NO_PHRASE_CHECK = 1.72

# Database info
USER_NAME = 'scrapper'
USER_PASSWD = 'scrapper'
DEX_DB = 'DEX'
SCRAPPER_DB = 'rwscrapper'
HOSTNAME = 'localhost'

# Cache info
CACHE_CAPACITY = 10000

# Reject no diacritic texts
NO_DIA = False

# Minimum word length
WLEN = 3

# Reject proper names:
PROPER = True

# Maximum dict cache
MAX_DICT_CACHE = 100000

import logging

def setup_logger():
    logging.basicConfig(
        filename='multi_page_scrap.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)

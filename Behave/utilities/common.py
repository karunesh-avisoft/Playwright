import time, logging

# Logger
logger = logging.getLogger(__name__)

# Timespan
def measure(action):
    start = time.perf_counter()
    action()
    return time.perf_counter() - start

# Dialog handler
def dialog_handler(page):
    def handle(dialog):
        logger.info(f"Message: {dialog.message}")
        # Assert dialog text
        assert dialog.type == 'alert', "Unexpected dialog"
        assert dialog.message == "Sorting is broken! This error has been reported to Backtrace.", "Unexpected dialog"
        # Accept the dialog
        dialog.accept()
    page.once("dialog", handle)
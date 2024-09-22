from frontend.app import Application
import logging


logging.basicConfig(
    level=logging.INFO,
    filename='logger.log',
    filemode='w',
    format='''%(levelname)s [%(asctime)s]: %(filename)s > %(funcName)s
    >>> %(message)s''',
    encoding='utf8'
)

app = Application()
app.mainloop()

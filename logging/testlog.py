import logging

logging.basicConfig(filename="test.txt", filemode='w', format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%d-%m-%H-%M-%S', level=logging.INFO)

# logging.basicConfig(filename="test.txt", filemode='w', format='%(asctime)s %(message)s',
#                     datefmt='%Y-%d-%m-%H-%M-%S')

print("Test logs")
logging.info("Hi")
logging.warning("warning msg")
logging.error("error message")

import logging

logging.basicConfig(level=logging.INFO)

logging.info("You have got 20 mails in your inbox!")
logging.critical("All components failed!")

logger = logging.getLogger("NeuralNine Logger")
logger.info("The best logger was just created!")
logger.critical("Your Slack channel was deleted!")
logger.log(logging.ERROR, "An error occured!")
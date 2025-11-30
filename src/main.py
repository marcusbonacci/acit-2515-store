# Imports
import logging

# Local Imports
from app import create_app
from util import logger

def main():
    logger.debug("Starting app")
    create_app()

# Main
if __name__ == "__main__":
    main()
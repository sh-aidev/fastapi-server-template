import warnings

warnings.filterwarnings("ignore")

from src.utils.logger import logger
from src import App


def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()

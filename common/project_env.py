# settings.py
from dotenv import load_dotenv, find_dotenv
# from pathlib import Path
import os


def setup_environment():
    # 自动搜索 .env 文件
    # load_dotenv(verbose=True)

    # 或者指定 .env 文件位置
    # env_path = Path('.') / '.env'
    # load_dotenv(dotenv_path=env_path, verbose=True)

    # from dotenv import load_dotenv, find_dotenv
    # load_dotenv(find_dotenv())

    load_dotenv(find_dotenv(), verbose=True, override=True)

    print(os.getenv('OPENAI_BASE_URL'))
    print(os.getenv('OPENAI_API_KEY'))

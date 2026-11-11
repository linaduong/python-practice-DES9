from dotenv import load_dotenv
import os

load_dotenv()

not_so_secret_secret = os.getenv('secret')
print(not_so_secret_secret)
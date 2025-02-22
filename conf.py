import os
from dotenv import load_dotenv

load_dotenv()


YTOKEN = os.environ.get("YTOKEN")
TOKEN = os.environ.get("TOKEN")
adm = os.environ.get("ADMINS")
ADMINS = [int(admin_id) for admin_id in adm.split(',')]
url = os.environ.get("url")
TOKEN = os.environ.get("TOKEN")
user = os.environ.get("user")
password = os.environ.get("passw")
host = os.environ.get("host")
port = os.environ.get("port")
db = os.environ.get("db")
rbmq_port = os.environ.get("RABBITMQ_PORT")
rbmq_host = os.environ.get("RABBITMQ_HOST")
rbmq_password = os.environ.get("RABBITMQ_PASSWORD")
rbmq_username = os.environ.get("RABBITMQ_USERNAME")
vhost = os.environ.get("VHOST")
# base_url = os.environ.get("BASE_URL")
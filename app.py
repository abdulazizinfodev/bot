import ssl
from pathlib import Path
from aiogram import executor

from loader import dp
import middlewares
import filters
import handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

I18N_DOMAIN = 'mybot'
BASE_DIR = Path(__file__).parent
LOCALES_DIR = BASE_DIR / 'locales'


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)


context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain(certfile='/path/to/your/cert.pem',
                        keyfile='/path/to/your/private.key')

dp.start_webhook(
    webhook_path="/webhook",
    on_startup=on_startup,
    skip_updates=True,
    host="127.0.0.1",
    port=8080,
    ssl_context=context,
)

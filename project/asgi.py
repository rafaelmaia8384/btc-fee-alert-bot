import os
import multiprocessing
from .bot import start_bot
from .fees import fee_monitoring


from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

application = get_asgi_application()

p1 = multiprocessing.Process(target=start_bot)
p2 = multiprocessing.Process(target=fee_monitoring)
p1.start()
p2.start()

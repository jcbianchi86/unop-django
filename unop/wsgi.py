import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unop.settings')

import django
django.setup()

from django.core.management import call_command

# Ejecutar migraciones automáticamente
call_command('migrate', interactive=False)

# Recopilar archivos estáticos
call_command('collectstatic', interactive=False, clear=True)

application = get_wsgi_application()

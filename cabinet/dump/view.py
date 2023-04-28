import os
import json
import subprocess
from django.conf import settings
from django.http import HttpResponse


def dump_request(request):
    sql_dump = subprocess.check_output(['python', os.path.join(settings.BASE_DIR, 'manage.py'), 'dumpdata'])
    sql_dump = sql_dump.decode("utf-8")
    sql_dump = json.loads(sql_dump)

    return HttpResponse(json.dumps(sql_dump, indent=4), content_type='application/json')

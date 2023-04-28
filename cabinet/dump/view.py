import os
import json
import subprocess
from django.http import HttpResponse


def dump_request(request):
    sql_dump = subprocess.check_output(['python', 'manage.py', 'dumpdata'])
    sql_dump = sql_dump.decode("utf-8")
    sql_dump = json.loads(sql_dump)

    return HttpResponse(json.dumps(sql_dump, indent=4), content_type='application/json')

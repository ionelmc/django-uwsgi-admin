import time
from datetime import datetime
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages


@staff_member_required
def index(request):
    try:
        import uwsgi
    except ImportError:
        return render(request, 'uwsgi_admin/uwsgi.html', {
            'unavailable': True
        })

    workers = uwsgi.workers()
    total_load = time.time() - uwsgi.started_on
    for w in workers:
        w['running_time'] = w['running_time'] / 1000
        w['load'] = w['running_time'] / total_load / 10 / len(workers)
        w['last_spawn'] = datetime.fromtimestamp(w['last_spawn'])

    jobs = []
    if 'spooler' in uwsgi.opt:
        spooler_jobs = uwsgi.spooler_jobs()
        for j in spooler_jobs:
            jobs.append({'file': j, 'env': uwsgi.parsefile(j)})

    return render(request, 'uwsgi_admin/uwsgi.html', {
        'masterpid': uwsgi.masterpid(),
        'stats': [
            ('masterpid', str(uwsgi.masterpid())),
            ('started_on', datetime.fromtimestamp(uwsgi.started_on)),
            ('now', datetime.now()),
            ('buffer_size', uwsgi.buffer_size),
            ('total_requests', uwsgi.total_requests()),
            ('numproc', uwsgi.numproc),
            ('cores', uwsgi.cores),
            ('spooler pid', uwsgi.spooler_pid()
                            if uwsgi.opt.get('spooler')
                            else 'disabled'),
            ('threads', 'enabled' if uwsgi.has_threads else 'disabled')
        ],
        'options': uwsgi.opt.items(),
        'workers': workers,
        'jobs': jobs,
    })


@staff_member_required
def reload(request):
    import uwsgi
    if uwsgi.masterpid() > 0:
        uwsgi.reload()
        messages.add_message(request,
                             messages.SUCCESS,
                             _('uWSGI reloaded'),
                             fail_silently=True)
    else:
        messages.add_message(request,
                             messages.ERROR,
                             _('The uWSGI master process is not active'),
                             fail_silently=True)

    return HttpResponseRedirect(reverse("admin:uwsgi_status_changelist"))

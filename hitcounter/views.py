# -*- coding: utf-8 -*-
import json

from ipware.ip import get_ip

from django.http import HttpResponse

from .decorators import ajax_required
from .models import Visit


@ajax_required
def visit_view(request, ct, pk):
    """
    This view should be used along with some front-end scripts.
    This way we can exclude robots from records.
    """
    ip = get_ip(request)
    visit, created = Visit.objects.get_or_create(
        ip=ip, content_type_id=ct, object_id=pk)
    if not created:
        visit.visit_count += 1
        visit.save()
    return HttpResponse(json.dumps({
        'created': created,
        'id': visit.pk,
        'counter': visit.visit_count,
    }), content_type="application/json")

from django.http import JsonResponse
from django.db.models import F

from common.models import Entity, Relation


def listgraph(request):
    if request.user.is_authenticated():
        return JsonResponse({
            'ret': 302,
            'msg': '未登录'},
            status=302)

    if 'project_id' not in request.session:
        return JsonResponse({
            'ret': 302,
            'msg': '未进入项目'},
            status=302)

    pid = request.session['project_id']
    qs_entity = Entity.objects.filter(project_id=pid).values()

    qs_relation = Relation.objects.filter(project_id=pid) \
        .annotate(
        source=F('entity1__id'),
        target=F('entity2__id')
    ) \
        .values(
        'id', 'name', 'source', 'target'
    )

    nodes = list(qs_entity)
    links = list(qs_relation)

    count = 0
    for node in nodes:
        temp = node['id']
        node['id'] = count

        for link in links:
            if link['source'] == temp:
                link['source'] = count
            if link['target'] == temp:
                link['target'] = count

        count += 1

    return JsonResponse({'ret': 0, 'nodes': nodes, 'links': links})
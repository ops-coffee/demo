import json
from django.shortcuts import render
from django.http import JsonResponse

from tree.models import Department


def tree(request):
    mList = Department.objects.all()

    _data = [
        {
            'id': x.id,
            'name': x.name,
            'pId': x.parent.id if x.parent else 0, 'open': 1
        } for x in mList
    ]

    return render(request, 'tree.html', {'data': _data})


def create(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        postdata = {
            "name": data['name'],
            "parent": Department.objects.get(id=data['parent'])
        }

        try:
            Department.objects.create(**postdata)

            return JsonResponse({'state': 1, 'message': '创建成功!'})
        except Exception as e:
            return JsonResponse({'state': 0, 'message': 'Create Error: ' + str(e)})

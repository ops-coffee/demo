import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import render, get_object_or_404

from ops_coffee.models import Blog
from ops_coffee.backends.file import FileRun
from ops_coffee.backends.render import RenderHtml


# Create your views here.

@login_required(login_url='/login')
def index(request):
    if request.method == 'GET':
        state, data = FileRun().read()
        return render(request, 'ops_coffee/index.html', {'state': state, 'data': data})


@login_required(login_url='/login')
def index_save(request):
    if request.method == 'POST':
        postdata = request.body.decode('utf-8')
        content = json.loads(postdata).get('content')

        state, data = FileRun().write(json.dumps(content, ensure_ascii=False))
        return JsonResponse({'state': state, 'message': data})


@login_required(login_url='/login')
def index_push(request):
    if request.method == 'POST':
        postdata = request.body.decode('utf-8')
        content = json.loads(postdata).get('html')

        state, data = RenderHtml().index(content)
        return JsonResponse({'state': state, 'message': data})


@login_required(login_url='/login')
def blog(request):
    if request.method == 'GET':
        _list = Blog.objects.all().order_by('-id')

        return render(request, 'ops_coffee/detail.html', {'lPage': _list})


@login_required(login_url='/login')
def blog_change(request):
    if request.method == 'GET':
        try:
            _data = get_object_or_404(Blog, id=request.GET.get('id'))

            jsondata = model_to_dict(_data, exclude=['create_time', 'update_time'])
            return JsonResponse({'state': 1, 'message': jsondata})
        except Exception as e:
            return JsonResponse({'state': 0, 'message': 'Get Error: ' + str(e)})

    if request.method == 'POST':
        print(request.body.decode('utf-8'))

        postdata = {}
        for key, value in json.loads(request.body.decode('utf-8')).items():
            # 将接收到的json数据去掉csrf和password之后的数据存入字典postdata
            if key != 'csrfmiddlewaretoken' and key != 'password':
                postdata[key] = value if value != '' else None

        try:
            # 根据传入的ID判断是新建还是更新
            object, created = Blog.objects.update_or_create(
                id=postdata.get('id'),
                defaults=postdata
            )

            msg = '创建' if created else '更新'
            return JsonResponse({'state': 1, 'message': msg + '成功 ^_^'})
        except Exception as e:
            return JsonResponse({'state': 0, 'message': 'Error: ' + str(e)})


@login_required(login_url='/login')
def blog_delete(request):
    if request.method == 'POST':
        try:
            _t = Blog.objects.get(id=request.POST.get('id'))
            _t.is_deleted = True
            _t.save()

            return JsonResponse({'state': 1, 'message': '删除成功!'})
        except Exception as e:
            return JsonResponse({'state': 0, 'message': 'Error: ' + str(e)})


@login_required(login_url='/login')
def render_blogs(request):
    if request.method == 'POST':
        state, data = RenderHtml().blogs()
        return JsonResponse({'state': state, 'message': data})

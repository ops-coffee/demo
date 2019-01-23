import os
import time
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def upload(request):
    upload_file = request.FILES['imagefile']
    if request.method == 'POST' and upload_file:
        success, message = 0, '上传失败'

        # 本地创建保存图片的文件夹
        path = settings.STATIC_URL + 'upload/' + time.strftime('%Y%m%d') + '/'
        if not os.path.exists(settings.BASE_DIR + path):
            os.makedirs(settings.BASE_DIR + path)

        # 拼装本地保存图片的完整文件名
        filename = time.strftime('%H%M%S') + '_' + upload_file.name
        local_file = settings.BASE_DIR + path + filename

        # 写入文件
        with open(local_file, 'wb+') as f:
            for chunk in upload_file.chunks():
                f.write(chunk)

            success, message = 1, '上传成功'

        # 返回格式
        data = {
            'success': success,
            'message': message,
            'url': path + filename
        }

        return JsonResponse(data)
    else:
        return JsonResponse({'state': 0, 'message': 'Not support method or Can not get file'})

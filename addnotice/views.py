from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from adminnotice.models import Notice
# Create your views here.

@csrf_exempt
def addnotice(request):
    print('reached')
    if request.method == 'POST':
        title = request.POST.get('title-field')
        content = request.POST.get('content')
        new_notice = Notice(title=title,content=content)
        new_notice.save()
        return redirect('Add Notice')
    return render(request, 'addnotice.html')

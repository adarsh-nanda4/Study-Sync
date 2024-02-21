from django.shortcuts import render,get_object_or_404,redirect
from django.views.decorators.csrf import csrf_exempt
from adminnotice.models import Notice
# Create your views here.
@csrf_exempt
def adminnotice(request):
    context={'context':reversed(Notice.objects.all())}
    return render(request,'adminnotice.html',context)

@csrf_exempt
def delete_notice(request,id):
    notice_to_delete = get_object_or_404(Notice,id=id)
    context={'context':reversed(Notice.objects.all())}
    if request.method == 'POST':
        notice_to_delete.delete()
        return redirect('Admin Notice')
    return render(request, 'adminnotice.html',context)
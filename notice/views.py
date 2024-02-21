from django.shortcuts import render

from adminnotice.models import Notice
def viewnotice(request):
    context={'context':reversed(Notice.objects.all())}
    return render(request,'viewnotice.html',context)

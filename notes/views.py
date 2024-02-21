from django.shortcuts import render,get_object_or_404,redirect
from adminnotes.models import Notes
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def viewnotes(request):
    context={'context':reversed(Notes.objects.all())}
    return render(request,'viewnotes.html',context)

@csrf_exempt
def filternotes(request):
    if request.method == 'POST':
        department = request.POST.get('select-dept')
        sem = request.POST.get('select-sem')
        print(request.POST)  # Add this line to print the entire POST data
        print(department)
        print(sem)
        filterednotes = Notes.objects.filter(department=department, sem=sem)
        print(filterednotes.values())
        if filterednotes.exists():
            context = {'context': filterednotes}
            return render(request, 'viewnotes.html', context)
        else:
            return render(request,'viewnotes.html',{'context':reversed(Notes.objects.all())})

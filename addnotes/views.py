from django.shortcuts import render,redirect

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from adminnotes.models import Notes

@csrf_exempt
def addnotes(request):
    if request.method == 'POST':
        title = request.POST.get('title-field')
        department = request.POST.get('select-dept').upper() 
        sem = request.POST.get('select-sem')
        content = request.POST.get('content')
        files = request.FILES.get('files')  
        print(f"Title: {title}, Department: {department}, Sem: {sem}")
        new_note = Notes(title=title, department=department, sem=sem, content=content, files=files)
        new_note.save()
        return redirect('Add Notes')

    return render(request, 'addnotes.html')
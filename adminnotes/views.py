from django.shortcuts import render,get_object_or_404,redirect
from adminnotes.models import Notes
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def adminnotes(request):
    context={'context':reversed(Notes.objects.all())}
    return render(request,'adminnotes.html',context)


@csrf_exempt
def delete_note(request,id):
    print(f"Deleting note with title: {id}")
    note_to_delete = get_object_or_404(Notes, id=id)
    context={'context':reversed(Notes.objects.all())}
    if request.method == 'POST':
        print("POST request received")
        if note_to_delete.files:
            note_to_delete.files.delete()
        note_to_delete.delete()
        return redirect('Admin Notes')
        # added the name of the url not the url
    return render(request,'adminnotes.html',context)



@csrf_exempt
def filternotesadmin(request):
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
            return render(request, 'adminnotes.html', context)
        else:
            return render(request,'adminnotes.html',{'context':reversed(Notes.objects.all())})

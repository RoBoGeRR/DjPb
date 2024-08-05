from django.shortcuts import get_object_or_404, render, redirect
from .models import Paste
from .forms import PasteForm

# Create your views here.
def create_paste(request):
    if request.method == 'POST':
        form = PasteForm(request.POST)
        print('POST')
        if form.is_valid():
            print('is_valid')
            paste = form.save(commit=False)
            paste.user_profile = request.user.userprofile
            paste.save()
            return redirect('home')
    else:
        if request.user.is_authenticated:
            form = PasteForm()
        else:
            return redirect('home')
    return render(request, 'pastes/create_paste.html', {'form': form})

def paste_edit(request, pk):
    instance = get_object_or_404(Paste, id=pk)
    if request.method=="POST":
        form = PasteForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = PasteForm(instance=instance)

    print(instance.id)
    return render(request, 'pastes/edit_paste.html', {'form': form,'instance':instance})        

def paste_list(request):
    pastes = Paste.objects.all()
    return render(request, 'pastes/paste_list.html', {'pastes': pastes})
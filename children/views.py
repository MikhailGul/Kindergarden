from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OpenDayForm
from .models import OpenDayRegistration
from django.contrib import messages
from children.forms import ChildApplicationForm
from children.models import Child, ChildPhoto

def open_day_registration(request):
    if request.method == 'POST':
        form = OpenDayForm(request.POST)
        if form.is_valid():
            OpenDayRegistration.objects.create(
                parent_name=form.cleaned_data['parent_name'],
                phone=form.cleaned_data['phone']
            )
            messages.success(request, 'Спасибо за заявку! Мы свяжемся с вами для подтверждения.')
            return redirect('home')
    else:
        form = OpenDayForm()
    
    return render(request, 'children/open_day_registration.html', {'form': form})

@login_required
def add_child(request):
    if request.method == 'POST':
        form = ChildApplicationForm(request.POST)
        if form.is_valid():
            child = form.save(commit=False)
            child.parent = request.user
            child.save()
            messages.success(request, 'Заявка отправлена! Галерея будет создана после одобрения.')
            return redirect('profile')
    else:
        form = ChildApplicationForm()
    
    return render(request, 'children/add_child.html', {'form': form})

@login_required
def child_gallery(request, child_id):
    child = get_object_or_404(Child, id=child_id, parent=request.user)
    photos = child.photos.all()  # Получаем все фото ребенка
    
    # Для отладки - выводим данные в консоль
    print(f"Child: {child}")
    print(f"Photos count: {photos.count()}")
    
    return render(request, 'children/child_gallery.html', {
        'child': child,
        'photos': photos
    })
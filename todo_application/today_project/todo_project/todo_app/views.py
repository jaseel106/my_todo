from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import task
from . forms import todoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# class views
class TaskListview(ListView):
    model = task
    template_name = 'index.html'
    context_object_name = 'show'

class TaskDetailivew(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'task'

class TaskUpdateview(UpdateView):
    model = task
    template_name = 'update_view.html'
    context_object_name = 'task'
    fields = ('name', 'priority')

    def get_success_url(self):
        return reverse_lazy('todo_app:cbvdetail', kwargs={'pk': self.object.id})

class TaskDeleteview(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('todo_app:cbvhome')

# function views
# Create your views here.
def demo1(request):
    task_show = task.objects.all()
    if request.method == 'POST':
        name1 = request.POST.get('task', '')
        prio1 = request.POST.get('priority', '')
        date1 = request.POST.get('date', '')

        Task = task(name=name1, priority=prio1, date=date1)
        Task.save()


    return render(request, 'index.html', {'show': task_show })

def delete(request, taskid):
    task_delete = task.objects.get(id=taskid)
    if request.method == 'POST':
        task_delete.delete()

        return redirect('/')

    return render(request, 'delete.html')

def update(request, updateid):
    task_update = task.objects.get(id=updateid)
    form = todoForm(request.POST or None, instance=task_update)
    if form.is_valid():
        form.save()

        return redirect('/')
    return render(request, 'update.html', {'f':form, 't':task_update})

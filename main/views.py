from django.shortcuts import render
from . import models
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from main.models import Todo
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")    
    return render(request, 'main/index.html', {
        "todo_items": todo_items,
    })

# def home(request):
#     todo_items = Todo.objects.all().order_by("-added_date")
#     return render(request, 'main/index.html', {
#       "todo_items": todo_items
#     })


@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    mycontent = request.POST['content']
    created_obj = Todo.objects.create(added_date=current_date, text=mycontent)
    # print('--------------')
    # print (created_obj.text)
    # print (created_obj.added_date)
    # print('--------------')
    # return render(request, 'main/index.html')
    return HttpResponseRedirect("/")

@csrf_exempt
def del_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()    
    # print('--------------')
    # print (todo_id, ' to be deleted')
    # print('--------------')
    return HttpResponseRedirect("/")
# @csrf_exempt
# def delete_todo(request, todo_id):
#   Todo.objects.get(id=todo_id).delete()
#   return HttpResponseRedirect("/")

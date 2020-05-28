from django.conf.urls import url
from django.contrib import admin
from main import views
from django.urls import path


urlpatterns = [
#   url(r'^admin/', admin.site.urls),
#   url(r'^$', views.home, name='home'),
    # url('', views.home, name='home'),
    path('', views.home, name='home'),
    path('add_todo/', views.add_todo),
    path('del_todo/<int:todo_id>/', views.del_todo),
]

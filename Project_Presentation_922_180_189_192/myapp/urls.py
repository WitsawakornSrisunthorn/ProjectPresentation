from django.urls import path
from myapp import views
from django.contrib.auth.decorators import login_required
from . import views
from .views import signup # ตรวจสอบว่าคุณได้ import ฟังก์ชัน signup มาแล้ว
from .views import search_view

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('form/', views.form, name='form'),  # เพิ่ม URL pattern สำหรับ 'form' ที่เชื่อมโยงกับ views.form และตั้งชื่อว่า 'form'
    path('edit/<person_id>', views.edit),
    path('delete/<person_id>', views.delete),
    path('signup/', signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('search/', search_view, name='search'),
]

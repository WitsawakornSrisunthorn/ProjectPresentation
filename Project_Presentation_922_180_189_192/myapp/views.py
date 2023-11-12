from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Person
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#############################################################################
def about(request):
    return render(request,"about.html")


def index(request):
    all_person = Person.objects.all()
    return render(request, "index.html", {"all_person": all_person})
@login_required(login_url='login')
def form(request):
    if request.method == "POST":
        # รับข้อมูล
        name = request.POST["name"]
        age = request.POST["age"]

        # บันทึกข้อมูล
        person = Person.objects.create(
            name=name,
            age=age
        )
        person.save()
        messages.success(request, "ขอบคุณสำหรับข้อมูล")
        # เปลี่ยนเส้นทาง
        return redirect("/")
    else:
        return render(request, "form.html")

@login_required(login_url='login')  # เพิ่ม decorator เพื่อป้องกันการเข้าถึง
def edit(request, person_id):
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.name = request.POST["name"]
        person.age = request.POST["age"]
        person.save()
        messages.success(request, "อัพเดตข้อมูลเรียบร้อย")
        return redirect("/")
    else:
        person = Person.objects.get(id=person_id)
        return render(request, "edit.html", {"person": person})

@login_required(login_url='login')  # เพิ่ม decorator เพื่อป้องกันการเข้าถึง
def delete(request, person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    messages.success(request, "ลบข้อมูลเรียบร้อย")
    return redirect("/")
################################################################################################
# views.py

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'ลงทะเบียนสำเร็จ! ยินดีต้อนรับ, {}'.format(user.username))
            return redirect('login')  # ให้ไปยังหน้าที่คุณต้องการหลังจากลงทะเบียนสำเร็จ
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # ตรวจสอบความถูกต้องของชื่อผู้ใช้และรหัสผ่าน
        if not username or not password:
            messages.error(request, 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง')
            return render(request, 'login.html')

        # ตรวจสอบสถานะการล็อกอินของผู้ใช้
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('form')  # หน้าหลักหลังจากล็อกอินสำเร็จ

        else:
            # กรณีล็อกอินไม่สำเร็จ
            messages.error(request, 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง')
            return render(request, 'login.html')
    else:
        # แสดงฟอร์มล็อกอิน
        return render(request, 'login.html')
##############################################################################
# views.py


from django.shortcuts import render
from .forms import SearchForm
from .models import Person  # แทน YourModel ด้วยชื่อ model ที่คุณใช้

@login_required(login_url='login')  # เพิ่ม decorator เพื่อป้องกันการเข้าถึง
def search_view(request):
    form = SearchForm(request.GET)
    results = None

    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        results = Person.objects.filter(name__icontains=search_query)  # แทน YourModel ด้วยชื่อ model ที่คุณใช้

    return render(request, 'search_results.html', {'search_form': form, 'results': results})


from django.shortcuts import render,redirect
from Adminapp.models import*
from.models import*
# Create your views here.
def userindex(request):
    data2=Category.objects.all()
    return render(request,'userindex.html',{'data2':data2})
def category_card(request):
    data=Category.objects.all()
    return render(request,'cat_viewmore.html',{'data':data})
def cat_viewmore(request,id):
    data=Category.objects.filter(id=id)
    return render(request,'category_card.html',{'data':data})  
def service_card(request,category):
    if(category =="all"):
        data1=Service.objects.all()
    else:
        data1=Service.objects.filter(category=category)
    data2=Category.objects.all()
    return render(request,'service_viewmore.html',{'data1':data1,'data2':data2})

def service_viewmore(request,id):
    data=Service.objects.filter(id=id)
    return render(request,'service_card.html',{'data':data})  

def about(request):
    return render(request,'about.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def reg(request):
    if request.method=='POST':
        username=request.POST['name']
        password=request.POST['pass']
        phone=request.POST['numb']
        email=request.POST['email']
        address=request.POST['address']
        data=Register(User_Name=username,Pass_word=password,Phone_Number=phone,Email=email,Address=address)
        data.save()
        return redirect('reg_table')
def log(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if Register.objects.filter(User_Name=username,Pass_word=password).exists():
           data = Register.objects.filter(User_Name=username,Pass_word=password).values('Phone_Number','Email','id','Address').first()
           request.session['address_u'] = data['Address'] 
           request.session['u_id'] = data['id']
           request.session['phonenumber_u'] = data['Phone_Number'] 
           request.session['email_u'] = data['Email'] 
           request.session['username_u'] = username
           request.session['password_u'] = password
           return redirect('category_card') 
        else:
            return render(request,'login.html',{'msg':'invalid user credentials'})
    else:
        return redirect('userindex')

def userlogout(request):
    del request.session['address_u']
    del request.session['u_id']
    del request.session['phonenumber_u']
    del request.session['email_u']
    del request.session['username_u']
    del request.session['password_u']
    return redirect('userindex')
def booking(request,id):
    u=request.session.get('u_id')
    data=Book.objects.filter(User_id=u,Status=0)
    data1=Service.objects.all()
    return render(request,'booking.html',{'data':data,'data1':data1})
def book(request):
    if request.method=='POST':
        userid=request.session.get('u_id')
        serviceid=request.POST['service']
        Date=request.POST['date']
        Time=request.POST['time']
        data=Book(User_id=Register.objects.get(id=userid),Service_id=Service.objects.get(id=serviceid),Date=Date,Time=Time)
        data.save()
        return redirect('success_page')
def branches(request):
    return render (request,'branches.html')
def success_page(request):
    u=request.session.get('u_id')
    data=Book.objects.filter(User_id=u)
    return render(request,'success_page.html',{'data':data})
def branch_card(request):
    data=Branch.objects.all()
    return render(request,'branch_card.html',{'data':data})
def contact(request):
    return render(request,'contact.html')
def contactus(request):
    if request.method=='POST':
        nam=request.POST['nam']
        mail=request.POST['eml']
        Message=request.POST['msg']
        data=Contact(Name=nam,mail=mail,Message=Message)
        data.save()
        return redirect('contact_table')
    return render(request,'contact.html')
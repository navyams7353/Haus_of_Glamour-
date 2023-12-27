from django.shortcuts import render,redirect
from.models import*
from Userapp.models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def index(request):
    Categories=Category.objects.all().count()
    Services=Service.objects.all().count()
    Branches=Branch.objects.all().count()
    Appoinments=Book.objects.all().count()
    Contacts=Contact.objects.all().count()
    return render(request,'index.html',{'Categories':Categories,'Services':Services,'Branches':Branches,'Appoinments':Appoinments,'Contacts':Contacts})
def category(request):
    return render (request,'category.html')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
def form(request):
    if request.method=='POST':
        category=request.POST['name']
        Image=request.FILES['image']
        Description=request.POST['description']
        data=Category(Cat_Name=category,Image=Image,Description=Description)
        data.save()
        return redirect('cat_table')
def edit(request,id):
    data=Category.objects.filter(id=id)
    return render(request,'edit_cat.html',{'data':data})
def update(request,id):
    if request.method=='POST':
        category=request.POST['name']
        try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Category.objects.get(id=id).Image
        Description=request.POST['description']
        Category.objects.filter(id=id).update(Cat_Name=category,Image=file,Description=Description)
        return redirect('cat_table')
def delete(request,id):
    Category.objects.filter(id=id).delete()
    return redirect('cat_table')
def cat_table(request):
    data=Category.objects.all()
    return render(request,'cat_table.html',{'data':data})
def service(request):
    data=Category.objects.all()
    return render (request,'services.html',{'data':data})
def products(request):
    if request.method=='POST':
        Services=request.POST['service']
        Image=request.FILES['img']
        cat=request.POST['category']
        Price=request.POST['price']
        data=Service(Service_Name=Services,Images=Image,category=cat,Price=Price)
        data.save()
        return redirect('service_table')
def service_table(request):
    data=Service.objects.all()
    return render(request,'Service_table.html',{'data':data})
def edit_services(request,id):
    data=Service.objects.filter(id=id)
    data1=Category.objects.all()
    return render(request,'edit_services.html',{'data':data,'data1':data1})
def update_service(request,id):
    if request.method=='POST':
        Services=request.POST['service']
        try:
            img_c = request.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Service.objects.get(id=id).img
        cat=request.POST['category']
        Price=request.POST['price']
        Service.objects.filter(id=id).update(Service_Name=Services,Images=file,category=cat,Price=Price)
        return redirect('reg_table')
def delete_service(request,id):
    Service.objects.filter(id=id).delete()
    return redirect('service_table')
def booking_table(request):
    data=Book.objects.filter(Status=0)
    return render (request,'booking_table.html',{'data':data})
def reg_table(request):
    data=Register.objects.all()
    return render (request,'reg_table.html',{'data':data})
def branch(request):
    return render(request,'branches.html')
def Bran(request):
    if request.method=='POST':
        Branch_Name=request.POST['branch']
        Image=request.FILES['imagess']
        Location=request.POST['location']
        data=Branch(Branch_Name=Branch_Name,Img=Image,Location=Location)
        data.save()
        return redirect('branch_table')
def branch_table(request):
    data=Branch.objects.all()
    return render (request,'branch_table.html',{'data':data})
def delete_branch (request,id):
    Branch.objects.filter(id=id).delete()
    return redirect('branch_table')
def delete_appoinment(request,id):
    Book.objects.filter(id=id).update(Status=2)
    return redirect('booking_table')
def approve(request,id):
    Book.objects.filter(id=id).update(Status=1)
    return redirect('booking_table')
def contact_table(request):
    data=Contact.objects.all()
    return render (request,'contact_table.html',{'data':data})

    
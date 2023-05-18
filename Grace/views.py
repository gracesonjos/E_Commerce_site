from django.shortcuts import render , redirect,HttpResponse
from django.core.files.storage import FileSystemStorage
from Grace.models import idgen
from Grace.models import tbl_category
from Grace.models import tbl_shope
from Grace.models import tbl_product
from Grace.models import tbl_coustomer
from Grace.models import tbl_login
from Grace.models import tbl_order
from Grace.models import tbl_review
from Grace.models import tbl_deliveryagent
import datetime
from django.core.mail import send_mail
 


def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def product(request):
    return render(request,'products.html')

def reservation(request):
    data= tbl_category.objects.all()
    return render(request,'reservation.html',{"g":data})


def testimonial(request):
    return render(request,'testimonial.html')


def ourstory(request):
    return render(request,'ourstory.html')

def ourvision(request):
    return render(request,'ourvision.html')

def adminmenu(request):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        return render(request,'adminmenu.html')


def addcategory(request):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        return render(request,'addcategory.html')


def actioncategory(request):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        data=idgen.objects.get(id=1)
        f=int(data.categoryid)
        f=f+1
        f1="Category"+str(f)
        data = tbl_category()
        data.category_id=f1
        data.category_name=request.POST.get("name")
        data.photo=request.POST.get("photo")
        data.description=request.POST.get("description")

        Photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo) 
        uploaded_file_url = fs.url(filename)
        data.photo= uploaded_file_url
        data.save()
        
        data1=idgen.objects.get(id=1)
        data1.categoryid=f
        data1.save()
        return render(request,"addcategory.html")


def updateviewcategory(request):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        data = tbl_category.objects.all()
        return render (request,"updateviewcategory.html",{"g":data})


def updatecategory(request, a):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        data = tbl_category.objects.get(category_id=a)
        return render(request,'updatecategory.html',{"g":data})



def updateactioncategory(request,a):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        data=tbl_category.objects.get(category_id=a)
        if request.POST.get("photo")=="":
            if request. method =="POST":
                data.category_id= request.POST.get("category_id")
                data.category_name= request.POST.get("name")
                data.description = request.POST.get("discription")
            
                data.save()
                return redirect('/updateviewcategory')
        else:
            if request. method =="POST":
                data.category_id= request.POST.get("category_id")
                data.category_name= request.POST.get("name")
                data.description = request.POST.get("discription")
                Photo = request.FILES['photo']
                fs = FileSystemStorage()
                filename = fs.save(Photo.name, Photo) 
                uploaded_file_url = fs.url(filename)
                data.photo=uploaded_file_url
            
                data.save()
                return redirect('/updateviewcategory')


def deletecategory(request):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        data=tbl_category.objects.all()
        return render (request,'deletecategory.html',{"g":data})
        

def actiondeletecategory(request, a):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        data = tbl_category.objects.get(category_id= a)
        data.delete()
        return redirect('/deletecategory')


def addshope(request):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        return render(request,'addshope.html')

def actionshope(request):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        count =tbl_shope.objects.filter(username=request.POST.get("user_id")).count()
        if count==0:
            data=idgen.objects.get(id=1)
            f=int(data.shopeid)
            f=f+1
            f1="Shope"+str(f)
            data = tbl_shope()
            data.shope_id=f1
            data.shope_name=request.POST.get("shope_name")
            data.location=request.POST.get("location")
            data.pincode=request.POST.get("pincode")
            data.phone_number=request.POST.get("phone_number")
            data.email=request.POST.get("email")
            data.photo=request.POST.get("photo")
            data.username=request.POST.get("user_id")
            Photo = request.FILES['photo']
            fs = FileSystemStorage()
            filename = fs.save(Photo.name, Photo) 
            uploaded_file_url = fs.url(filename)
            data.photo= uploaded_file_url
            data.save()

            data2 = tbl_login()
            data2.username=request.POST.get("user_id")
            data2.password=request.POST.get("password")
            data2.category = "shope"
            data2.hint=request.POST.get("hint")
            data2.save()
            
            data1=idgen.objects.get(id=1)
            data1.shopeid=f
            data1.save()
            send_mail('Your User ID and Password','Dear coustomer '+'\n\n'+'I am writing this email to provide you with your user ID and password to access Grace Times And Eletronics. Your login credentials are as follows'+'\n'+'User ID: '+request.POST.get('user_id')+'\n'+'Password:  '+request.POST.get('password')+'\n'+'Please keep your login details confidential and do not share them with anyone. We recommend that you change your password periodically for added security.'+'\n'+'If you encounter any issues while logging in or have forgotten your password, please click on the "Forgot Password" link on the login page to reset your password.'+'\n'+'We hope that you have a pleasant experience using our platform. If you have any questions or concerns, please do not hesitate to contact us at coustomer@gmail.com'+'\n'+'Thank you for choosing Grace Times and Eletronics. We look forward to serving you.'+'\n'+'Best regards'+'\n'+'Graceson','from@example.co',[request.POST.get('email'),])
            return render(request,"addshope.html")
        else:
            return HttpResponse("user already exist.............")


def updateviewshope(request):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        data=tbl_shope.objects.all()
        return render(request,'updateviewshope.html',{"g":data})

def updateshope(request,a):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        data=tbl_shope.objects.get(shope_id=a)
        return render(request,'updateshope.html',{"g":data})

def updateactionshope(request,a):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        data = tbl_shope.objects.get(shope_id=a)
        if request.POST.get("photo")=="":
            if request.method == 'POST':
                data.shope_id=request.POST.get("shope_id")
                data.shope_name=request.POST.get("shope_name")
                data.location=request.POST.get("location")
                data.pincode=request.POST.get("pincode")
                data.phone_number=request.POST.get("phone_number")
                data.email=request.POST.get("email")
                
                data.save()
                
                return redirect('/updateviewshope')
        else:
            if request.method == 'POST':
                data.shope_id=request.POST.get("shope_id")
                data.shope_name=request.POST.get("shope_name")
                data.location=request.POST.get("location")
                data.pincode=request.POST.get("pincode")
                data.phone_number=request.POST.get("phone_number")
                data.email=request.POST.get("email")
                data.photo=request.POST.get("photo")

                Photo = request.FILES['photo']
                fs = FileSystemStorage()
                filename = fs.save(Photo.name, Photo) 
                uploaded_file_url = fs.url(filename)
                data.photo=uploaded_file_url
            
                data.save()
                return redirect('/updateviewshope')


def deleteshope(request):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        data= tbl_shope.objects.all()
        return render(request,'deleteshope.html',{"g":data})
        
def deleteactionshope(request,a):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        data=tbl_shope.objects.get(shope_id=a)
        data.delete()
        data2=tbl_login.objects.get(username=data.username)
        data2.delete()
        return redirect("/deleteshope")

def shopemenu(request):
    if 'shope' not in request.session:
        return render(request,"home.html")
    else:
        return render(request,'shopemeanubar.html')

def addproduct(request):
    if 'shope' not in request.session:
        return render(request,"home.html")
    else:
        data=tbl_category.objects.all()
        shopid=request.session['shope']
        data2=tbl_shope.objects.get(username=shopid)
        return render(request,'addproduct.html',{'g':data,'shopid':data2.shope_id})

def actionproduct(request):
    if 'shope' not in request.session:
        return render(request,"home.html")
    else:
        data=idgen.objects.get(id=1)
        f=int(data.productid)
        f=f+1
        f1="Product"+str(f)
        data = tbl_product()
        data.product_id=f1
        data.category_id_id=request.POST.get("category_id")
        data.shope_id_id=request.POST.get("shope_id")
        data.product_name=request.POST.get("product_name")
        data.price=request.POST.get("price")
        data.description=request.POST.get("description")
        data.photo=request.POST.get("photo")
        data.stock=request.POST.get("stock")


        Photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo) 
        uploaded_file_url = fs.url(filename)
        data.photo= uploaded_file_url
        data.save()
        
        data1=idgen.objects.get(id=1)
        data1.productid=f
        data1.save()
        return redirect('/addproduct')

def updateviewproduct(request):
    if 'shope' not in request.session:
        return render(request,"home.html")
    else:
        username=request.session['shope']
        data2=tbl_shope.objects.get(username=username)
        data=tbl_product.objects.filter(shope_id_id=data2.shope_id)
        return render(request,'updateviewproduct.html',{"g":data})

def updateproduct(request,a):
    if 'shope' not in request.session:
        return render(request,"home.html")
    else:
        data=tbl_product.objects.get(product_id=a)
        data1=tbl_category.objects.all()
        return render(request,'updateproduct.html',{"g":data,'data1':data1})

def updateactionproduct(request,a):
    if 'shope' not in request.session:
        return render(request,"home.html")
    else:
        data = tbl_product.objects.get(product_id=a)
        if request.POST.get("photo")=="": 
            if request.method == 'POST':
                data.product_id=request.POST.get("product_id")
                data.category_id_id=request.POST.get("category_id")
                data.shope_id_id=request.POST.get("shop_id")
                data.product_name=request.POST.get("product_name")
                data.price=request.POST.get("price")
                data.description=request.POST.get("description")
                data.stock=request.POST.get("stock")

                data.save()
                return redirect('/updateviewproduct')
        else:
            if request.method == 'POST':
                data.product_id=request.POST.get("product_id")
                data.category_id_id=request.POST.get("category_id")
                data.shope_id_id=request.POST.get("shop_id")
                data.product_name=request.POST.get("product_name")
                data.price=request.POST.get("price")
                data.description=request.POST.get("description")
                data.stock=request.POST.get("stock")

                Photo = request.FILES['photo']
                fs = FileSystemStorage()
                filename = fs.save(Photo.name, Photo) 
                uploaded_file_url = fs.url(filename)
                data.photo=uploaded_file_url
        
                data.save()
                return redirect('/updateviewproduct')
        


def deleteproduct(request):
    if 'shope' not in request.session:
        return render(request,"home.html")
    else:
        username=request.session['shope']
        data2=tbl_shope.objects.get(username=username)
        data=tbl_product.objects.filter(shope_id_id=data2.shope_id)
        return render(request,'deleteproduct.html',{"g":data})

def deleteactionproduct(request,a):
    if 'shope' not in request.session:
        return render(request,"home.html")
    else:
        data=tbl_product.objects.get(product_id=a)
        data.delete()
        return redirect("/deleteproduct")



def viewproduct(request,id):
    data= tbl_product.objects.filter(category_id_id=id)
    return render(request,'viewproduct.html',{"g":data})



def coustomermenu(request):
    if 'coustomer' not in request.session:
        return render(request,"home.html")
    else:
        return render(request,'coustomermenubar.html')

def coustomerviewcategory(request):
    if 'coustomer' not in request.session:
        return render(request,"home.html")
    else:
        data= tbl_category.objects.all()
        return render(request,'coustomerviewcategory.html',{"g":data})


def coustomerviewproduct(request,id):
    if 'coustomer' not in request.session:
        return render(request,"home.html")
    else:
        data= tbl_product.objects.filter(category_id_id=id)
        return render(request,'coustomerviewproduct.html',{"g":data})


def coustomerregistration(request):
    return render(request,'coustomerregistration.html')


def actioncoustomerregistration(request):
    data=idgen.objects.get(id=1)
    f=int(data.coustomerid)
    f=f+1
    f1="Coustomer"+str(f)
    data = tbl_coustomer()
    data.coustomer_id=f1
    data.coustomer_name=request.POST.get("coustomer_name")
    data.adress=request.POST.get("adress")
    data.pincode=request.POST.get("pincode")
    data.phone_number=request.POST.get("phone_number")
    data.email=request.POST.get("email")
    data.username=request.POST.get("user_id")
    data.save()
    data2 = tbl_login()
    data2.username=request.POST.get("user_id")
    data2.password=request.POST.get("password")
    data2.category = "coustomer"
    data2.hint=request.POST.get("hint")
    data2.save()
    data1=idgen.objects.get(id=1)
    data1.coustomerid=f
    data1.save()
    send_mail('Your User ID and Password','Dear coustomer '+'\n\n'+'I am writing this email to provide you with your user ID and password to access Grace Times And Eletronics. Your login credentials are as follows'+'\n'+'User ID: '+request.POST.get('user_id')+'\n'+'Password:  '+request.POST.get('password')+'\n'+'Please keep your login details confidential and do not share them with anyone. We recommend that you change your password periodically for added security.'+'\n'+'If you encounter any issues while logging in or have forgotten your password, please click on the "Forgot Password" link on the login page to reset your password.'+'\n'+'We hope that you have a pleasant experience using our platform. If you have any questions or concerns, please do not hesitate to contact us at coustomer@gmail.com'+'\n'+'Thank you for choosing Grace Times and Eletronics. We look forward to serving you.'+'\n'+'Best regards'+'\n'+'Graceson','from@example.co',[request.POST.get('email'),])
    return render(request,"coustomerregistration.html")

def coustomerlogin(request):
    return render(request,'login.html')


def coustomerhome(request):
    if 'coustomer' not in request.session:
        return render(request,"home.html")
    else:
        data= tbl_product.objects.all()
        return render(request,'coustomerhome.html',{'g':data})


def adminhome(request):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        return render(request,'adminhome.html')


def shopehome(request):
    if 'shope' not in request.session:
        return render(request,"home.html")
    else:
        username=request.session['shope']
        data2=tbl_shope.objects.get(username=username)
        data=tbl_product.objects.filter(shope_id_id=data2.shope_id)
        return render(request,'shopehome.html',{'g':data})

def loginaction(request):
    data=tbl_login.objects.all()
    if request.method == 'POST':
        
        u=request.POST.get('user_id')  
        p=request.POST.get('password')
        flag=0
        for da in data:
            if u==da.username and p==da.password:
                type=da.category
                flag=1
                if type=="admin":
                    request.session['uid']=u
                    return redirect('/adminhome')
                elif type=="shope":
                    request.session['shope']=u
                    return redirect('/shopehome')
                elif type=="coustomer":
                    request.session['coustomer']=u
                    return redirect('/coustomerhome')
                elif type=="deliveryagent":
                    request.session['deliveryagent']=u
                    return redirect('/agenthome')
                
                else:
                    return render(request,"contact.html")  
                    #return HttpResponse("Invalid")
        if flag==0:
            return render(request,"login.html",{'s1':1})
            # return render(request,"coustomerregistration.html")
        
def forgetpassword(request):
    return render(request,"forgetpassword.html")

def forgetpasswordaction(request):
    hint=request.POST.get("hint")
    data=tbl_login.objects.get(hint=hint)
    return render(request,"forgetpasswordchange.html",{'data':data})

def forgetpasswordchange(request,id):
    data=tbl_login.objects.get(username=id)
    data.password=request.POST.get("password")
    data.save()
    return redirect('/coustomerlogin')


def productdetails(request,id):
    if 'coustomer' not in request.session:
        return render(request,"home.html")
    else:
        data=tbl_product.objects.get(product_id=id)
        return render(request,'productdetails.html',{'data':data})

def orderdetails(request,id):
    if 'coustomer' not in request.session:
        return render(request,"home.html")
    else:
        data1=datetime.datetime.now().strftime ("%Y-%m-%d")
        data=tbl_product.objects.get(product_id=id)
        return render(request,'orderform.html',{'g':data,'date':data1})

def order(request):
    if 'coustomer' not in request.session:
        return render(request,"home.html")
    else:
        data5=tbl_product.objects.get(product_id=request.POST.get("product_id"))
        stock=int(data5.stock)
        if (stock < int(request.POST.get("quandity"))):
            return HttpResponse('stock not avilable')
        else:
            data=idgen.objects.get(id=1)
            f=int(data.orderid)
            f=f+1
            f1="Order"+str(f)
            data = tbl_order()
            data.order_id=f1
            data.product_id_id=request.POST.get("product_id")
            data.order_date=request.POST.get("oder_date")
            data.oder_quandity=request.POST.get("quandity")
            data.total_amount=request.POST.get("total")
            
            data10=tbl_coustomer.objects.get(username=request.session['coustomer'])
            data.coustomer_id_id=data10.coustomer_id
            data.status="pending"
            data.delivery_adress=request.POST.get("adress")
            data.save()
        
            data1=idgen.objects.get(id=1)
            data1.orderid=f
            data1.save()
            return render(request,"coustomerviewproduct.html")


def shopeorder(request):
    if 'shope' not in request.session:
        return render(request,"home.html")
    else:
        username=request.session['shope']
        data2=tbl_shope.objects.get(username=username)
        data=tbl_product.objects.filter(shope_id_id=data2.shope_id)
        return render(request,'shopeorder.html',{'g':data})


def shopevieworder(request,id):
    if 'shope' not in request.session:
        return render(request,"home.html")
    else:
        data= tbl_order.objects.filter(product_id_id=id).filter(status="pending")
        return render(request,'vieworder.html',{"g":data})

def coustomerpostreview(request,id):
    if 'coustomer' not in request.session:
        return render(request,"home.html")
    else:
        data=tbl_product.objects.get(product_id=id)
        id1=request.session['coustomer']
        data2= tbl_coustomer.objects.get(username=id1)
        data1=datetime.datetime.now().strftime ("%Y-%m-%d")
        return render(request,'coustomerpostreview.html',{'g':data,"date":data1,"f":data2})


def actionreview(request):
    if 'coustomer' not in request.session:
        return render(request,"home.html")
    else:
        data=idgen.objects.get(id=1)
        f=int(data.reviewid)
        f=f+1
        f1="Review"+str(f)
        data = tbl_review()
        data.review_id=f1
        data.product_id_id=request.POST.get("product_id")
        data.review_date=request.POST.get("review_date")
        data.coustomer_id_id=request.POST.get("coustomer_id")
        data.review=request.POST.get("review")
        data.save()
    
        data1=idgen.objects.get(id=1)
        data1.reviewid=f
        data1.save()
        data=tbl_product.objects.get(product_id=request.POST.get("product_id"))
        return render(request,"productdetails.html",{'data':data})



def coustomerviewreview(request,id):
    if 'coustomer' not in request.session:
        return render(request,"home.html")
    else:
        data= tbl_review.objects.filter(product_id_id=id)
        return render (request,'coustomerviewreview.html',{"g":data})

def rejectorder(request,id):
    if 'shope' not in request.session:
        return render(request,"home.html")
    else:
        data = tbl_order.objects.get(order_id=id)
        data.status="rejected"
        data.save()
        send_mail('Order Rejection Notification','Dear Customer ,'+'\n\n'+'We regret to inform you that your recent order '+data.order_id +' has been rejected. We understand that this news may come as a disappointment to you, and we apologize for any inconvenience caused.'+'\n'+'Upon review, we found that the order did not meet our internal standards or requirements. Due to this, we were unable to proceed with the order, and it has been rejected.'+'\n'+'We would like to assure you that we take our customers orders very seriously, and we make every effort to ensure that they are processed efficiently and accurately. Unfortunately, in this case, we were unable to fulfill your order due to the reasons mentioned above.'+data.order_id+'\n'+'Order Date: '+data.order_date+'\n'+'Delivery Address: '+'\n'+'If you have any questions or concerns regarding this matter, please feel free to contact our customer support team at contact@gmail.com. We will be happy to assist you and address any queries that you may have.'+'\n'+'We value your business and appreciate your understanding in this matter. We hope to continue serving you in the future and look forward to the opportunity to provide you with better service.'+'\n'+'Thank you for your cooperation and support.'+'\n'+'Sincerely,'+'\n'+'Graceson Joseph'+'\n'+'Grace times ','from@example.co',[data.coustomer_id.email,])
        return redirect('/shopeorder')

def acceptorder(request,id):
    if 'shope' not in request.session:
        return render(request,"home.html")
    else:
        data = tbl_order.objects.get(order_id=id)
        data.status="accepted"
        data.save()
        data10=tbl_product.objects.get(product_id=data.product_id_id)
        stock=data10.stock
        newstock=int(stock)-int(data.oder_quandity)
        data10.stock=newstock
        data10.save()
        
        send_mail('Order Confirmation - Your Order Has Been Accepted','Dear Customer Name,'+'\n\n'+'We are delighted to inform you that your recent order has been accepted and is being processed. Thank you for choosing to do business with us.'+'\n'+'Your order details are as follows:'+'\n'+'Order Number: '+data.order_id+'\n'+'Order Date: '+data.order_date+'\n'+'Delivery Address: '+data.delivery_adress+'\n'+'Please note that the estimated delivery date for your order is by today evening. We will send you a tracking number as soon as your order is shipped.'+'\n'+'If you have any questions or concerns about your order, please feel free to contact us at contact@gmail.com.'+'\n'+'Once again, thank you for your order. We appreciate your business and look forward to serving you in the future.'+'\n'+'Best regards,'+'\n'+'Graceson Joseph'+'\n'+'Grace times ','from@example.co',[data.coustomer_id.email,])
        return redirect('/shopeorder')

def shopereview(request):
    if 'shope' not in request.session:
        return render(request,"home.html")
    else:
        username=request.session['shope']
        data2=tbl_shope.objects.get(username=username)
        data=tbl_product.objects.filter(shope_id_id=data2.shope_id)
        return render(request,'shopereview.html',{'g':data})


def shopeviewreview(request,id):
    if 'shope' not in request.session:
        return render(request,"home.html")
    else:
        data= tbl_review.objects.filter(product_id_id=id)
        return render(request,'shopeviewreview.html',{"g":data})
    
def coustomervieworder(request):
    if 'coustomer' not in request.session:
        return render(request,"home.html")
    else:
        return render(request,'coustomerorder.html')

def coustomerviewpendingorder(request):
    if 'coustomer' not in request.session:
        return render(request,"home.html")
    else:
        username=request.session['coustomer']
        data2=tbl_coustomer.objects.get(username=username)
        data=tbl_order.objects.filter(coustomer_id_id=data2).filter(status="pending")
        return render(request,'coustomerviewpendingorder.html',{'g':data})

def coustomerviewonthewayorder(request):
    if 'coustomer' not in request.session:
        return render(request,"home.html")
    else:
        username=request.session['coustomer']
        data2=tbl_coustomer.objects.get(username=username)
        data=tbl_order.objects.filter(coustomer_id_id=data2).filter(status="On the way")
        return render(request,'coustomerviewonthewayorder.html',{'g':data})

def coustomerviewacceptedorders(request):
    if 'coustomer' not in request.session:
        return render(request,"home.html")
    else:
        username=request.session['coustomer']
        data2=tbl_coustomer.objects.get(username=username)
        data=tbl_order.objects.filter(coustomer_id_id=data2).filter(status="accepted")
        return render(request,'coustomerviewacceptedorders.html',{'g':data})


def coustomerrejectvieworder(request):
    if 'coustomer' not in request.session:
        return render(request,"home.html")
    else:
        username=request.session['coustomer']
        data2=tbl_coustomer.objects.get(username=username)
        data=tbl_order.objects.filter(coustomer_id_id=data2).filter(status="rejected")
        return render(request,'coustomerrejectvieworder.html',{'g':data})

def coustomerdelivredvieworder(request):
    if 'coustomer' not in request.session:
        return render(request,"home.html")
    else:
        username=request.session['coustomer']
        data2=tbl_coustomer.objects.get(username=username)
        data=tbl_order.objects.filter(coustomer_id_id=data2).filter(status="Delivred")
        return render(request,'coustomerdelivredvieworder.html',{'g':data})


def coustomerviewreviewdelete(request):
    if 'coustomer' not in request.session:
        return render(request,"home.html")
    else:
        username=request.session['coustomer']
        data2=tbl_coustomer.objects.get(username=username)
        data=tbl_review.objects.filter(coustomer_id_id=data2)
        return render(request,'coustomerviewreviewdelete.html',{'g':data})


def deletecoustomerreview(request,id):
    if 'coustomer' not in request.session:
        return render(request,"home.html")
    else:
        data=tbl_review.objects.get(review_id=id)
        data.delete()
        return redirect("/coustomerviewreviewdelete")


def viewreview(request,id):
    data= tbl_review.objects.filter(product_id_id=id)
    return render (request,'viewreview.html',{"g":data})


def adminviewproduct(request):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        data= tbl_product.objects.all()
        return render(request,'adminviewproduct.html',{"g":data})

def adminviewreview(request,id):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        data= tbl_review.objects.filter(product_id_id=id)
        return render (request,'adminviewreview.html',{"g":data})


def adminviewreport(request):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        data= tbl_product.objects.all()
        return render(request,'adminviewreport.html',{"g":data})

def adminactionviewreport(request,id):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        data= tbl_order.objects.filter(product_id_id=id)
        return render (request,'adminactionviewreport.html',{"g":data})


def deliveryagentmenubar(request):
    return render(request,'deliveryagentmenubar.html')


def agenthome(request):
    if 'deliveryagent' not in request.session:
        return render(request,"home.html")
    else:
        return render(request,'agenthome.html')

def adddeliveryagent(request):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        return render(request,'adddeliveryagent.html')


def actionaddagent(request):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        count =tbl_deliveryagent.objects.filter(username=request.POST.get("user_id")).count()
        if count==0:
            data=idgen.objects.get(id=1)
            f=int(data.agentid)
            f=f+1
            f1="Agent"+str(f)
            data = tbl_deliveryagent()
            data.agent_id=f1
            data.agent_name=request.POST.get("agent_name")
            data.phone_number=request.POST.get("phone_number")
            data.email=request.POST.get("email")
            data.username=request.POST.get("user_id")
            data.save()

            data2 = tbl_login()
            data2.username=request.POST.get("user_id")
            data2.password=request.POST.get("password")
            data2.category = "deliveryagent"
            data2.save()
            
            data1=idgen.objects.get(id=1)
            data1.agentid=f
            data1.save()
            send_mail('Your User ID and Password','Dear coustomer '+'\n\n'+'I am writing this email to provide you with your user ID and password to access Grace Times And Eletronics. Your login credentials are as follows'+'\n'+'User ID: '+request.POST.get('user_id')+'\n'+'Password:  '+request.POST.get('password')+'\n'+'Please keep your login details confidential and do not share them with anyone. We recommend that you change your password periodically for added security.'+'\n'+'If you encounter any issues while logging in or have forgotten your password, please click on the "Forgot Password" link on the login page to reset your password.'+'\n'+'We hope that you have a pleasant experience using our platform. If you have any questions or concerns, please do not hesitate to contact us at coustomer@gmail.com'+'\n'+'Thank you for choosing Grace Times and Eletronics. We look forward to serving you.'+'\n'+'Best regards'+'\n'+'Graceson','from@example.co',[request.POST.get('email'),])
            return render(request,"adddeliveryagent.html")
        else:
            return HttpResponse("user already exist.............")
        
def updateviewdeliveryagent(request):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        data=tbl_deliveryagent.objects.all()
        return render(request,'updateviewdeliveryagent.html',{"g":data})

def updatedeliveryagent(request,a):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        data=tbl_deliveryagent.objects.get(agent_id=a)
        return render(request,'updatedeliveryagent.html',{"g":data})

def updateactiondeliveryagent(request,a):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        data = tbl_deliveryagent.objects.get(agent_id=a)
        if request.method == 'POST':
            data.agent_id=request.POST.get("agent_id")
            data.agent_name=request.POST.get("agent_name")
            data.phone_number=request.POST.get("phone_number")
            data.email=request.POST.get("email")
        
        
            data.save()
            return redirect('/updateviewdeliveryagent')
        
def devileryagentviewdelete(request):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        data= tbl_deliveryagent.objects.all()
        return render(request,'devileryagentviewdelete.html',{"g":data})
        
def deleteactiondeliveryagent(request,a):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        data=tbl_deliveryagent.objects.get(agent_id=a)
        data.delete()
        data2=tbl_login.objects.get(username=data.username)
        data2.delete()
        return redirect("/devileryagentviewdelete")


def deliveryagentvieworder(request):
    if 'deliveryagent' not in request.session:
        return render(request,"home.html")
    else:
        data= tbl_order.objects.filter(status="accepted")
        return render(request,'deliveryagentvieworder.html',{"g":data})

def deliveryagentacceptorder(request,id):
    if 'deliveryagent' not in request.session:
        return render(request,"home.html")
    else:
        data = tbl_order.objects.get(order_id=id)
        data.status="On the way"
        data.save()
        send_mail(' Your Order is On the Way!','Dear Valued Customer,'+'\n\n'+'We are excited to inform you that your order is on its way! Our team has carefully processed and packed your items, and they are now being shipped directly to you.'+'\n'+'We understand how important it is to receive your order in a timely and efficient manner, which is why we have selected the best shipping option to ensure a quick and secure delivery. You can expect to receive your order within the estimated timeframe provided at checkout.'+'\n'+'Thank you for choosing us for your shopping needs. We hope that you will be satisfied with your purchase and that you will continue to shop with us in the future. If you have any questions or concerns about your order, please do not hesitate to reach out to our customer service team.'+'\n'+'We appreciate your business and look forward to serving you again soon.'+'\n'+'Best regards, '+'\n\n'+'Graceson Joseph'+'\n'+'Grace times ','from@example.co',[data.coustomer_id.email,])
        return redirect('/deliveryagentvieworder')

def deliveryagentdelivered(request):
    if 'deliveryagent' not in request.session:
        return render(request,"home.html")
    else:
        data= tbl_order.objects.filter(status="On the way")
        return render(request,'deliveryagentdelivered.html',{"g":data})

def actiondeliveryagentdelivered(request,id):
    if 'deliveryagent' not in request.session:
        return render(request,"home.html")
    else:
        data = tbl_order.objects.get(order_id=id)
        data.status="Delivred"
        data.save()
        send_mail('Your Order Has Been Delivered','Dear Customer ,'+'\n\n'+'We are writing to inform you that your order has been successfully delivered to the address provided during checkout. We hope that you are pleased with your purchase and that it meets your expectations.'+' If you have any questions or concerns regarding your order, please do not hesitate to contact our customer service team by replying to this email. We are always happy to assist you in any way we can.'+'\n'+'Thank you for choosing our company for your purchase. We appreciate your business and look forward to serving you again in the future.'+'\n'+'Best regards,'+'\n'+'Graceson Joseph'+'\n'+'Grace times ','from@example.co',[data.coustomer_id.email,])
        return redirect('/deliveryagentdelivered')


def adminlogout(request):
    if 'uid' not in request.session:
        return render(request,"home.html")
    else:
        del request.session['uid']
        return render(request,"home.html")

def shopelogout(request):
    if 'shope' not in request.session:
        return render(request,"home.html")
    else:
        del request.session['shope']
        return render(request,"home.html")

def coustomerlogout(request):
    if 'coustomer' not in request.session:
        return render(request,"home.html")
    else:
        del request.session['coustomer']
        return render(request,"home.html")

def deliveryagentlogout(request):
    if 'deliveryagent' not in request.session:
        return render(request,"home.html")
    else:
        del request.session['deliveryagent']
        return render(request,"home.html")






# Create your views here.

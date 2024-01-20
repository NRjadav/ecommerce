from django.shortcuts import render,redirect
from .models import *
# Create your views here.


def index(request):
    if "email" in request.session:
        mid=main_category.objects.all()
        uid=user.objects.get(email=request.session['email'])
        c_count=add_cart.objects.filter(user=uid).count()
        
        contaxt={
            "mid":mid,
            "c_count":c_count,
        }
        return render(request,"index.html",contaxt)
    else:

        return render(request,"login.html")

def cart(request):
    if "email" in request.session:
        mid=main_category.objects.all()
        
        uid=user.objects.get(email=request.session['email'])
        print(uid)
        aid=add_cart.objects.filter(user=uid)
        print(aid)
        c_count=add_cart.objects.all().count()
        
        l1=[]
        sub_total=0
        total=0
        for i in aid:
            l1.append(i.total_price)
        sub_total=sum(l1)
        total=sub_total+10    
        contaxt={
            "mid":mid,
            "aid":aid,
            "sub_total":sub_total,
            "total":total,
            "c_count":c_count,
        }
        return render(request,"cart.html",contaxt)
    else:
        return render(request,"login.html")

def checkout(request):
    if "email" in request.session:
        uid=user.objects.get(email=request.session['email'])
        print(uid)
        mid=main_category.objects.all()
        c_count=add_cart.objects.filter(user=uid).count()
        aid=add_cart.objects.filter(user=uid)
        if request.method == "POST":
            first_name= request.POST['first_name']
            last_name=request.POST['last_name']
            email=request.POST['email']
            mobile_no=request.POST['mobile_no']
            address_line=request.POST['address_line']
            country=request.POST['country']
            city=request.POST['city']
            state=request.POST['state']
            zip_code=request.POST['zip_code']
            print("first_name", first_name)
            billing_details.objects.create(first_name=first_name,
            last_name=last_name,email=email,mobile_no=int(mobile_no),
            address_line=address_line,country=country,city=city,
            state=state,zipcode=zip_code)
        l1=[]
        sub_total=0
        total=0
        for i in aid:
            l1.append(i.total_price)
        sub_total=sum(l1)
        total=sub_total+10  
        contaxt={
            "mid":mid,
            "c_count":c_count,
            "aid": aid,
            "sub_total":sub_total,
            
        
        }
        return render(request,"checkout.html", contaxt)
    else:
        return render(request,"login.html")

def contact(request):
    if "email" in request.session:
        mid=main_category.objects.all()
        c_count=add_cart.objects.all().count()
        if request.method == "POST":
            name= request.POST['name']
            email=request.POST['email']
            subject=request.POST['subject']
            message=request.POST['message']
            contact_info.objects.create(name=name,email=email,subject=subject,message=message)
            contaxt={
                "mid":mid,
                "c_count":c_count,
                "name": name, 
                "email": email, 
                "subject": subject, 
                "message": message, 
            } 
            return render(request,"contact.html", contaxt)
        else:
            return render(request,"contact.html")

    else:
        return render(request,"login.html")

def detail(request):
    if "email" in request.session:
        mid=main_category.objects.all()
        c_count=add_cart.objects.all().count()
        contaxt={
            "mid":mid,
            "c_count":c_count,
        } 
        return render(request,"detail.html", contaxt)
    else:
        return render(request,"login.html")

def shop(request):
    if "email" in request.session:
        mid=main_category.objects.all()
        product_show= product.objects.all()
        pid=price.objects.all()
        cid=color.objects.all()
        c_id=request.GET.get("c_id")
        p_id=request.GET.get("p_id")
        c_count=add_cart.objects.all().count()
        pl=request.GET.get("lth")
        print(pl)
        print(p_id)

        if p_id:
            product_show=product.objects.filter(price1=p_id)
        elif pl=="lth":
            product_show=product.objects.order_by('price')
        elif pl=="htl":
            product_show=product.objects.order_by('-price')   
        elif pl=="atz":
            product_show=product.objects.order_by('name')   
        elif pl=="zta":
            product_show=product.objects.order_by('-name')   
        elif c_id:
            product_show=product.objects.filter(color=c_id)

        else:
            product_show= product.objects.all()


        contaxt={
            "mid":mid,
            "cid":cid,
            "pid":pid,
            "product_show": product_show,
            "c_count":c_count,
        } 
        return render(request,"shop.html", contaxt)
    else:
        return render(request,"login.html")

def login(request):
    if "email" in request.session:
        return redirect("index")
    else:

        if request.POST:
            email=request.POST['email']
            password=request.POST['password']

            try:
                uid=user.objects.get(email=email)
                print(uid)
                
                if uid.email==email:
                    if uid.password==password:
                        request.session['email']=uid.email
                        return redirect("index")
                    else:
                        return render(request,"login.html")
                else:
                    return render(request,"login.html")
            except:
                return render(request,"login.html")
                    
        else:
            return render(request,"login.html")

def register(request):
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password1']
        c_password=request.POST['password']
        # print(name,email,password)
        if password==c_password:
            user.objects.create(name=name,email=email,password=password)
            return redirect("login")
        else:
            contaxt={
                "msg":"invalid password"
            }
            return render(request,"register.html",contaxt)

    else:
        return render(request,"register.html")
    
def logout(request):
    del request.session['email']    
    return redirect("login")


def search(request):
    sid=request.GET.get('search')
    print(sid)
    product_show=product.objects.filter(name__icontains=sid)
    print(product_show)
    contaxt={
            "product_show": product_show
        } 
    return render(request,"shop.html", contaxt)

def detail1(request,id):
    if "email" in request.session:
        mid=main_category.objects.all()
        s_product=product.objects.get(id=id)
        contaxt={
            "mid":mid,
            "s_product":s_product,
        } 
        return render(request,"detail.html", contaxt)
    else:
        return render(request,"login.html")
    

def add_to_cart(request,id):
    s_product=product.objects.get(id=id)
    uid=user.objects.get(email=request.session['email'])
    cid1=add_cart.objects.filter(user=uid,product=s_product).exists()
    print(cid1)
    if cid1:
        cid=add_cart.objects.get(product=s_product)
        cid.qty+=1
        cid.total_price=cid.price*cid.qty
        cid.save()
        return redirect('cart')

    else:

        add_cart.objects.create(user=uid,product=s_product,name=s_product.name,price=s_product.price,qty=1,total_price=s_product.price)
        return redirect('cart')

def cart_plus(request,id):
    cid=add_cart.objects.get(id=id)
    cid.qty+=1
    cid.total_price=cid.price*cid.qty
    cid.save()
    return redirect('cart')

def cart_minus(request,id):
    cid=add_cart.objects.get(id=id)
    cid.qty-=1
    cid.total_price=cid.price*cid.qty
    cid.save()
    if cid.qty==0:
        cid.delete()
    
    return redirect('cart')


def cart_remove(request,id):
    cid=add_cart.objects.get(id=id)
    cid.delete()
        
    return redirect('cart')
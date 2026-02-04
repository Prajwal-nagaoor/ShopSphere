from django.shortcuts import render, redirect
from .models import productsmodel,category, cartmodel
from django.db.models import Q
# Create your views here.

def hoem(request):
    
    cart_count = cartmodel.objects.filter(host = request.user).count() if request.user.is_authenticated else 0
   

    trend = False
    offer = False
    if 'q' in request.GET:
        q = request.GET['q']
        try:
            cat = category.objects.get(category_name__contains = q)
            all_product=productsmodel.objects.filter(Q(product_name__contains=q)|Q(product_desc__contains=q)|Q(product_category=cat))
        except:
            all_product= productsmodel.objects.filter(Q(Q(product_name__contains=q)|Q(product_desc__contains=q)))
            print()
    elif 'cat'in request.GET:
        cat = category.objects.get(category_name__contains = request.GET['cat'])
        all_product=productsmodel.objects.filter(Q(product_category=cat))
    elif 'trending'in request.GET:
        all_product=productsmodel.objects.filter(trending = True)
        trend = True
    elif 'offer'in request.GET:
        all_product=productsmodel.objects.filter(offer = True)
        offer = True
    else:
        all_product = productsmodel.objects.all()
    all_category=category.objects.all()
    context = {
        'data':all_product,
        'all_category':all_category,
        'trend':trend,
        'cart_count':cart_count
        
    }
    
    return render(request, 'home.html', context)


from django.shortcuts import get_object_or_404

def add_product(request):
    all_category = category.objects.all()

    if request.method == 'POST':
        product_category = request.POST.get('category_attr')
        product_type = request.POST.get('product_type')
        product_desc = request.POST.get('product_desc')
        product_price = request.POST.get('product_price')
        product_image = request.FILES.get('product_image', 'default.png')

        pk_cat_model = get_object_or_404(
            category,
            category_name=product_category
        )

        productsmodel.objects.create(
            product_category=pk_cat_model,
            product_name=product_type,
            product_desc=product_desc,
            product_price=product_price,
            product_image=product_image,
        )

        return redirect('home')

    return render(request, 'add_product.html', {
        'all_category': all_category
    })
def pro_details(request,pk):
    pro = productsmodel.objects.get(id = pk)
    return render(request, 'pro_details.html', {'product':pro})
def add_cart(request, pk):
    pro = productsmodel.objects.get(id = pk)

    try:
        c = cartmodel.objects.get(
            Q(product_name=pro.product_name) &
            Q(host=request.user)
        )
        c.quantity += 1
        c.price = c.product_price * c.quantity  
        c.save()

    except cartmodel.DoesNotExist:
        cartmodel.objects.create(
            product_category=pro.product_category,
            product_name=pro.product_name,
            product_desc=pro.product_desc,
            product_price=pro.product_price,
            product_image = pro.product_image,
            quantity=1,
            price=pro.product_price,
            host=request.user,
        )

    return redirect('cart')
def cart(request):
    total_price = 0
    cart_count = cartmodel.objects.filter(host = request.user).count()
    cart_product = cartmodel.objects.filter(host=request.user)
    for i in cart_product:
        total_price += i.price 
    print(total_price)
    context = {'cart_product':cart_product, 
               'total_price':total_price,
               'cart':True,
               'cart_count':cart_count}
    return render(request,'cart.html',context)
def cart_increase(request,pk):
    pro = cartmodel.objects.get(id = pk)
    pro.quantity += 1
    pro.save()
    pro.price = pro.product_price * pro.quantity
    pro.save()
    return redirect('cart')
def cart_decrease(request,pk):
    pro = cartmodel.objects.get(id = pk)
    pro.quantity -= 1
    pro.save()
    pro.price = pro.product_price * pro.quantity
    pro.save()
    if pro.quantity == 0:
        pro.quantity = 1
        pro.save()
        pro.price = pro.product_price * pro.quantity
        pro.save()
    return redirect('cart')
def cart_pro_remove(reqeust,pk):
    pro = cartmodel.objects.get(id= pk)
    pro.delete()
    return redirect('cart')

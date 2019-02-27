

# Create your views here.
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.views.generic import View,ListView,DetailView
from .forms import Userform
from django.contrib import auth,messages
from .models import user_table,items_table,CartTable,CategoryTable,Cart, CartItem
from django.contrib.auth.models import User
from django.core.files.storage import  FileSystemStorage
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.urls import reverse


'''class UserSignupView(View):
    form_class = Userform
    template_name='items/signup.html'
    # give blank signup form

    def get(self, request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form,})

    # process form data

    if request.method==
        #form = self.form_class(request.POST)
        #if form.is_valid():
        username=request.POST.get['un']
        email=request.POST.get['em']
        password=request.POST.get['ps']
        User.objects.create_user(username=username, email=email, password=password)
        #form.save()
        tb = user_table(username=username, email=email, password=password)
        tb.save()
        return redirect('login')'''

def UserSignupView(request):
    if request.method =='POST':
        # form = self.form_class(request.POST)
        # if form.is_valid():
        username = request.POST.get('un', '')
        email = request.POST.get('em', '')
        password = request.POST.get('ps', '')
        User.objects.create_user(username=username, email=email, password=password)
        # form.save()
        tb = user_table(username=username, email=email, password=password)
        tb.save()
        return redirect('login')
    return render(request, 'items/signup.html')


class UserLoginView(View):
    login_template = 'items/login.html'
    index_template = 'items/headblock.html'

    def get(self, request):
        return render(request,self.login_template)

    # process form data
    def post(self, request):
        username = request.POST['un']
        password = request.POST['ps']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            u1 = user_table.objects.get(username=username)
            request.session['idd'] = u1.id

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('index')
        else:
            messages.error(request, 'username or password not exist')
        return render(request, self.login_template)


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('index')


def indexview(request):
    # template_name = 'items/index2.html'
    template_name = 'items/headblock.html'
    items_list = items_table.objects.all()
    category_list = CategoryTable.objects.all()
    featured_list = items_table.objects.filter(feature=True)
    discount_list = items_table.objects.filter(~Q(discount=0))
    context={'items_list': items_list,'category_list': category_list, 'featured_list': featured_list,'discount_list': discount_list}
    return render(request, template_name, context)


'''
class IndexView(ListView):
    template_name = 'items/index1.html'

    def get_queryset(self):
        return items_table.objects.all()

    def 
'''
'''
class ProductView(DetailView):
    
    def product_view(self,request,idd):
        model = items_table.objects.get(id=idd)
        context = {'model': model}
        template_name = 'items/product.html'
      return render(request, template_name=template_name, context)
    
    
    def render_to_response(self, context, **response_kwargs):
        return {}
'''


def productview1(request,idd):
    items_list = items_table.objects.all()
    category_list = CategoryTable.objects.all()
    featured_list = items_table.objects.filter(feature=True)
    discount_list = items_table.objects.filter(~Q(discount=0))
    model = items_table.objects.get(id=idd)
    context = {'model': model,'items_list': items_list, 'category_list':category_list, 'featured_list': featured_list, 'discount_list': discount_list}
    template_name = 'items/product.html'
    return render(request, template_name,context)

@login_required(login_url='login')
def cart1(request, cartid):
    quantity = request.POST.get('quantity', 0)
    model = items_table.objects.get(id=cartid)
    context = {'model': model, 'cartid': cartid}
    template_name = 'items/cart.html'
    if request.method == 'POST':
        if request.user.is_authenticated:
            model = items_table.objects.get(id=cartid)
            uid = request.user.id
            itemid = model.id
            itemprice = model.price
            tb = CartTable(uid=uid, itemprice=itemprice, itemid=itemid, quantity=quantity)
            tb.save()
            total_price = int(itemprice)*int(quantity)
            context_cart = {'model': model, 'cartid': cartid, 'quantity': quantity, 'total_price':total_price}
            return render(request, 'items/cart.html', context_cart)
        else:
            return redirect('login')
    return render(request, template_name, context)


def shop(request, idd):
    category = CategoryTable.objects.filter(id=idd)
    items = items_table.objects.filter(category=category[0])
    context = {'items': items, 'category': category[0]}
    return render(request, 'items/shop.html',context)


def blogview(request):
    return render(request,'items/blog.html')


def singleblog(request):
    return render(request, 'items/blog_single.html')


def cart(request):
    return render(request,'items/cart.html')


def contact(request):
    return render(request, 'items/contact.html')


def regular(request):
    return render(request, 'items/regular.html')


def newcart(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None

    if the_id:
        cart = Cart.objects.get(id= the_id)
        context = {'cart': cart}
    else:
        empty_message = 'Your cart is empty,please keep shopping.'
        context = {'empty':True, 'empty_message':empty_message}
    template = 'items/newcart.html'
    return render(request, template, context)


def add_to_cart(request, idd):
    request.session.set_expiry(120000)
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
    cart = Cart.objects.get(id=the_id)

    try:
        product = items_table.objects.get(id=idd)
    except items_table.DoesNotExist:
        pass
    except:
        pass
    if request.method == "POST":
        qty = request.POST.get('qty',1)

        cart_item = CartItem.objects.create(cart=cart,item=product)
        cart_item.quantity = qty
        cart_item.save()
        print(cart.cartitem_set.count())
        print(cart.cartitem_set)
        if cart_item in cart.cartitem_set.all():
            print('qwertyuiop')
            cart.cartitem_set.add(cart_item)
            print(cart.cartitem_set)
        else:
            pass

        new_total = 0.00
        for item in cart.cartitem_set.all():
            print(item.item.discountprice)
            print(item.quantity)
            line_total = float(item.item.discountprice) * item.quantity
            new_total += line_total
            print(new_total)

        request.session['items_total'] = cart.cartitem_set.count()
        cart.total = new_total
        cart.save()
        return HttpResponseRedirect(reverse('newcart'))
    else:
        return HttpResponseRedirect(reverse('newcart'))

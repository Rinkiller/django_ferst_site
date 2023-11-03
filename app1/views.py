import logging
import datetime
import random
from .forms import ProductForm, СlientForm, OrderForm, Client_id
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import SaveCoin,Product, Сlient, Order
from django.core.files.storage import FileSystemStorage

logger = logging.getLogger(__name__)
# Create your views here.
def index(request):
    return render(request, "app1/index.html")

def about(request):
    return render(request, "app1/About_us.html")

def coin(request):
    rnd_coin = random.choice(["Орел","Решка"])
    save_coin = SaveCoin(coin_var=rnd_coin)
    save_coin.save()
    logger.info(f'Coin is {rnd_coin}')
    return HttpResponse(rnd_coin)

def get_all_coin(request):
    return HttpResponse(SaveCoin.get_n(4))

def get_user_products(request,user_id,days): 
    client = get_object_or_404(Сlient, pk=user_id)
    orders = Order.objects.filter(client=client).order_by('-id')
    result = []
    for order in orders:
        if order.date > (datetime.datetime.now() - datetime.timedelta(days=days)).replace(tzinfo=datetime.timezone.utc):
            if order.product.name is not result: result.append(order.product.name)
    context = {"name": client.name,"products":result,"days":days}
    return render(request, "app1/get_user_prod.html", context)


def productaddform(request):
    message = "Введите данные нового продукта"
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        message = "Введенные данные ошибочны"
        if form.is_valid():
            name = form.cleaned_data['name']
            title = form.cleaned_data['title']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            image = form.cleaned_data['image']
            product = Product(name=name, title=title, price=price, quantity=quantity, image = image)
            product.save()
            fs = FileSystemStorage()
            fs.save(product.image.name, product.image)
            logger.info(f'Получили product {name=}, {title=}, {quantity=}, {image.name=}.')
            message = "Новый продукт успешно сохранен."
    else:
        form = ProductForm()
    return render(request, 'app1/add_new_product.html', {'form':form,'message':message,'title':"продукта"})

def clientaddform(request):
    message = "Введите данные нового клиента"
    if request.method == 'POST':
        form = СlientForm(request.POST)
        message = "Введенные данные ошибочны"
        if form.is_valid():
            name = form.cleaned_data['name']
            mail = form.cleaned_data['mail']
            telNumber = form.cleaned_data['telNumber']
            adress = form.cleaned_data['adress']
            client = Сlient(name = name, mail = mail, telNumber = telNumber, adress = adress)
            client.save()
            logger.info(f'Получили client {name=}, {mail=}, {telNumber=}, {adress=}.')
            message = "Новый клиент успешно сохранен."
    else:
        form = СlientForm()
    return render(request, 'app1/add_new_product.html', {'form':form,'message':message,'title':"клиента"})

def orderaddform(request):
    message = "Введите данные нового заказа"
    if request.method == 'POST':
        form = OrderForm(request.POST)
        message = "Введенные данные ошибочны"
        if form.is_valid():
            client_name = form.cleaned_data['name']
            product_id = form.cleaned_data['product_id']
            total_order = form.cleaned_data['total_order']
            client = Сlient.objects.filter(name=client_name)[0]      
            product = get_object_or_404(Product, pk = product_id)
            order = Order(client = client, product = product, total_order = total_order)
            order.save()
            logger.info(f'Получили order {order=}.')
            message = "Новый заказ успешно сохранен."
    else:
        form = OrderForm()
    return render(request, 'app1/add_new_product.html', {'form':form,'message':message,'title':"клиента"})

def client_orders_form(request):
    message = "Выберите нужного клиента"
    if request.method == 'POST':
        form = Client_id(request.POST)
        message = "Введенные данные ошибочны"
        if form.is_valid():
            client_id = form.cleaned_data['client_id']     
            client = get_object_or_404(Сlient, pk = client_id)
            orders = Order.objects.filter(client=client)
            logger.info(f'Получили orders {orders=} клиента {client}.')
            return render(request, 'app1/get_orders_of_client.html', {'name':client.name,'title':f"Заказы клиента{client.name}",'orders':orders})
    else:
        form = Client_id()
    return render(request, 'app1/add_new_product.html', {'form':form,'message':message,'title':"клиента"})

def get_all_clients_in_db(request):
    clients = Сlient.objects.all()
    return render(request, 'app1/get_all_clients.html', {'title':"Список всех клиентов",'clients':clients})
   
def get_all_products_in_db(request):
    products = Product.objects.all()
    return render(request, 'app1/get_all_product.html', {'title':"Список всех клиентов",'products':products})
   



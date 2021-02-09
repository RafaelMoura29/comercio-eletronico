from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from app.models import Product
from app.models import Cart
from django.http import JsonResponse
from django.utils import timezone

def indexPage(request):
    return render(request, 'app/index.html', {'data': Product.objects.all()})

def productPage(request, pk):
    return render(request, 'app/product.html', {'data': Product.objects.get(pk=pk) })

def purchasePage(request):
    return render(request, 'app/purchase.html', {})

@login_required
def cartPage(request):
    return render(request, 'app/cart.html', {'data': "none"})

@login_required
def cadastroProduto(request):
    return render(request, 'app/cadastroProduto.html', {})

@login_required
def registerProduct(request):
    p = Product(name=request.POST.get('NomeProduto'), price=request.POST.get('Preco'), img_url=request.POST.get('UrlImagem'), description=request.POST.get('Descricao'))
    print(p.save())
    return render(request, 'app/cadastroProduto.html', {})

def clientInformationsPage(request):
    return render(request, 'app/clientInformations.html', {})

@csrf_exempt
@login_required
def addToCart(request, productPk):
    #product = Product.objects.get(pk=productPk)
    #c = Cart(user_fk=request.user, date=timezone.now())
    #print(c.save())
    return JsonResponse(dados, safe=False)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Product
# Create your views here.

def indexPage(request):
    return render(request, 'app/index.html', {'data': Product.objects.all()})

def productPage(request, pk):
    return render(request, 'app/product.html', {'data': Product.objects.get(pk=pk) })

def purchasePage(request):
    return render(request, 'app/purchase.html', {})

@login_required
def cartPage(request):
    return render(request, 'app/cart.html', {})

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


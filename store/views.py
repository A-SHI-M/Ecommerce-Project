from typing import Any
from django import http
from django.shortcuts import render, get_object_or_404, redirect
from store.models import Category, Product , ProductImages, Banner, Review1
from django.views.generic import ListView, DetailView, TemplateView
from account.models import Profile
from notification.notific import SendNotification

class HomeListView(TemplateView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all().order_by('-id')
        banners = Banner.objects.filter(is_active=True).order_by('-id')[0:3]
        """ user = Profile.objects.filter(user=request.user) """

        context = {
            'products': products,
            'banners': banners,
        }
        return render(request, 'store/index.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'post' or request.method == 'POST':
            search_product = request.POST.get('search_product')
            products = Product.objects.filter(name__icontains=search_product).order_by('-id')
            
            

            context = {
                'products': products,
                
                
            }
            return render(request, 'store/index3.html', context)



class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product.html'
    context_object_name = 'item'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_images'] = ProductImages.objects.filter(product=self.object.id)
        context['reviews']        = Review1.objects.filter(product=self.object.id)
        return context
    



def ReviewForm(request, pk):
    item = get_object_or_404(Product, pk=pk)
    user_info = Profile.objects.get(user=request.user)
    context = {
        'item' : item,
        'user_info' : user_info,

    }
    return render(request, 'review.html', context)

def ReviewSub(request, pk):
    if request.user.is_authenticated:
        item = get_object_or_404(Product, pk=pk)
        if request.method == 'post' or request.method == 'POST':
            name = request.POST.get('name')
            title = request.POST.get('title')
            rate = request.POST.get('rating')
            rate = int(rate)
            comment = request.POST.get('review')
        item_review = Review1.objects.get_or_create(product=item, name=name, title=title, rate=rate, comment=comment)
        message = f"You have successfully reviewed a Product"
        SendNotification(request.user, message)
        return redirect('store:index')
    else:
        return redirect('account:login')


 
    
# def product_details(request, pk):
#     item = Product.objects.get(id=pk)
#     context = {
#         'item': item,
#     }
#     return render(request, 'store/product.html', context)

from django.shortcuts import render, get_object_or_404

from phones.models import Phone


def show_catalog(request):
    sort_phone = request.GET.get('sort')
    phone = Phone.objects.all()
    if sort_phone == 'name':
        phone = phone.order_by('name')
    elif sort_phone == 'max_price':
        phone = phone.order_by('-price')
    elif sort_phone == 'min_price':
        phone = phone.order_by('price')
    template = 'catalog.html'
    context = {'phone': phone}
    return render(request, template, context)


def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)

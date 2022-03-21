from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_phones = str(request.GET.get('sort','name'))
    template = 'catalog.html'
    phone_obj = Phone.objects.all()
    pho = [[c.name, c.price, c.image, c.release_date, c.lte_exists,
            c.slug] for c in phone_obj]
    keys_pho = ['name', 'price', 'image', 'release_date', 'lte_exists', 'slug']
    phones = []
    for b in pho:
        lst = {x: y for x, y in zip(keys_pho, b)}
        phones.append(lst)

    if sort_phones == 'name':
        phones = sorted(phones, key=lambda i: (i['name']))

    elif sort_phones == 'min_price':
        phones = sorted(phones, key=lambda i: (i['price']))

    elif sort_phones == 'max_price':
        phones = sorted(phones, key=lambda i: (i['price']), reverse=True)



    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    keys_pho = ['name', 'price', 'image', 'release_date', 'lte_exists', 'slug']

    phone_obj = Phone.objects.filter(slug=slug)
    pho = [[c.name, c.price, c.image, c.release_date, c.lte_exists,
            c.slug] for c in phone_obj][0]
    lst = dict(zip(keys_pho, pho))

    context = {'phone': lst}
    return render(request, template, context)

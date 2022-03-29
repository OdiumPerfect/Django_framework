from django.shortcuts import render

# Create your views here.

def index(request):
    content = {
        'title': 'Geekshop',
    }
    return  render(request, 'mainapp/index.html', content)

def products(request):
    categories = [
        {'name': 'Новинки'},
        {'name': 'Одежда'},
        {'name': 'Обувь'},
        {'name': 'Аксесуары'},
        {'name': 'Подарки'},
    ]

    prod_card = [
        {
            'img': 'vendor/img/products/Adidas-hoodie.png',
            'title': 'Худи черного цвета с монограммами adidas Originals',
            'price': 6090,
            'text': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'
        },
        {
            'img': 'vendor/img/products/Blue-jacket-The-North-Face.png',
            'title': 'Синяя куртка The North Face',
            'price': 23725,
            'text': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'
        },
        {
            'img': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
            'title': 'Коричневый спортивный oversized-топ ASOS DESIGN',
            'price': 3390,
            'text': 'Материал с плюшевой текстурой. Удобный и мягкий.'
        },
        {
            'img': 'vendor/img/products/Black-Nike-Heritage-backpack.png',
            'title': 'Черный рюкзак Nike Heritage',
            'price': 2340,
            'text': 'Плотная ткань. Легкий материал.'
        },
        {
            'img': 'vendor/img/products/Black-Dr-Martens-shoes.png',
            'title': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
            'price': 13590,
            'text': 'Гладкий кожаный верх. Натуральный материал.'
        },
        {
            'img': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
            'title': 'Темно-синие широкие строгие брюки ASOS DESIGN',
            'price': 2890,
            'text': 'Легкая эластичная ткань сирсакер Фактурная ткань.'
        }
    ]


    content = {
        'title': 'Geekshop - каталог',
        'categories': categories,
        'prod_card': prod_card,
    }


    return  render(request, 'mainapp/products.html', content)
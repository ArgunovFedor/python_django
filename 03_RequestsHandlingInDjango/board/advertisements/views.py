from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


def advertisement_list(request, *args, **kwargs):
    advertisements = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика, гидромолота, ямобура'
    ]
    advertisements_1 = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика, гидромолота, ямобура'
    ]
    return render(request, 'advertisements/advertisement_list.html', {'advertisements': advertisements,
                                                                      'advertisements_1': advertisements_1})


class About(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Бесплатные объявления, описание'
        context['context'] = 'Бесплатные объявления в вашем городе!'
        return context


def categories_list(request, *args, **kwargs):
    categories = ['личные вещи', 'транспорт', 'хобби и отдых', 'dungeons']
    print('fefe')
    return render(request, 'categories/categories_list.html', {'categories': categories})


class Regions(View):
    def get(self, request):
        regions = ['Алтай', 'Москва']
        return render(request, 'regions.html', {'regions': regions})

    def post(self, request):
        return 'Регион успешно создан'


content = [
    {
        'url': 'https://248006.selcdn.ru/LandGen/phone_4589beaf332198133164e04e0fb855c2c1368858.png',
        'header': 'Профессия Python-разработчик',
        'text': 'На Python пишут веб-приложения и нейросети, '
                'проводят научные вычисления и автоматизируют процессы. '
                'Язык просто выучить, даже если вы никогда не программировали. '
                'На курсе вы создадите Telegram-бота, полноценный магазин и задачник для портфолио, '
                'а Центр карьеры поможет найти работу Python-разработчиком.'
    },
    {
        'url': 'https://248006.selcdn.ru/LandGen/phone_0b95c9f42ca3ec65c771ec857e7f8193459ca51d.png',
        'header': 'Профессия Инженер по тестированию',
        'text': 'Вы научитесь находить ошибки в работе сайтов и приложений с помощью Java, JavaScript или Python. '
                'С первого занятия погрузитесь в практику и сможете начать зарабатывать уже через 4 месяца.'
    },
    {
        'url': 'https://248006.selcdn.ru/LandGen/phone_65230cde05b752f3ad673b7c8dc172a45ad958ae.png',
        'header': 'Профессия Data Scientist PRO',
        'text': 'Освойте Data Science с нуля. Попробуйте силы в аналитике данных, машинном обучении, '
                'дата-инженерии и решите, какое направление вам нравится больше. '
                'Через год сможете работать Junior-специалистом, а через два — станете профессионалом уровня Middle.'
    },
    {
        'url': 'https://248006.selcdn.ru/LandGen/phone_5df6b6516eb2604c7f99a5236b90e097217fae1f.png',
        'header': 'Профессия 1С-разработчик',
        'text': 'Станьте разработчиком в системе «1С:Предприятие» под руководством личного наставника '
                'и зарабатывайте на этом даже без опыта программирования. '
                'После прохождения курса — помощь в трудоустройстве.'
    },
    {
        'url': 'https://248006.selcdn.ru/LandGen/phone_57c9d80b2b75745579f68b99bdd0e2c0516a955f.png',
        'header': 'Профессия Java-разработчик PRO',
        'text': 'Вы с нуля освоите востребованный язык программирования, '
                'научитесь создавать качественные приложения под разные платформы и станете ценным '
                'Java-специалистом уровня middle.'
    },
]
request_counter = 0


class Advertisements(TemplateView):
    template_name = 'advertisements/advertisement_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advertisements_list'] = content
        global request_counter
        request_counter += 1
        context['request_counter'] = request_counter
        return context

    def post(self, request):
        global template_name
        return HttpResponse('Запрос на создание новой записи успешно выполнен')


class Contacts(TemplateView):
    template_name = 'contacts/contacts_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['phone_number'] = '8-800-708-19-45'
        context['mail'] = 'sales@company.com'
        return context


class Main(View):
    template_name = 'main.html'
    def get(self, request):
        regions = ['Алтайский край', 'Амурская область', 'Архангельская область', 'Астраханская область']
        categories = ['Категория - 1', 'Категория - 2', 'Категория - 3',
                      'Категория - 4', 'Категория - 5', 'Категория - 6',
                      'Категория - 7']

        return render(request, 'main.html', {
            'regions': regions,
            'categories': categories
        })

    def post(self,request):
        category = request.POST['category']
        region = request.POST['region']
        text = request.POST['text']
        return HttpResponse(f'Вы выбрали:{category}, {region}, {text}')
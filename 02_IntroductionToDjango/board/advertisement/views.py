from django.shortcuts import render
from django.http import HttpResponse


def main_page(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_list.html', {})


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


def course(request, num=0, *args, **kwargs):
    return render(request, 'advertisement/advertisement_list.html', context=content[num - 1])

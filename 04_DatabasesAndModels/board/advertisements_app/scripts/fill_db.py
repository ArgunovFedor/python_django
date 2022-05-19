from advertisements_app.models import Advertisement


def script():
    for i in range(500000):
        adv = Advertisement(title=f'Название {i}', description=f'Описание {i}')
        adv.save()
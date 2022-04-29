import django_loguru.middleware
from django_loguru.middleware import DjangoLoguruMiddleware

"""
Прописал полный путь к logger, так как похоже у меня баг с pycharm 
"""
django_loguru.middleware.logger.add('info.log', filter=lambda record: record['level'].name == 'INFO',
                                    retention='10 days')


class FilterDataMiddleware:
    def __init__(self, get_response):
        self.get_respense = get_response

    def __call__(self, request):
        method = request.method
        url = request.path
        user = request.user
        django_loguru.middleware.logger.log('INFO',
                                            ' '.join(['Пользователь c ID:', str(user), 'вызвал http метод:', method,
                                                      'по url', url]))
        response = self.get_respense(request)
        return response

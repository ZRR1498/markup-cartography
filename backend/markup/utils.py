
menu = [{'title': "Главная страница", 'url_name': 'home'},
        {'title': "Добавить разметку", 'url_name': 'add_markup'},
        {'title': "История разметок", 'url_name': 'history'},
        ]


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)

        context['menu'] = user_menu

        return context

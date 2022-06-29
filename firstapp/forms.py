from django import forms
#
#
# class UserForm(forms.Form):
#     name = forms.CharField()
#     age = forms.IntegerField()
#
#
# class ProductForm(forms.Form):
#     name = forms.CharField()
#     price = forms.IntegerField()
#     count = forms.IntegerField()
#
#
# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField()
#     is_admin = forms.BooleanField()


# class UserForm(forms.Form):
#     name = forms.CharField()
#     age = forms.CharField()
#     work = forms.NullBooleanField()


# class UserForm(forms.Form):
#     test1 = forms.BooleanField()
#     test2 = forms.NullBooleanField()
#     test3 = forms.CharField()
#     test4 = forms.EmailField()
#     test5 = forms.GenericIPAddressField()
#     test6 = forms.URLField()
#     test7 = forms.FileField()
#     test8 = forms.ImageField()
#     test9 = forms.DateField()
#     test10 = forms.TimeField()
#     test11 = forms.SplitDateTimeField()
#     test12 = forms.IntegerField()
#     test13 = forms.FloatField()
#     test14 = forms.ChoiceField(choices=((1, 'Ivan'), (2, 'Serhii'), (3, 'Egor')))


# forms.BooleanField()  - Создается поле checkbox если флажок стоит возвращает True, а еслли нет то возвращает False
# forms.NullBooleanField()  - Генерирует выпадающий список с вариантами ответов: unknown-NULL, yes-True, no-False
# forms.CharField()  - Предназначен для ввода текста(python type = str)
# forms.EmailField()  - Предназначен для ввода адресса електронной почты(имеет встроеную валидацию на @gmail.com,@mail.com)
# forms.GenericIPAddressField()  - Предназначен для ввода IP адрессов(имеет встроеную валидацию)
# forms.URLField()  - Предназначен для ввода URL адрессов(имеет встроеную валидацию)
# forms.FileField()  - Предназначен для выбора файла(с устройства), позволяет выбирать РАЗЛИЧНЫЕ файлы
# forms.ImageField()  - Предназначен для выбора файла(с устройства), позволяет выбирать IMAGE файлы
# forms.DateField()  - Создает тестовое поле, предназначен для ввода даты(0000-00-00 или 00/00/00)
# forms.TimeField()  - Создает тестовое поле, предназначен для ввода времени(00:00:00 или 00:00)
# forms.SplitDateTimeField()  - Создает 2 текстовых поля, предназначны для даты и времени(также как и по отдельности, сначала дата потом время)
# forms.IntegerField()  - Предназначен для ввода типа даных только int, также имеет функционал с 2 стрелочками которые увеличивают или уменьшают число на 1
# forms.FloatField()  - Предназначен для ввода типа даных int и float, также имеет функционал с 2 стрелочками которые увеличивают или уменьшают на 1
# forms.ChoiceField(choices=((1, 'Ivan'), (2, 'Serhii'), (3, 'Egor')))  - Генерирует выпадающий список с вариантами ответов: (создаем tuple в tuple в каждом из которых есть по 2 елемента: первый-ключ, второй значение)
# На HTML странице выглядит соответствующим образом:
# <option value="1">Ivan</option>
# <option value="2">Serhii</option>
# <option value="3">Egor</option>
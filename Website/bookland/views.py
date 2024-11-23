from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView


def index(request):
    """
    Отображает главную страницу сайта с каталогом электронных книг.

    :param request: Объект HttpRequest, представляющий HTTP-запрос.
    :return: Объект HttpResponse, содержащий HTML-страницу с каталогом книг.
    """
    text_head = 'На нашем сайте вы можете купить книги в электронном виде'
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    context = {'text_head': text_head, 'books': books, 'num_books': num_books}
    return render(request, 'index.html', context=context)


class BookList(ListView):
    """
    Представление для отображения списка книг с поддержкой пагинации.

    Наследуется от generic.ListView.
    """
    model = Book
    context_object_name = 'books'
    template_name = 'book_list.html'
    paginate_by = 5


class BookDetail(DetailView):
    """
    Представление для отображения подробной информацией выбранной из списка книги с поддержкой динамической url
    """

    model = Book
    context_object_name = 'book'
    template_name = 'book_detail.html'

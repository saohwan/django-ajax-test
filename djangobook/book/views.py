from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

from book.forms import BookForm
from book.models import Book


def index(request):
    return render(request, "index.html")


def book_list(request):
    context = {}

    books = Book.objects.filter().order_by('-id')

    context['books'] = books  # context 에  books를 넣어준다
    return render(request, 'book_list.html', context)  # 넣어준  context를 boot_list.html 에 보내준다.


def save_book_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            books = Book.objects.all().order_by('-id')
            data['html_book_list'] = render_to_string('includes/partial_book_create.html', {
                'books': books
            })
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
    else:
        form = BookForm()

    return save_book_form(request, form, 'includes/partial_book_create.html')


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
    else:
        form = BookForm(instance=book)

    return save_book_form(request, form, 'includes/partial_book_update.html')


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    data = dict()
    if request.method == 'POST':
        book.delete()
        data['form_is_valid'] = True
        books = Book.objects.all().order_by('-id')[:7]
        data['html_book_list'] = render_to_string('includes/partial_book_list.html', {
            'books': books
        })
    else:
        context = {'book': book}
        data['html_form'] = render_to_string('includes/partial_book_delete.html', context, request=request)

    return JsonResponse(data)

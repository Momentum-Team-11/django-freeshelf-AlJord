from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm

def home(request):
    if request.user.is_authenticated:
        return redirect('book_list') ## need html for homepage
    return render(request, 'book/home.html')


def check_admin_user(user):
    return user.is_staff



## @login_required should be added to every view behind login look up permission required
## @user_passes_test(check_admin_user)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'base/book_list.html', {"books": books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book':book})

def add_book(request):
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='add_book')
    return render(request, 'add_book.html',{'form':form})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.methond == "GET":
        form = BookForm(instance=book)
    else:
        form = BookForm(data = request.POST, instance = book)
        if form.is_valid():
            form.save()
        return redirect(to='book_list')
    return render(request, 'edit_book.html', {
        'form':form,
        'book':book
    })

def delete_book(request, pk):
    book= get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect(to='book_list')
    return render(request, "delete_book.html",{'book':book})

#def show_genere(request, slug):
    #book = Book.objects.filter(genres__slug=slug)

    #return render(request, 'book/booklist.html',{'book':book})
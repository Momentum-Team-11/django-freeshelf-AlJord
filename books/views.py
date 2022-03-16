from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Book, Group
from .forms import BookForm

def home(request):
    if request.user.is_authenticated:
        return redirect('book_list') ## need html for homepage
    return render(request, 'book/home.html')


def check_admin_user(user):
    return user.is_staff

@login_required 
@user_passes_test(check_admin_user)
def book_list(request):
    books = Book.objects.all()
    groups = Group.objects.all()
    return render(request, 'base/book_list.html', {"books": books, 'groups':groups})

@login_required 
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'base/detail.html', {'book':book, })

@login_required 
@user_passes_test(check_admin_user)
def add_book(request):
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='add_book')
    return render(request, 'add_book.html',{'form':form})

@login_required 
@user_passes_test(check_admin_user)
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

@login_required 
@user_passes_test(check_admin_user)
def delete_book(request, pk):
    book= get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect(to='book_list')
    return render(request, "base/delete_book.html",{'book':book})



def group(request, slug):
    group = get_object_or_404(Group, slug=slug)
    books = group.book.all()
    return render(request, "base/group.html", {"group": group, "books": books})
#def show_genere(request, slug):
    #book = Book.objects.filter(genres__slug=slug)
    #genre = get_object_or_404(Genre,slug=slug
    #albums = genre

    #return render(request, 'book/booklist.html',{'book':book})
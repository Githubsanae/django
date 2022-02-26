from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Book
# Create your views here.
def all_book(requset):
    all_book=Book.objects.filter(is_active=True)
    return render(requset,'bookstore/all_book.html',locals())

def update_book(request,book_id):
    try:
        book=Book.objects.get(id=book_id,is_active=True)
    except Exception as e:
        print('id wrong')
        return HttpResponse('--id wrong--')
    if request.method=='GET':
        return render(request,'bookstore/update_book.html',locals())
    if request.method=='POST':
        price=request.POST['price']
        book.price=price
        book.save()
        return HttpResponseRedirect('/bookstore/all_book')

def delete_book(request):
    book_id = request.GET.get('book_id')
    if not book_id:
        return HttpResponse('wrong')
    try:
        book=Book.objects.get(id=book_id,is_active=True)
    except Exception as e:
        print(f'error {e}')
        return HttpResponse('wrong')
    book.is_active=False
    book.save()
    return HttpResponseRedirect('/bookstore/all_book')
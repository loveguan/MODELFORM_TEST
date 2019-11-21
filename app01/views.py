from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from  .models import *
from  django import  forms
from django.forms import ModelForm
from django.forms import  widgets as wid

class BookForm(ModelForm):
    class Meta:
        model=Book
        fields="__all__"
        labels={"title":"书籍名称","price":"价格"}
        widgets={
            "title": wid.TextInput(attrs={"class": "form-control"}),
            "price": wid.TextInput(attrs={"class": "form-control"}),
            "date": wid.TextInput(attrs={"class": "form-control", "type": "date"}),
            "publish": wid.Select(attrs={"class": "form-control"}),
            "authors": wid.SelectMultiple(attrs={"class": "form-control"}),
        }
        error_messages={
            "title":{"required":"不能为空"}
        }


def books(request):
    book_list=Book.objects.all()
    return render(request,'books.html',locals())

def addbook(request):
    if request.method=="POST":
        form =BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books/')
        else:
            return redirect('/book/add')
    form=BookForm()
    return render(request,'add.html',locals())

def editbook(request,edit_book_id):
    edit_book=Book.objects.filter(pk=edit_book_id).first()
    if request.method=="POST":
        # 带instance说明是编辑数据
        form=BookForm(request.POST,instance=edit_book)
        if form.is_valid():
            form.save()
            return redirect("/books/")
    #     注意和add的区别，这个有instance，把数据带过去了
    form =BookForm(instance=edit_book)
    return render(request,'edit.html',locals())
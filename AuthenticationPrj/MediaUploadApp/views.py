from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from .forms import BookModelForm
from .models import Book

# Create your views here.
def uploadView(request):
    if request.method=='POST':
        uploaded_file=request.FILES['document']
        #print(uploaded_file.name)
        #print(uploaded_file.size)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name,uploaded_file)
        # print(type(name))
        # print(name)
        url = fs.url(name)
        # print(type(url))
        context = {'url':url}
        return render(request,'MediaUploadApp/upload.html',context)
    return render(request, 'MediaUploadApp/upload.html')


def book_list(request):
    books = Book.objects.all()
    return render(request,'MediaUploadApp/book_list.html',{'books':books})

def upload_book(request):
    form = BookModelForm()
    if request.method=='POST':
        # print('post request')
        form = BookModelForm(request.POST,request.FILES)
        if form.is_valid():
            # print('form created')
            form.save()
            # print('form saved')
        return redirect('books')
    # print('get request')
    return render(request,'MediaUploadApp/upload_book.html',{'form':form})
from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm
import pyqrcode


def my_view(request):
    print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    message = 'Upload as many files as you want!'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            # barcode.png('myqr.png', scale = 6)
            newdoc.save()
            
            url = pyqrcode.create('https://drive.google.com/file/d/1vYRUNRRouqKMAxXwccDz-P2HeAbCkPGD/view?usp=sharing')
            url.svg('fhutr.svg', scale=8)
            print(url.terminal(quiet_zone=1))
            # Redirect to the document list after POST
            return redirect('my-view')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'list.html', context)
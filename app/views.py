from django.shortcuts import render
from PyPDF2 import PdfReader, PdfWriter

# Home page view
def home(request):
    return render(request, 'index.html')

# Merge PDF view
def merge(request):
    if request.method == 'POST':
        pdf_files = request.FILES.getlist('pdfs')  # Get list of uploaded PDFs
        writer = PdfWriter()
        
        for pdf_file in pdf_files:
            reader = PdfReader(pdf_file)
            for page in reader.pages:
                writer.add_page(page)

        # Save merged PDF
        with open('merged_output.pdf', 'wb') as f:
            writer.write(f)

        return render(request, 'merge.html', {'message': 'PDFs Merged Successfully!'})

    return render(request, 'merge.html')

# Other views for split, rotate, remove password etc.
def pdf_editor(request):
    return render(request, 'pdf_editor.html')

def qa_qc(request):
    return render(request, 'qa_qc.html')

def remove_password(request):
    return render(request, 'remove_password.html')

def rotate(request):
    return render(request, 'rotate.html')

def split(request):
    return render(request, 'split.html')

def survey(request):
    return render(request, 'survey.html')

def billing_planning(request):
    return render(request, 'billing_planning.html')
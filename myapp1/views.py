from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# # personal navigator
# def index(request):
#     return HttpResponse('''<h1>Hello Vishal</h1> <a href="https://www.djangoproject.com/start/">Django Tutorial:</a>''')

# def about(request):
#     return HttpResponse("About Vishal")

#Note: for running the website at a time the we have to declare djtext = analysed  and comment the return statements, use only if statement. and lastly we declare the return statement


def index(request):
    #1 return HttpResponse("Home")
    #2 params = {'name': 'Vishal', 'place': 'Pune'}
    #2 return render(request, 'myapp1/index.html', params)
    return render(request, 'myapp1/index.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    print(djtext)

    # Check checkbox values - we covert it into post beacause it getting large data
    # removepunc = request.GET.get('removepunc', 'off')
    # print(removepunc)
    # fullcaps = request.GET.get('fullcaps', 'off')
    # newlineremover = request.GET.get('newlineremover', 'off')
    # extraspaceremover = request.GET.get('extraspaceremover', 'off')
    # charcount = request.GET.get('charcount', 'off')

    removepunc = request.POST.get('removepunc', 'off')
    print(removepunc)
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char.upper()
            # print("Analysed text is:" + analyzed)
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'myapp1/analyze.html', params)
    elif fullcaps == "on":
        analyzed = " "
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Capital all', 'analyzed_text': analyzed}
        return render(request, 'myapp1/analyze.html', params)
    elif newlineremover == "on":
        analyzed = " "
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char.upper()
        params = {'purpose':'New Line Remove', 'analyzed_text': analyzed}
        return render(request, 'myapp1/analyze.html', params)
    elif extraspaceremover == "on":
        analyzed = " "
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose':'Extra Space Remover', 'analyzed_text': analyzed}
        return render(request, 'myapp1/analyze.html', params)
    elif charcount == "on":
        my = len(djtext)
        params = {'purpose':'Character Counter', 'analyzed_text': my}
        return render(request, 'myapp1/analyze.html', params)

    else:
        return HttpResponse("Error")

"""
def removepunc(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    print(djtext)
    # analyze the text
    return HttpResponse('''<h1>Remove punc</h1> <form>
 <input type="button" value="Go back!" onclick="history.back()">
</form>''')

def capfirst(request):
    return HttpResponse('''<h1>Capatalize first</h1> <form>
 <input type="button" value="Go back!" onclick="history.back()">
</form>''')

def newlineremove(request):
    return HttpResponse('''<h1>Newline remove first</h1> <form>
 <input type="button" value="Go back!" onclick="history.back()">
</form>''')

def spaceremove(request):
    return HttpResponse('''<h1>Space remover</h1> <form>
 <input type="button" value="Go back!" onclick="history.back()">
</form>''')

def charcount(request):
    return HttpResponse('''<h1>character count</h1> <a href="http://127.0.0.1:8000/">Go Back !</a>''')

"""
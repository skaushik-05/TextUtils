# I have created this file - shubham 

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    

def analyse(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    ##checkbox values
    removepunc = request.POST.get('removepunc','off')
    uppercase = request.POST.get('uppercase','off')
    newlineremoval = request.POST.get('newlineremoval','off')
    extraspaceremoval = request.POST.get('extraspaceremoval','off')
    charcounter = request.POST.get('charcounter','off')
    # check if checkbox is on
    #condition for puntutation removal

    if removepunc == 'on':
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analysed =""
        for char in djtext:
            if char not in punctuations:
                analysed= analysed+ char
        params = {'purpose':'Removed punctuations', 'analysed_text': analysed}
        djtext = analysed
        
    if uppercase=='on':
        analysed= ""
        for char in djtext:
            analysed = analysed+ char.upper()
        params = {'purpose':'UPPER CASE converted', 'analysed_text': analysed}
        djtext = analysed
        # return render(request, 'analyse.html', params)

    # new line removal
    if newlineremoval=='on':
        analysed= ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analysed = analysed+ char
        params = {'purpose':'New line removed', 'analysed_text': analysed}
        djtext = analysed
        #return render(request, 'analyse.html', params)

    # extra space removal
    if extraspaceremoval=='on':
        analysed= ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analysed = analysed+ char
        params = {'purpose':'Extra space removed', 'analysed_text': analysed}
    
    if (removepunc != 'on' and uppercase !='on' and newlineremoval !='on' and extraspaceremoval !='on'):
        return HttpResponse("Please select the operation to analyse the text")
    
    return render(request, 'analyse.html', params)
    

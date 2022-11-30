from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # POSTting text's values form Html forms.
    text = request.POST.get('text', 'Default')
    checkbox = request.POST.get('removepunc', 'off')
    upper = request.POST.get('upper', 'off')
    lower = request.POST.get('lower', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    if checkbox == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punction',
                  'analyze_text': analyzed}
        # Overridding text.
        text = analyzed
        print(text)

    if upper == 'on':
        analyzed = ''
        for char in text:
            if char in text:
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Remove Punction',
                  'analyze_text': analyzed}
        text = analyzed

    if lower == 'on':
        analyzed = ''
        for char in text:
            analyzed = analyzed + char.lower()
        params = {'purpose': 'Remove Punction',
                  'analyze_text': analyzed}
        text = analyzed
    if newlineremover == 'on':
        analyzed = ''
        for char in text:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punction',
                  'analyze_text': analyzed}
        text = analyzed

    if extraspaceremover == 'on':
        analyzed = ''
        for index, char in enumerate(text):
            if not (text[index] == ' ' and text[index+1] == ' '):
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punction',
                  'analyze_text': analyzed}
        text = analyzed
    if charcounter == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        chrcunter = ''
        analyze = ''
        for x in text:
            if x not in punctuations:
                pass
            chrcunter += x
            analyze += x
        # analyzed = analyze
        chrcunter = len(chrcunter)
        params = {'purpose': 'Remove Punction',
                  'characterrounter': chrcunter, 'analyze_text': analyze}

    if(checkbox != 'on' and upper != 'on' and lower != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charcounter
       != 'on'):
        return HttpResponse('Plseas select any operation and try again.')

    return render(request, 'analyze.html', params)

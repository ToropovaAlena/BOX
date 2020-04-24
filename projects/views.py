from django.shortcuts import render, redirect
from datetime import datetime
from mysite.settings import SECRET_KEY


def index(request):
    return render(request, "project/index.html")


publications_data = [
    {
        'id': 0,
        'name': 'статья 1 круть!',
        'date': datetime.now(),
        'text': '''Hello! This is a generator for text fonts of the "cool" variety. I noticed people were trying to find a generator like fancy letters, but were ending up on actual font sites rather than generators of copy-paste text like this one. So currently this is basically a duplicate of the above, but I think I'll try to collect a few more "cool" text fonts, like the old enlgish one, and specialise this a bit.
               <br> <br> If you're wondering how one produces cool text fonts like you see above, it's fairly simple (but maybe not what you'd expect). Basically, the text that gets generated isn't actually a font - it's a bunch of symbols that are in the unicode standard. You're reading symbols that are in the unicode standard right now - the alphabet is a part of it, as are all the regular symbols on your keyboard: !@#$%^&*() etc.'''

    },
    {
        'id': 1,
        'name': 'статья 2 вооще круть!',
        'date': datetime.now(),
        'text': '''Hello! This is a generator for text fonts of the "cool" variety. I noticed people were trying to find a generator like fancy letters, but were ending up on actual font sites rather than generators of copy-paste text like this one. So currently this is basically a duplicate of the above, but I think I'll try to collect a few more "cool" text fonts, like the old enlgish one, and specialise this a bit.
               <br> <br> If you're wondering how one produces cool text fonts like you see above, it's fairly simple (but maybe not what you'd expect). Basically, the text that gets generated isn't actually a font - it's a bunch of symbols that are in the unicode standard. You're reading symbols that are in the unicode standard right now - the alphabet is a part of it, as are all the regular symbols on your keyboard: !@#$%^&*() etc.'''
    }
]


def index_tests(request, number):

    if number < len(publications_data):

        return render(request, 'index_test.html', publications_data[number])
    else:
        return redirect('/')

def index_test(request):
    return render(request, 'index_tests.html', {
    'publications':publications_data
    })


def publish(request):
    if request.method =='GET':
        return render(request, "publish.html")
    else:
        secret=request.POST["secret"]
        name=request.POST["name"]
        text=request.POST["text"]


    if secret != SECRET_KEY:
        return render(request, 'publish.html', {
        'publications':'SECRET_KEY не верный'
        })

    if name == '':
        return render(request, 'publish.html', {
        'publications':'название стаьтьи не указано'
        })

    if text == '':
        return render(request, 'publish.html', {
        'publications':'статья без текста'
        })

    publications_data.append({
        'id': len(publications_data),
        'name': name,
        'date': datetime.now(),
        'text': text.replace('\n', '<br />')
    })
    return redirect('/publications')
comments = [{
    'namecom': 'namecom',
    'textcom': 'textcom'
}]
def comment(request):
    if request.method =='GET':
        return render(request, "index_test.html")
    else:
        namecom=request.POST["namecom"]
        textcom=request.POST["textcom"]
        print(request.POST["namecom"])
        print(request.POST["textcom"])

    comments.append({
        'namecom': namecom,
        'textcom': textcom
    })

    return redirect('/publications')

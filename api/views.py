from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from api.models import Note
from logger import Logger

def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/')


def userlogin(request):

    u, p = (str(request.POST['username']),
            str(request.POST['password']))
    user = authenticate(username=u, password=p)

    if user is not None:
        login(request, user)
        return True
    return False


def userpost(request):

    try:
        title, body, key = (str(request.POST['note_title']),
                            str(request.POST['note_body']),
                            str(request.POST['note_key']))
        if key:
            key = int(key)
            if key > 0:
                note = Note.objects.get(pk=key)
                note.title = title
                note.body = body
                note.save()
            else:  # Delete
                note = Note.objects.get(pk=abs(key))
                note.delete()

        else:
            Note(title=title, body=body, user=request.user).save()
        return True
    except Exception:
        return False


def _handlePosts(request):

    lg = userlogin(request) if 'username' in request.POST.keys() else None
    sv = userpost(request) if 'note_title' in request.POST.keys() else None
    return lg, sv


def index(request):

    if request.POST:
        _handlePosts(request)

        return HttpResponseRedirect('/')

    notes = Note.objects.all().order_by('-date_created')

    if request.user.is_authenticated:
        return render(request, 'indexS.html', {'notes': notes, 'user': request.user})
    else:
        return render(request, 'index.html', {'notes': notes})

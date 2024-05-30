from django.shortcuts import render, redirect
from .models import Board, Image, Imageboard
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash


def index(request):
    return render(request, 'index.html')

def mylogin(request):
    return render(request, 'loginpage.html')

def myregister(request):
    return render(request, 'register.html')

def mylogout(request):
    logout(request)
    return redirect('loginpage')

def formregister(request):
    usernamevar = request.POST['username']
    passwordvar = request.POST['password']
    emailvar = request.POST['email']
    firstnamevar = request.POST['firstname']
    lastnamevar = request.POST['lastname']


    user = User.objects.create_user(usernamevar, emailvar, passwordvar)
    user.first_name = firstnamevar
    user.last_name = lastnamevar

    user.save()
    return render(request, 'loginpage.html')

@login_required
def profil(request):
    # Ambil informasi pengguna saat ini
    user = request.user

    # Render halaman profil dengan memberikan informasi pengguna ke dalam konteks template
    return render(request, 'profil.html', {'user': user})

@login_required
def edit_profil(request):
    user = request.user

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password == password_confirm:
            user.username = username
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            if password:
                user.set_password(password)
                update_session_auth_hash(request, user)  # Untuk menjaga pengguna tetap login setelah mengubah password
            user.save()
            return redirect('profil')
        else:
            # Tambahkan logika untuk menangani kesalahan validasi password tidak cocok
            error_message = "Password dan konfirmasi password tidak cocok."
            return render(request, 'editprofil.html', {'user': user, 'error_message': error_message})

    return render(request, 'editprofil.html', {'user': user})

def dashboard(request):
    user = request.user
    search_query = request.GET.get('search_query')

    if search_query:
        imagelist = Image.objects.filter(
            Q(nama__icontains=search_query) | 
            Q(deskripsi__icontains=search_query) |
            Q(userid__first_name__icontains=search_query) |
            Q(userid__last_name__icontains=search_query)
        )
    else:
        imagelist = Image.objects.all()

    context = {
        'user': user,
        'imagelist': imagelist,
    }
    return render(request, 'dashboard.html', context)

def formlogin(request):
    usernamevar = request.POST['username']
    passwordvar = request.POST['password']

    user = authenticate(username=usernamevar, password=passwordvar)
    if user is not None:
        login(request, user)
        return redirect('dashboard')
    return redirect('loginpage')

def boardpage(request):
    return render(request, 'boardpage.html')

def formboard(request):
    namavar = request.POST['nama'] #nama didapat dari nilai name diinput boardpage.html
    deskripsivar = request.POST['deskripsi']
    user = request.user  # menangkap user yang saat ini sedang login

    # create
    boardvar = Board(nama=namavar, deskripsi=deskripsivar, userid=user) #userid dari model
    boardvar.save()
    return redirect('dashboard')

def boardedit(request, id):
    board = Board.objects.get(id=id)
    context = {
        'board': board
    }
    return render(request, 'boardedit.html', context)

def formboardedit(request):
    namavar = request.POST['nama'] #nama didapat dari nilai name diinput boardpage.html
    deskripsivar = request.POST['deskripsi']
    id = request.POST['id']

    # edit
    board = Board.objects.get(id=id)
    board.nama = namavar
    board.deskripsi = deskripsivar
    board.save()
    return redirect('dashboard') #dashboard dari name di path urls

def boarddelete(request, id):
    board = Board.objects.get(id=id)
    context = {
        'board': board
    }
    return render(request, 'boarddelete.html', context)

def formboarddelete(request):
    # delete
    id = request.POST['id']
    board = Board.objects.get(id=id)
    board.delete()
    return redirect('dashboard')

def uploadimage(request):
    user = request.user
    imagelist = Image.objects.filter(userid=user)
    context = {
        'imagelist' : imagelist,
    }
    return render(request, 'uploadimage.html', context)

def hapusgambar(request, id):
    imagevar = Image.objects.get(id=id)
    imagevar.delete()
    return redirect('uploadimage')

def formuploadimage(request):
    namavar = request.POST['nama']
    deskripsivar = request.POST['deskripsi']
    sourcevar = request.FILES['source']
    user = request.user
    imagevar = Image(nama=namavar, deskripsi=deskripsivar, source=sourcevar, userid=user)
    imagevar.save()
    return redirect('uploadimage')

def viewboard(request):
    user = request.user
    boardlist = Board.objects.filter(userid=user.id)
    context = {
        'boardlist' : boardlist,
    }
    return render(request, 'viewboard.html', context)

def lihatgambarpapan(request, id):
    board = Board.objects.get(id=id)
    imagelist = Imageboard.objects.filter(boardid=board)
    context = {
        'board': board,
        'imagelist' : imagelist,
    }
    return render(request, 'lihatgambarpapan.html', context) #render dari file hmtl

def formuploadgambarpapan(request):
    idvar = request.POST['id']
    namavar = request.POST['nama']
    deskripsivar = request.POST['deskripsi']
    sourcevar = request.FILES['source']
    user = request.user
    board = Board.objects.get(id=idvar)
    imagevar = Imageboard(nama=namavar, deskripsi=deskripsivar, source=sourcevar, userid=user, boardid=board)
    imagevar.save()
    return redirect('/lihatgambarpapan/' + idvar + '/') #redirect dari 'name' di urls.py

def hapusgambarpapan(request, idimage, idboard):
    imagevar = Imageboard.objects.get(id=idimage)
    imagevar.delete()
    return redirect('/lihatgambarpapan/' + idboard + '/')


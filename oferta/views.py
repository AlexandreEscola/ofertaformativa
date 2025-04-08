from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import OfertaFormativa
from .forms import OfertaForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True  # Isso força o redirecionamento para a home após o login de um usuário autenticado

    def get_success_url(self):
        # Se o usuário for superuser, ele será redirecionado para a dashboard. Caso contrário, será redirecionado para a homepage.
        if self.request.user.is_superuser:
            return reverse_lazy('dashboard')
        return reverse_lazy('home')  # Redireciona para a homepage caso não seja superuser



def home(request):
    ofertas = OfertaFormativa.objects.all()
    return render(request, 'home.html', {'ofertas': ofertas})

@login_required
def dashboard(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Você não tem permissão para aceder à página de administração.")
    
    ofertas = OfertaFormativa.objects.all()  # Ou a lógica que você usa para listar as ofertas
    return render(request, 'dashboard.html', {'ofertas': ofertas})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def criar_oferta(request):
    if request.method == 'POST':
        form = OfertaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = OfertaForm()
    return render(request, 'criar_oferta.html', {'form': form})

# Editar oferta
def editar_oferta(request, id):
    # Recupera a oferta do banco de dados
    oferta = get_object_or_404(OfertaFormativa, id=id)

    if request.method == 'POST':
        # Lógica para salvar as mudanças
        oferta.nome = request.POST['nome']
        oferta.descricao = request.POST['descricao']
        oferta.saidas_profissionais = request.POST['saidas_profissionais']
        oferta.carga_horaria = request.POST['carga_horaria']
        oferta.disciplinas = request.POST['disciplinas']

        # Verifica se foi enviado um arquivo de imagem e atualiza a imagem
        if 'imagem' in request.FILES:
            oferta.imagem = request.FILES['imagem']
        
        # Salva a oferta com as mudanças, incluindo a imagem
        oferta.save()

        # Redireciona após salvar
        return redirect('dashboard')  # Ajuste para o redirecionamento que você deseja

    return render(request, 'editar_oferta.html', {'oferta': oferta})

# Remover oferta
def remover_oferta(request, id):
    oferta = OfertaFormativa.objects.get(id=id)
    if request.method == 'POST':
        oferta.delete()
        return redirect('dashboard')
    return render(request, 'confirmar_remocao.html', {'oferta': oferta})

def detalhes_oferta(request, id):
    oferta = get_object_or_404(OfertaFormativa, id=id)
    return render(request, 'detalhes_oferta.html', {'oferta': oferta})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from citasMedicas.forms import medicosRegistrationForm
from citasMedicas.forms import pacientesRegistrationForm
from citasMedicas.forms import citasRegistrationForm
from citasMedicas.models import Medicos
from citasMedicas.models import Pacientes
from citasMedicas.models import Citas

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST["usuario"]
        contrasena = request.POST["contrasena"]
        user = authenticate(request, username=username, password=contrasena)
        print(user)
        if user is not None:
            print("entra")
            login(request, user)
            return redirect("/inicio")
        else:
            messages.error(request, "¡Usuario o contraseña incorrectos!")
            return redirect("/")
    else:

        return render(request, "login.html")


@login_required
def logout_user(request):
    logout(request)
    return redirect("/")


def registrarse(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print("llega al print")
        if form.is_valid():
            print("llega al validar")
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def index(request):
    data = {}

    arreglo = []
    if Citas.objects.all():
        data = {"citas": Citas.objects.all()}
    else:
        data = {"citas": []}

    return render(request, "index.html", data)


@login_required
def medicosRequest(request):

    form = medicosRegistrationForm()

    if request.method == "POST":
        form = medicosRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        form.cleaned_data["nombre"]
        form.cleaned_data["email"]
        form.cleaned_data["fono"]
        return redirect("/medicos")
        # return render(index())

    if Medicos.objects.all():
        medicos = Medicos.objects.all()
        data = {"form": form, "medicos": medicos}
    else:
        data = {"form": form}
    return render(request, "medicos.html", data)


@login_required
def actualizarMedicos(request, id):
    medicos = Medicos.objects.get(id=id)
    form = medicosRegistrationForm(instance=medicos)
    if request.method == "POST":
        form = medicosRegistrationForm(request.POST, instance=medicos)
        if form.is_valid():
            form.save()
            return redirect("/medicos")

    if Medicos.objects.all():
        medicos = Medicos.objects.all()
        data = {"form": form, "medicos": medicos}
    else:
        data = {"form": form}
    return render(request, "medicos.html", data)


@login_required
def eliminarMedicos(request, id):
    medicos = Medicos.objects.get(id=id)
    medicos.delete()
    return redirect("/medicos")


@login_required
def pacientesRequest(request):
    form = pacientesRegistrationForm()

    if request.method == "POST":
        form = pacientesRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form de paciente es valido")
            print("Nombre: ", form.cleaned_data["nombre"])
            print("Correo: ", form.cleaned_data["email"])
            print("Fono: ", form.cleaned_data["fono"])
            return redirect("/pacientes")

    if Pacientes.objects.all():
        print("si")
        pacientes = Pacientes.objects.all()
        print(pacientes)
        data = {"form": form, "pacientes": pacientes}
    else:
        data = {"form": form}
    return render(request, "pacientes.html", data)


@login_required
def actualizarPacientes(request, id):
    pacientes = Pacientes.objects.get(id=id)
    form = pacientesRegistrationForm(instance=pacientes)
    if request.method == "POST":
        form = pacientesRegistrationForm(request.POST, instance=pacientes)
        if form.is_valid():
            form.save()
            return redirect("/pacientes")

    if Pacientes.objects.all():
        print("si")
        pacientes = Pacientes.objects.all()
        print(pacientes)
        data = {"form": form, "pacientes": pacientes}
    else:
        data = {"form": form}
    return render(request, "pacientes.html", data)


@login_required
def eliminarPacientes(request, id):
    pacientes = Pacientes.objects.get(id=id)
    pacientes.delete()
    return redirect("/pacientes")


@login_required
def citasRequest(request):
    form = citasRegistrationForm()
    arreglo = []

    if request.method == "POST":
        form = citasRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            form.cleaned_data["Asunto"]
            form.cleaned_data["Paciente"]
            form.cleaned_data["Medico"]
            form.cleaned_data["fecha"]
            return redirect("/citas")

    if Citas.objects.all():

        data = {"form": form, "citas": Citas.objects.all()}
    else:
        data = {"form": form}
    return render(request, "citas.html", data)


@login_required
def actualizarCitas(request, id):
    citas = Citas.objects.get(id=id)
    form = citasRegistrationForm(instance=citas)
    arreglo = []
    if request.method == "POST":
        form = citasRegistrationForm(request.POST, instance=citas)
        if form.is_valid():
            form.save()
            print("elimnado")
            return redirect("/citas")

    if Citas.objects.all():

        data = {"form": form, "citas": Citas.objects.all()}
    else:
        data = {"form": form}
    return render(request, "citas.html", data)


@login_required
def eliminarCitas(request, id):
    citas = Citas.objects.get(id=int(id))
    citas.delete()
    return redirect("/citas")


@login_required
def eliminarcitasIndex(request, id):
    citas = Citas.objects.get(id=int(id))
    citas.delete()
    return redirect("/inicio")


def pageNoFoud(request, exception):
    data = {}

    arreglo = []
    if Citas.objects.all():
        data = {"citas": Citas.objects.all()}
    else:
        data = {"citas": []}

    return render(request, "index.html", data)

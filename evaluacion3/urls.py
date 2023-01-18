from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from citasMedicas import views as medic

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", medic.login_user, name="login"),
    path("registrarse/", medic.registrarse, name="registrarse"),
    path("inicio/", medic.index, name="inicio"),
    path("medicos/", medic.medicosRequest, name="medicos"),
    path("pacientes/", medic.pacientesRequest, name="pacientes"),
    path("citas/", medic.citasRequest, name="citas"),
    path("eliminarmedicos/<int:id>", medic.eliminarMedicos),
    path("medicos/<int:id>", medic.actualizarMedicos),
    path("eliminarpacientes/<int:id>", medic.eliminarPacientes),
    path("pacientes/<int:id>", medic.actualizarPacientes),
    path("eliminarcitas/<int:id>", medic.eliminarCitas),
    path("eliminarcitasIndex/<int:id>", medic.eliminarcitasIndex),
    path("citas/<int:id>", medic.actualizarCitas),
    path("logout/", medic.logout_user),
]

handler404 = medic.pageNoFoud

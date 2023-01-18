from django import forms
from citasMedicas.models import Medicos
from citasMedicas.models import Pacientes
from citasMedicas.models import Citas
from django.db import connection


""" def db_table_exists(table_name):
    return table_name in connection.introspection.table_names()


print(db_table_exists("citasmedicas_pacientes"))


pacientes = [(0, "Seleccione paciente")]
if db_table_exists("citasmedicas_pacientes"):
    print(db_table_exists("citasmedicas_pacientes"))
    for paciente in Pacientes.objects.all():
        pacientes.append((paciente.id, paciente.nombre))
        print(paciente.nombre)

medicos = [(0, "Seleccione médico")]
if db_table_exists("citasmedicas_medicos"):
    print(db_table_exists("citasmedicas_medicos"))
    for medico in Medicos.objects.all():
        medicos.append((medico.id, medico.nombre)) """


class pacientesRegistrationForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = ["nombre", "email", "fono"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "fono": forms.TextInput(attrs={"class": "form-control"}),
        }


class medicosRegistrationForm(forms.ModelForm):
    class Meta:
        model = Medicos
        fields = ["nombre", "email", "fono"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "fono": forms.TextInput(attrs={"class": "form-control"}),
        }


class citasRegistrationForm(forms.ModelForm):
    class Meta:
        model = Citas
        fields = ["Asunto", "Paciente", "Medico", "fecha"]
        widgets = {
            "Asunto": forms.TextInput(attrs={"class": "form-control"}),
            "Paciente": forms.Select(attrs={"class": "form-control"}),
            "Medico": forms.Select(attrs={"class": "form-control"}),
            "fecha": forms.TextInput(
                attrs={"class": "form-control", "id": "datetimepicker"}
            ),
        }


""" self.fields["reminder_object_type"] = forms.ChoiceField(
    required=True,
    label="",
    widget=forms.RadioSelect(attrs={"class": "form-check form-control"}),
    choices=(("Client", "Client"), ("Contact", "Contact"), ("Action", "Action")),
) """

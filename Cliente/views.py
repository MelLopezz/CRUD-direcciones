from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Cliente
from .models import Direccion

def prueba(request):
    return render(request,'prueba.html')

def login_cliente(request):
    if request.method == "POST":
        email = request.POST['username']
        password = request.POST['password']
        try:
            cliente = Cliente.objects.get(correo_cliente=email)
            if cliente.check_password(password):
                request.session['cliente_id'] = cliente.correo_cliente
                print(f"Cliente logueado: {cliente.correo_cliente}")  # Debug
                return redirect('prueba')
            else:error_message = "Credenciales incorrectas"
        except Cliente.DoesNotExist:
            error_message = "Usuario no encontrado"

        return render(request, 'clienteLogin.html', {'error_message': error_message})
    return render(request, "clienteLogin.html")

def registro_cliente(request):
    if request.method == 'POST':
        nombre_cliente = request.POST.get('nombre_cliente')
        correo_cliente = request.POST.get('correo_cliente')
        telefono_cliente = request.POST.get('telefono_cliente')
        password_cliente = request.POST.get('password_cliente')
        confirm_password_cliente = request.POST.get('confirm_password_cliente')

        # Validaciones
        if password_cliente != confirm_password_cliente:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('registro_cliente')
        
        if len(password_cliente) < 6:
            messages.error(request, 'La contraseña debe tener al menos 6 caracteres.')
            return redirect('registro_cliente')

        # Guardar el cliente si todo es válido
        try:
            cliente = Cliente.objects.create(
                nombre_cliente=nombre_cliente,
                correo_cliente=correo_cliente,
                telefono_cliente=telefono_cliente,
                password_cliente=make_password(password_cliente),
                puntos=0,  # Valor predeterminado
            )
            messages.success(request, 'Usuario creado exitosamente. Ahora puedes iniciar sesión.')
            return redirect('login')
       
        except Exception as e:
            messages.error(request, f'Ocurrió un error al registrar al cliente: {str(e)}')
            return redirect('registro_cliente')

    return render(request, 'registro_cliente.html')

#CRUD

def direcciones_cliente(request):
    direccionesListadas = Direccion.objects.all()
    return render(request,"direcciones.html",{"direcciones":direccionesListadas})

def registrarDireccion(request):
   cliente_id=request.POST['txtNombreCliente']
   nombre_direccion=request.POST['txtNombreDireccion']
   departamento=request.POST['txtDepartamento']
   municipio=request.POST['txtMunicipio']
   calle=request.POST['txtCalle']
   numero_casa=request.POST['txtNumeroDeCasa']
   punto_referencia=request.POST['puntoDeReferencia']

   direccion = Direccion.objects.create(cliente_id=cliente_id,nombre_direccion=nombre_direccion, departamento=departamento, municipio=municipio,calle=calle,numero_casa=numero_casa, punto_referencia=punto_referencia )
   return redirect('direcciones')

def eliminarDireccion(request, id_direccion):
    direccion=Direccion.objects.get(id_direccion=id_direccion)
    direccion.delete()

    return redirect('direcciones')

def edicionDireccion(request,id_direccion):
      direccion=Direccion.objects.get(id_direccion=id_direccion)
      return render(request,"editarDireccion.html",{"direccion":direccion})

def modificar_direccion(request):
 
   nombre_direccion=request.POST['txtNombreDireccion']
   departamento=request.POST['txtDepartamento']
   municipio=request.POST['txtMunicipio']
   calle=request.POST['txtCalle']
   numero_casa=request.POST['txtNumeroDeCasa']
   punto_referencia=request.POST['puntoDeReferencia']

   direccion=Direccion.objects.get(id_direccion=id_direccion)
   
   direccion.nombre_direccion=nombre_direccion
   direccion.departamento= departamento
   direccion.municipio= municipio
   direccion.numero_casa= numero_casa
   direccion.calle= calle
   direccion.punto_referencia= punto_referencia
   direccion.save()

   return redirect('direcciones')


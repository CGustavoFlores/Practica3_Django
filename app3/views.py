from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ContactoForm, ProductoForm,CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required



def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, "app3/home.html", data)





def contacto(request):
    data = {
        'form':ContactoForm()
    }
    if request.method == 'POST':
        formulario =ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="contacto enviado"
        else:
            data["form"]= formulario
        
    return render(request,"app3/contacto.html",data)


@login_required
def galeria(request):
    return render(request,"app3/galeria.html")



@permission_required('app.add_producto')
def agregar_producto(request):  
    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            #datos=formulario.cleaned_data  LO CONVIERTE EN UN DICCIONARIO, POR LO TANTO HAY QUE GRABAR DE OTRA MANERA
            #datos.save()
            formulario.save()
            data["mensaje"] ="grabado correctamente !"
            return redirect(to="listar_productos")
        else:
            data["form"] = formulario   
    return render(request,'app3/producto/agregar.html', data)




@permission_required('app.view_producto')
def listar_productos(request):
    productos = Producto.objects.all()
    page= request.GET.get('page',1)
    try:
        paginator =Paginator(productos,2)
        productos = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': productos,
        'paginator': paginator
    }
    return render(request, 'app3/producto/listar.html', data)




@permission_required('app.change_producto')
def modificar_producto(request,id):    
    producto =get_object_or_404(Producto,id=id)
    data = {
        'form': ProductoForm(instance=producto)
    }    
    if request.method == 'POST':
        formulario  = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect(to="listar_productos")
        data["form"]=formulario
    return render(request,'app3/producto/modificar.html', data)





@permission_required('app.delete_producto')
def eliminar_producto(request,id):
    producto= get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado correctamente")    
    return redirect(to="listar_productos")
    
    
    
    
    
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method=='POST':
        formulario= CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #autentifico el usuario
            user =  authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to='home')   
        data["form"]=formulario
    return render(request, "registration/registro.html", data)
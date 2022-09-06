from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ContactoForm, ProductoForm
from django.contrib import messages




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



def galeria(request):
    return render(request,"app3/galeria.html")




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



def listar_productos(request):
    
    productos = Producto.objects.all()
    
    data = {
        'productos': productos
        
    }
    
    return render(request, 'app3/producto/listar.html', data)





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



def eliminar_producto(request,id):
    producto= get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    
    return redirect(to="listar_productos")
    
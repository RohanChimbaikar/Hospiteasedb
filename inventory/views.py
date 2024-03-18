from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.contrib import messages

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')

        # Create and save the new product
        product = Product.objects.create(
            name=name,
            description=description,
            quantity=quantity,
            date_added=timezone.now()
        )
        product.save()

        return redirect('/templates/inventory.html')  # Redirect to the inventory page after adding the product

    else:
        return render(request, 'error.html', {'message': 'Method not allowed'})


# views.py



def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        # Update the product with data from the form
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.quantity = request.POST.get('quantity')
        product.save()
        return redirect('/templates/inventory.html')
    return render(request, '/templates/inventory.html', {'product': product})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('doc')
    return render(request, 'delete_product.html', {'product': product})



def use_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        use_quantity = int(request.POST.get('useQuantity'))
        
        # Subtract the use quantity from the product quantity
        product.quantity -= use_quantity
        product.save()
        
        # Display a success message
        messages.success(request, 'Product quantity updated successfully.')
        
        # Redirect back to the page or wherever appropriate
        return redirect('doc')
    else:
        # If it's not a POST request, redirect or handle appropriately
        return redirect('doc')
    
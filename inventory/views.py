from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.contrib import messages
from django.http import JsonResponse

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
def get_product_details(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        try:
            product = Product.objects.get(id=product_id)
            # Assuming you have fields like name and description in your Product model
            data = {
                'name': product.name,
                'description': product.description,
                # Add more fields as needed
            }
            return JsonResponse(data)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    print(product)
    if request.method == 'POST':
        # Update the product with data from the form
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.quantity = request.POST.get('quantity')
        product.price=request.POST.get('price')
        product.save()
        # Redirect to the appropriate URL after successful edit
        return redirect('doc')  # Make sure 'doc' is the correct URL name
    return render(request, 'docdash.html', {'product': product})



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
        
        # Check if the updated quantity is zero or negative
        if product.quantity <= 0:
            product.quantity = 0
            product.status = 'OUT_OF_STOCK'
        
        product.save()
        
        # Display a success message
        messages.success(request, 'Product quantity updated successfully.')
        
        # Redirect back to the page or wherever appropriate
        return redirect('doc')
    else:
        # If it's not a POST request, redirect or handle appropriately
        return redirect('doc')
    
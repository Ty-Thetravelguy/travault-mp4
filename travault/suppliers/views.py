from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def supplier_list(request):
    """View for listing all suppliers."""
    return render(request, 'suppliers/supplier.html')

@login_required
def supplier_add(request):
    """View for adding a new supplier."""
    return render(request, 'suppliers/supplier_add.html')

@login_required
def supplier_edit(request):
    """View for editing an existing supplier."""
    return render(request, 'suppliers/supplier_edit.html')

@login_required
def supplier_process(request):
    """View for supplier processes."""
    return render(request, 'suppliers/supplier_process.html')

@login_required
def supplier_process_add(request):
    """View for adding a new supplier process."""
    return render(request, 'suppliers/supplier_process_add.html')

@login_required
def supplier_process_edit(request):
    """View for editing an existing supplier process."""
    return render(request, 'suppliers/supplier_process_edit.html')
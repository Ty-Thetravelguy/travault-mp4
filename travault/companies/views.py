from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# from .models import Company, CompanyNote  # Uncomment when you have these models
# from .forms import CompanyForm, CompanyNoteForm  # Uncomment when you create these forms

@login_required
def company_list(request):
    # companies = Company.objects.all()  # Uncomment when you have a Company model
    companies = []  # Placeholder, replace with actual data
    return render(request, 'companies/company_list.html', {'companies': companies})

@login_required
def company_detail(request, company_id):
    # company = get_object_or_404(Company, id=company_id)  # Uncomment when you have a Company model
    company = {}  # Placeholder, replace with actual data
    return render(request, 'companies/company_details.html', {'company': company})

@login_required
def company_add(request):
    if request.method == 'POST':
        # form = CompanyForm(request.POST)  # Uncomment when you have a CompanyForm
        # if form.is_valid():
        #     company = form.save()
        #     return redirect('company_detail', company_id=company.id)
        pass  # Remove this when you uncomment the above code
    else:
        # form = CompanyForm()  # Uncomment when you have a CompanyForm
        form = None  # Placeholder, replace with actual form
    return render(request, 'companies/company_details_add.html', {'form': form})

@login_required
def company_edit(request, company_id):
    # company = get_object_or_404(Company, id=company_id)  # Uncomment when you have a Company model
    company = {}  # Placeholder, replace with actual data
    if request.method == 'POST':
        # form = CompanyForm(request.POST, instance=company)  # Uncomment when you have a CompanyForm
        # if form.is_valid():
        #     company = form.save()
        #     return redirect('company_detail', company_id=company.id)
        pass  # Remove this when you uncomment the above code
    else:
        # form = CompanyForm(instance=company)  # Uncomment when you have a CompanyForm
        form = None  # Placeholder, replace with actual form
    return render(request, 'companies/company_details_edit.html', {'form': form, 'company': company})

@login_required
def company_delete(request, company_id):
    # company = get_object_or_404(Company, id=company_id)  # Uncomment when you have a Company model
    if request.method == 'POST':
        # company.delete()
        return redirect('company_list')
    return render(request, 'companies/company_details_delete.html', {'company': {}})  # Replace {} with actual company data

@login_required
def company_activity_log(request, company_id):
    # company = get_object_or_404(Company, id=company_id)  # Uncomment when you have a Company model
    # activity_logs = company.activity_logs.all()  # Assuming you have a related name for activity logs
    activity_logs = []  # Placeholder, replace with actual data
    return render(request, 'companies/company_activity_log.html', {'company': {}, 'activity_logs': activity_logs})

@login_required
def company_notes(request, company_id):
    # company = get_object_or_404(Company, id=company_id)  # Uncomment when you have a Company model
    # notes = company.notes.all()  # Assuming you have a related name for notes
    notes = []  # Placeholder, replace with actual data
    return render(request, 'companies/company_note.html', {'company': {}, 'notes': notes})

@login_required
def company_notes_add(request, company_id):
    # company = get_object_or_404(Company, id=company_id)  # Uncomment when you have a Company model
    if request.method == 'POST':
        # form = CompanyNoteForm(request.POST)  # Uncomment when you have a CompanyNoteForm
        # if form.is_valid():
        #     note = form.save(commit=False)
        #     note.company = company
        #     note.save()
        #     return redirect('company_notes', company_id=company.id)
        pass  # Remove this when you uncomment the above code
    else:
        # form = CompanyNoteForm()  # Uncomment when you have a CompanyNoteForm
        form = None  # Placeholder, replace with actual form
    return render(request, 'companies/company_notes_add.html', {'form': form, 'company': {}})

@login_required
def company_notes_edit(request, company_id, note_id):
    # company = get_object_or_404(Company, id=company_id)  # Uncomment when you have a Company model
    # note = get_object_or_404(CompanyNote, id=note_id, company=company)  # Uncomment when you have a CompanyNote model
    if request.method == 'POST':
        # form = CompanyNoteForm(request.POST, instance=note)  # Uncomment when you have a CompanyNoteForm
        # if form.is_valid():
        #     form.save()
        #     return redirect('company_notes', company_id=company.id)
        pass  # Remove this when you uncomment the above code
    else:
        # form = CompanyNoteForm(instance=note)  # Uncomment when you have a CompanyNoteForm
        form = None  # Placeholder, replace with actual form
    return render(request, 'companies/company_notes_edit.html', {'form': form, 'company': {}, 'note': {}})

@login_required
def company_notes_delete(request, company_id, note_id):
    # company = get_object_or_404(Company, id=company_id)  # Uncomment when you have a Company model
    # note = get_object_or_404(CompanyNote, id=note_id, company=company)  # Uncomment when you have a CompanyNote model
    if request.method == 'POST':
        # note.delete()
        return redirect('company_notes', company_id=company_id)
    return render(request, 'companies/company_notes_delete.html', {'company': {}, 'note': {}})
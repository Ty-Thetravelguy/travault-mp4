from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
# from .models import Ticket, TicketUpdate
# from .forms import TicketForm, TicketUpdateForm, TicketEditForm

@login_required
def ticket_list(request):
    # tickets = Ticket.objects.filter(company=request.user.company)
    tickets = []  # Placeholder
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})

@login_required
def ticket_create(request):
    if not request.user.has_perm('tickets.add_ticket'):
        raise PermissionDenied
    if request.method == 'POST':
        # form = TicketForm(request.POST)
        # if form.is_valid():
        #     ticket = form.save(commit=False)
        #     ticket.company = request.user.company
        #     ticket.created_by = request.user
        #     ticket.save()
        #     return redirect('ticket_view', ticket_id=ticket.id)
        pass
    else:
        # form = TicketForm()
        form = None  # Placeholder
    return render(request, 'tickets/ticket_create.html', {'form': form})

@login_required
def ticket_view(request, ticket_id):
    # ticket = get_object_or_404(Ticket, id=ticket_id, company=request.user.company)
    # updates = ticket.updates.all()
    ticket, updates = {}, []  # Placeholder
    if not request.user.has_perm('tickets.view_ticket'):
        raise PermissionDenied
    return render(request, 'tickets/ticket_view.html', {'ticket': ticket, 'updates': updates})

@login_required
def ticket_view_edit(request, ticket_id):
    # ticket = get_object_or_404(Ticket, id=ticket_id, company=request.user.company)
    if not request.user.has_perm('tickets.change_ticket'):
        raise PermissionDenied
    if request.method == 'POST':
        # form = TicketEditForm(request.POST, instance=ticket)
        # if form.is_valid():
        #     form.save()
        #     return redirect('ticket_view', ticket_id=ticket.id)
        pass
    else:
        # form = TicketEditForm(instance=ticket)
        form = None  # Placeholder
    return render(request, 'tickets/ticket_view_edit.html', {'form': form, 'ticket': {}})

@login_required
def ticket_add_update(request, ticket_id):
    # ticket = get_object_or_404(Ticket, id=ticket_id, company=request.user.company)
    if not request.user.has_perm('tickets.add_ticketupdate'):
        raise PermissionDenied
    if request.method == 'POST':
        # form = TicketUpdateForm(request.POST)
        # if form.is_valid():
        #     update = form.save(commit=False)
        #     update.ticket = ticket
        #     update.created_by = request.user
        #     update.save()
        #     return redirect('ticket_view', ticket_id=ticket.id)
        pass
    else:
        # form = TicketUpdateForm()
        form = None  # Placeholder
    return render(request, 'tickets/ticket_add_update.html', {'form': form, 'ticket': {}})

@login_required
def ticket_update_edit(request, ticket_id, update_id):
    # ticket = get_object_or_404(Ticket, id=ticket_id, company=request.user.company)
    # update = get_object_or_404(TicketUpdate, id=update_id, ticket=ticket)
    if not request.user.has_perm('tickets.change_ticketupdate'):
        raise PermissionDenied
    if request.method == 'POST':
        # form = TicketUpdateForm(request.POST, instance=update)
        # if form.is_valid():
        #     form.save()
        #     return redirect('ticket_view', ticket_id=ticket.id)
        pass
    else:
        # form = TicketUpdateForm(instance=update)
        form = None  # Placeholder
    return render(request, 'tickets/ticket_update_edit.html', {'form': form, 'ticket': {}, 'update': {}})

@login_required
def ticket_delete(request, ticket_id):
    # ticket = get_object_or_404(Ticket, id=ticket_id, company=request.user.company)
    if not request.user.has_perm('tickets.delete_ticket'):
        raise PermissionDenied
    if request.method == 'POST':
        # ticket.delete()
        return redirect('ticket_list')
    return render(request, 'tickets/ticket_delete.html', {'ticket': {}})
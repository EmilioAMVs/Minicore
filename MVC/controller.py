from django.shortcuts import render
from .models import Gasto, Departamento
from .forms import FiltroGastosForm
from django.db.models import Sum, Q, DecimalField
from django.db.models.functions import Coalesce

def filtrar_gastos(request):
    form = FiltroGastosForm(request.GET or None)
    resultados = []
    
    if form.is_valid():
        fecha_inicio = form.cleaned_data['fecha_inicio']
        fecha_fin = form.cleaned_data['fecha_fin']
        
        resultados = (
            Departamento.objects.all()
            .annotate(
                total=Coalesce(
                    Sum(
                        'gasto__monto',
                        filter=Q(gasto__fecha__range=[fecha_inicio, fecha_fin])
                    ),
                    0,
                    output_field=DecimalField()
                )
            )
            .order_by('-total')
        )
    return render(request, 'filtrar_gastos.html', {'form': form, 'resultados': resultados})

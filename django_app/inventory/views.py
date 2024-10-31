from django.shortcuts import render
from .models import Supplier, Material, Delivery


def index(request):
    suppliers = Supplier.objects.all()
    materials = Material.objects.all()
    deliveries = Delivery.objects.all()
    return render(
        request,
        "index.html",
        {
            "suppliers": suppliers,
            "materials": materials,
            "deliveries": deliveries,
        },
    )

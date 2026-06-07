from django.shortcuts import render, redirect

from .forms import KursArizaForm
from .models import KursAriza


def ariza(request):

    if request.method == "POST":

        form = KursArizaForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            KursAriza.objects.create(
                toliq_ism=data["toliq_ism"],
                telefon=data["telefon"],
                yosh=data["yosh"],
                yonalish=data["yonalish"],
                tajriba_bor=data["tajriba_bor"],
                qoshimcha=data["qoshimcha"]
            )

            return redirect("ariza")

    else:
        form = KursArizaForm()

    return render(
        request,
        "ariza.html",
        {
            "form": form
        }
    )
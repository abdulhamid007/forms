from django import forms

YONALISHLAR = [
    ('back', 'Backend'),
    ('fro', 'Frontend'),
    ('diz', 'Dizayn'),
]


class KursArizaForm(forms.Form):

    toliq_ism = forms.CharField(
        label="To'liq ism",
        max_length=100,
        widget=forms.TextInput(
            
        )
    )

    telefon = forms.CharField(
        label="Telefon",
        help_text="Masalan: +998901234567",
        widget=forms.TextInput(
           
        )
    )

    yosh = forms.IntegerField(
        label="Yosh"
    )

    yonalish = forms.ChoiceField(
        label="Yo'nalish",
        choices=YONALISHLAR
    )

    tajriba_bor = forms.BooleanField(
        label="Dasturlash tajribangiz bormi?",
        required=False
    )

    qoshimcha = forms.CharField(
        label="Qo'shimcha izoh",
        required=False,
        widget=forms.Textarea(
                
        )
    )

    def clean_yosh(self):
        yosh = self.cleaned_data["yosh"]

        if yosh < 14:
            raise forms.ValidationError(
                "Yosh kamida 14 bo'lishi kerak."
            )

        return yosh

    def clean(self):
        data = super().clean()

        yonalish = data.get("yonalish")
        tajriba = data.get("tajriba_bor")
        qoshimcha = data.get("qoshimcha")

        if yonalish == "backend" and not tajriba:
            if not qoshimcha:
                raise forms.ValidationError(
                    "Backend yo'nalishiga tajribasiz yozilsangiz, sababini yozing."
                )

        return data
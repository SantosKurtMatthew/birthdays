from django import forms
from .models import Birthday


class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        fields = ['name', 'date']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class':'bg-white w-4/5 mb-4 relative left-1/10 text-[32px] flex justify-center text-center',
                    'placeholder':'name'
                }
            ),
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class':'bg-white w-4/5 mb-4 relative left-1/10 text-[32px] flex justify-center'
                },
            ),
        }

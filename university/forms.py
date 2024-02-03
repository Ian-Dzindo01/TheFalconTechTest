from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['broj', 'ime', 'prezime', 'email', 'prosjek', 'datum', 'ocijena_mature', 'mjesto', 'molba', 'doc', 'smijer']
        labels = {
            'broj':'Broj Studenta',
            'ime':'Ime',
            'prezime':'Prezime',
            'email':'Email',
            'prosjek':'Prosijek Ocijena',
            'datum': 'Datum Rodjenja',
            'ocijena_mature': 'Ocijena na maturi',
            'mjestoRodj': 'Mijesto rodjenja',
            'molba': 'Molba za upis',
            'doc': 'Dokument o zavrsenoj srednjoj skoli',
            'smijer': 'Odaberite smijer'
        }
        study_choices = [
            ('Informatički', 'Informatički'),
            ('Tehnički', 'Tehnički'),
            ('Matematički', 'Matematički')]
        widgets = {
                'broj':forms.NumberInput(attrs={'class':'form-control'}), 
                'ime':forms.TextInput(attrs={'class':'form-control'}), 
                'prezime':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),
                'prosjek':forms.NumberInput(attrs={'class':'form-control'}),
                'datum':forms.DateInput(attrs={'class':'form-control'}),
                'ocijena_mature': forms.NumberInput(attrs={'class':'form-control'}),
                'mjesto': forms.TextInput(attrs={'class':'form-control'}),
                'molba': forms.TextInput(attrs={'class':'form-control'}),
                'doc': forms.FileInput(attrs={'class': 'form-control'}),
                'smijer':forms.ChoiceField(choices=study_choices, widget=forms.Select(attrs={'class': 'form-control'}))
        }
from django import forms
from .models import Student, FieldOfStudy

class StudentForm(forms.ModelForm):
    smijer = forms.ModelChoiceField(queryset=FieldOfStudy.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))         # MOVE THIS BELOW WITH THE OTHERS
    doc = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Student
        fields = ['broj', 'ime', 'prezime', 'email', 'skola', 'prosjek', 'datum', 'ocijena_mature', 'mjesto', 'molba', 'smijer', 'doc']
        labels = {
            'broj':'Broj Studenta',
            'ime':'Ime',
            'prezime':'Prezime',
            'email':'Email',
            'skola': 'Skola',
            'prosjek':'Prosijek Ocijena',
            'datum': 'Datum Rodjenja',
            'ocijena_mature': 'Ocijena na maturi',
            'mjesto': 'Mjesto rodjenja',
            'molba': 'Molba za upis',
            'smijer': 'Odaberite smijer',
            'doc': 'Dokument of zavrsenoj srednjoj skoli'
        }
        
        widgets = {
                'broj':forms.NumberInput(attrs={'class':'form-control'}), 
                'ime':forms.TextInput(attrs={'clas  s':'form-control'}), 
                'prezime':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),
                'skola':forms.TextInput(attrs={'class':'form-control'}),
                'prosjek':forms.NumberInput(attrs={'class':'form-control'}),
                'datum':forms.DateInput(attrs={'class':'form-control'}),
                'ocijena_mature': forms.NumberInput(attrs={'class':'form-control'}),
                'mjesto': forms.TextInput(attrs={'class':'form-control'}),
                'molba': forms.TextInput(attrs={'class':'form-control'}),
                'doc': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
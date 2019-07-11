from django import forms


from firstapp.models import user

class newuserform(forms.ModelForm):
    class Meta():
        model=user
        fields='__all__'
from django import forms

class HomeForm(forms.Form):
    #In HTML, a form is a collection of elements inside <form>...</form> that allow a visitor to do
    # things like enter text, select options, manipulate objects or controls,
    # and so on, and then send that information back to the server.
    post = forms.CharField()#Criando um formulário de campo de texto


from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': "col-lg-6 col-md-6 col-sm-12 form-group", 'placeholder': "Name", "aria-required": True}))

    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': "col-lg-6 col-md-6 col-sm-12 form-group", 'placeholder': "Email"}))

    phone = forms.IntegerField(required=False, widget=forms.TextInput(
        attrs={'class': "col-lg-6 col-md-6 col-sm-12 form-group", 'placeholder': "Phone"}))

    # name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(
    #     attrs={'class': "col-lg-6 col-md-6 col-sm-12 form-group", 'placeholder': "Name"}))

    # name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(
    #     attrs={'class': "col-lg-6 col-md-6 col-sm-12 form-group", 'placeholder': "Name"}))

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields["name"].label = ""
        self.fields["email"].label = ""
        self.fields["phone"].label = ""

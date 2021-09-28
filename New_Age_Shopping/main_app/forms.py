from django import forms
from .models import Comment
from phonenumber_field.formfields import PhoneNumberField

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)

DISTRICT_CHOICES ={
    ('Pokhara', 'Pokhara'),
    ('Sunsari', 'Sunsari'),
    ('Jhapa', 'Jhapa'),
    ('Kathmandu', 'Kathmandu'),
}
class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length= 20, required= False, widget=forms.TextInput(attrs=
        {'class':'form_control_section',  'id':'input_firstname', 'placeholder':'First Name'}))
    last_name = forms.CharField(max_length= 20, required= False,widget=forms.TextInput(attrs=
        {'class':'form_control_section',  'id':'input_lastname', 'placeholder':'Last Name'}))
    phone_number = PhoneNumberField(help_text = "Required: +977-",required=False, widget=forms.TextInput(attrs=
        { 'type': 'number', 'class':'form_control_section','value': '+977-',  'id':'input_phonename', 'placeholder':'Phone Number'}))
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs=
        {'class':'form_control_section',  'id':'input_email', 'placeholder':'someone@email.com'}))
    # shipping_country = CountryField(blank_label='(select country)').formfield(
    #     required=False,
    #     widget=CountrySelectWidget(attrs={
    #         'class': 'custom-select d-block w-100',
    #     }))
    shipping_district = forms.ChoiceField(required=False, widget= forms.Select(attrs=
        {'class':'form_control_section',  'value':'Regions', 'id':'regions'}), choices= DISTRICT_CHOICES)
    shipping_address = forms.CharField(required=False, widget=forms.TextInput(attrs=
        {'class':'form_control_section',  'id':'input_address', 'placeholder':'Address'}))
    shipping_zip = forms.CharField(required=False, widget=forms.TextInput(attrs=
        {'class':'form_control_section',  'id':'input_address', 'placeholder':'Address'}))
    # same_billing_address = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


# Comment forms
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']
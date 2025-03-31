from django import forms

class QRCodeForm(forms.Form):
    restaurant_name = forms.CharField(max_length=50,
                                      label='Restaurant Name',
                                      widget=forms.TextInput(
                                          attrs={
                                              'class':'form-control',
                                              'placeholder':'Enter Restraurant name'
                                          }
                                      )
                                      )
    url = forms.URLField(max_length=256,
                         label="Menu URL",
                         widget=forms.URLInput(
                             attrs={
                                 'class':'form-control',
                                 'placeholder':'Enter the URL of online Menu exp google drive'
                             }
                         )
                         )
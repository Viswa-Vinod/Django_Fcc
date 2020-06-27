from django import forms
from .models import Product

# The similarities between forms.Form and forms.ModelForm are that they both generate sets of form inputs using widgets, 
# and both validate data sent by the browser. The differences are that ModelForm 
# gets its field definition from a specified model class, and also has methods that deal 
# with saving of the underlying model to the database.
# If your form is going to be used to directly add or edit a Django model, 
# you can use a ModelForm to avoid duplicating your model description.
class ProductForm(forms.ModelForm):
    # this will override what comes in by default with a django form
    # you dont need this if you like the defaults
    title       =   forms.CharField(label='', widget=forms.TextInput(attrs={
                                        "placeholder": "Product Title"
                                    })) #no label for this field
    description =   forms.CharField(required=False, widget=forms.Textarea(
                        attrs={
                            "class": "desc-text",
                            "rows": 5,
                            "cols": 100,
                            "placeholder": "Product Description"
                        }
                    )) #True is the default
    price       =   forms.DecimalField(initial=100.50)
    
    class Meta:
        model = Product
        fields = ['title', 'description', 'price']
    
    # custom validation method
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not 'smpl' in title:
            raise forms.ValidationError("Invalid title. Title must have smpl string in it")
        if len(title) < 6:
            raise forms.ValidationError("Invalid title. Title must be atleast 6 chars in length")
        return title
        

# standard django form that is useful in cases where your form may not directly interact with the db
class RawProductForm(forms.Form):
    title       =   forms.CharField(label='', widget=forms.TextInput(attrs={
                                        "placeholder": "Product Title"
                                    })) #no label for this field
    description =   forms.CharField(required=False, widget=forms.Textarea(
                        attrs={
                            "class": "desc-text",
                            "rows": 5,
                            "cols": 100,
                            "placeholder": "Product Description"
                        }
                    )) #True is the default
    price       =   forms.DecimalField(initial=100.50)

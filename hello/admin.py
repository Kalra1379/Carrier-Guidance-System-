from django.contrib import admin

# Register your models here.
from  hello.models import Marks
from  hello.models import Contact
from  hello.models import User
# Register your models here.
admin.site.register(Marks)
admin.site.register(User)
admin.site.register(Contact)

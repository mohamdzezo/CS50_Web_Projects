from django.contrib import admin
from auctions.models import *
# Register your models here.
admin.site.register(User)
admin.site.register(listings)
admin.site.register(comments)
admin.site.register(bids)
admin.site.register(watch_list)

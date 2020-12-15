from django.contrib import admin
from mainsite.models import Post, AccessInfo, Branch, StoreIncome, Kindergarten, SchoolStu


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

admin.site.register(Post, PostAdmin)
admin.site.register(AccessInfo)

class BranchAdmin(admin.ModelAdmin):
    list_display = ('shop_name', 'boss_name')
admin.site.register(Branch, BranchAdmin)

class StoreIncomeAdmin(admin.ModelAdmin):
    list_display = ('branch','income_year', 'income_month', 'income')
admin.site.register(StoreIncome, StoreIncomeAdmin)

class KindergartenAdmin(admin.ModelAdmin):
    list_display = ('president','branch_school')
admin.site.register(Kindergarten, KindergartenAdmin)

class SchoolStuAdmin(admin.ModelAdmin):
    list_display = ('kindergarten','recruit_year','recruit_num')
admin.site.register(SchoolStu, SchoolStuAdmin)






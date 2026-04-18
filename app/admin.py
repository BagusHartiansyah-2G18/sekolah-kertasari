from django.contrib import admin 
from django.utils.html import format_html
from django.urls import path, reverse
from django.shortcuts import render, redirect
from django import forms

from .models import Informasi, ContactMessage


# =========================
# 🔥 INFORMASI FORM
# =========================
class InformasiAdminForm(forms.ModelForm):
    keterangan = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 3,
            'style': 'width:100%; min-width:300px;'
        })
    )

    class Meta:
        model = Informasi
        fields = '__all__'


# =========================
# 🔥 FORM UPLOAD GAMBAR
# =========================
class UploadGambarForm(forms.Form):
    gambar = forms.ImageField(label="Pilih gambar baru")


# =========================
# 🔥 ADMIN INFORMASI
# =========================
@admin.register(Informasi)
class InformasiAdmin(admin.ModelAdmin):

    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }

    form = InformasiAdminForm

    list_display = (
        'kategori', 
        'judul', 
        'keterangan',
        'preview_gambar',
        'aksi_update'
    )

    list_filter = ('kategori',)
    search_fields = ('judul', 'keterangan')
    list_per_page = 10

    list_display_links = ('kategori',)
    list_editable = ('judul', 'keterangan')

    # 🔥 CUSTOM URL
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'update-gambar/<int:pk>/',
                self.admin_site.admin_view(self.update_gambar_single),
                name='update-gambar-single',
            ),
        ]
        return custom_urls + urls

    # 🔥 BUTTON
    def aksi_update(self, obj):
        url = reverse('admin:update-gambar-single', args=[obj.id])
        return format_html(
            '<a style="background:#6A8F6B;color:white;padding:5px 10px;'
            'border-radius:5px;text-decoration:none;" href="{}">New Image</a>',
            url
        )

    aksi_update.short_description = "Aksi"

    # 🔥 VIEW UPDATE GAMBAR
    def update_gambar_single(self, request, pk):
        obj = Informasi.objects.get(pk=pk)

        if request.method == "POST":
            form = UploadGambarForm(request.POST, request.FILES)
            if form.is_valid():
                obj.gambar = form.cleaned_data['gambar']
                obj.save()

                self.message_user(request, "Gambar berhasil diperbarui!")
                return redirect("../../")
        else:
            form = UploadGambarForm()

        return render(request, "admin/update_gambar_single.html", {
            "form": form,
            "obj": obj,
            "title": "Update Gambar"
        })

    readonly_fields = ('preview_gambar',)

    fieldsets = (
        ('Informasi', {
            'fields': ('kategori', 'judul', 'keterangan')
        }), 
        ('Media', {
            'fields': ('gambar', 'preview_gambar')
        }),
    )

    def preview_gambar(self, obj):
        if obj.gambar:
            return format_html(
                '<a href="{}" target="_blank">'
                '<img src="{}" width="100" style="border-radius:8px;" />'
                '</a>',
                obj.gambar.url,
                obj.gambar.url
            )
        return "-"
    
    preview_gambar.short_description = 'Preview'


# =========================
# 🔥 CONTACT FORM (TEXTAREA BESAR)
# =========================
class ContactMessageAdminForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = '__all__'
        widgets = {
            'message': forms.Textarea(attrs={
                'rows': 12,
                'style': 'width:100%; height:250px; padding:10px;'
            })
        }


# =========================
# 🔥 ADMIN CONTACT MESSAGE
# =========================
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    form = ContactMessageAdminForm

    list_display = ('name', 'email', 'subject', 'short_message', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)

    # 🔥 hanya preview di list
    def short_message(self, obj):
        return obj.message[:60] + '...' if len(obj.message) > 60 else obj.message

    short_message.short_description = "Message"

    # =========================
    # 🔒 HANYA SUPERUSER BISA DELETE
    # =========================
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    # 🔒 MATIKAN BULK DELETE
    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.is_superuser:
            actions.pop('delete_selected', None)
        return actions

        
# from django.contrib import admin 
# from django.utils.html import format_html
# from django.urls import path, reverse
# from django.shortcuts import render, redirect
# from django import forms

# from .models import Informasi
# from .models import ContactMessage



# # 🔥 FORM TEXTAREA (INI KUNCI UTAMA)
# class InformasiAdminForm(forms.ModelForm):
#     keterangan = forms.CharField(
#         widget=forms.Textarea(attrs={
#             'rows': 3,
#             'style': 'width:100%; min-width:300px;'
#         })
#     )

#     class Meta:
#         model = Informasi
#         fields = '__all__'


# # 🔥 FORM UPLOAD GAMBAR
# class UploadGambarForm(forms.Form):
#     gambar = forms.ImageField(label="Pilih gambar baru")


# @admin.register(Informasi)
# class InformasiAdmin(admin.ModelAdmin):

#     class Media:
#         css = {
#             'all': ('admin/css/custom_admin.css',)
#         }
#     form = InformasiAdminForm  # 🔥 WAJIB untuk textarea

#     # 🔥 LIST VIEW (pakai keterangan asli, bukan short)
#     list_display = (
#         'kategori', 
#         'judul', 
#         'keterangan',  # 🔥 penting
#         'preview_gambar',
#         'aksi_update'
#     )

#     list_filter = ('kategori',)
#     search_fields = ('judul', 'keterangan')
#     list_per_page = 10

#     list_display_links = ('kategori',)  # 🔥 biar tidak konflik
#     list_editable = ('judul', 'keterangan')

#     # 🔥 URL CUSTOM
#     def get_urls(self):
#         urls = super().get_urls()
#         custom_urls = [
#             path(
#                 'update-gambar/<int:pk>/',
#                 self.admin_site.admin_view(self.update_gambar_single),
#                 name='update-gambar-single',
#             ),
#         ]
#         return custom_urls + urls

#     # 🔥 TOMBOL UPDATE GAMBAR
#     def aksi_update(self, obj):
#         url = reverse('admin:update-gambar-single', args=[obj.id])
#         return format_html(
#             '<a style="background:#6A8F6B;color:white;padding:5px 10px;'
#             'border-radius:5px;text-decoration:none;" href="{}">New Image</a>',
#             url
#         )

#     aksi_update.short_description = "Aksi"

#     # 🔥 VIEW UPDATE GAMBAR
#     def update_gambar_single(self, request, pk):
#         obj = Informasi.objects.get(pk=pk)

#         if request.method == "POST":
#             form = UploadGambarForm(request.POST, request.FILES)
#             if form.is_valid():
#                 obj.gambar = form.cleaned_data['gambar']
#                 obj.save()

#                 self.message_user(request, "Gambar berhasil diperbarui!")
#                 return redirect("../../")
#         else:
#             form = UploadGambarForm()

#         return render(request, "admin/update_gambar_single.html", {
#             "form": form,
#             "obj": obj,
#             "title": "Update Gambar"
#         })

#     # 🔥 DETAIL FORM
#     readonly_fields = ('preview_gambar',)

#     fieldsets = (
#         ('Informasi', {
#             'fields': ('kategori', 'judul', 'keterangan')
#         }), 
#         ('Media', {
#             'fields': ('gambar', 'preview_gambar')
#         }),
#     )

#     # 🔥 PREVIEW GAMBAR
#     def preview_gambar(self, obj):
#         if obj.gambar:
#             return format_html(
#                 '<a href="{}" target="_blank">'
#                 '<img src="{}" width="100" style="border-radius:8px;" />'
#                 '</a>',
#                 obj.gambar.url,
#                 obj.gambar.url
#             )
#         return "-"
    
#     preview_gambar.short_description = 'Preview'

# class ContactMessageAdminForm(forms.ModelForm):
#     class Meta:
#         model = ContactMessage
#         fields = '__all__'
#         widgets = {
#             'message': forms.Textarea(attrs={
#                 'rows': 12,
#                 'style': 'width: 100%; font-size:14px; padding:10px;'
#             })
#         }


# @admin.register(ContactMessage)
# class ContactMessageAdmin(admin.ModelAdmin):
#     form = ContactMessageAdminForm

#     list_display = ('name', 'email', 'subject', 'short_message', 'created_at')
#     search_fields = ('name', 'email', 'subject')
#     list_filter = ('created_at',)

#     def short_message(self, obj):
#         return obj.message

#     short_message.short_description = "Message"
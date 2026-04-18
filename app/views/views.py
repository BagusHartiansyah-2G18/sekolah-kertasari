from django.shortcuts import render,redirect
from app.views.sf.SFdata import Dinformasi,dataFrameToJson

from django.contrib import messages
from app.forms  import ContactForm
from app.utils import is_spam, get_client_ip

def home(request): 
    _ = Dinformasi()
    # _.updKategori(12,"medsos")
    context = {
        'app': dataFrameToJson(_.get_by_kategori("app")),
        'tagline': dataFrameToJson(_.get_by_kategori("tagline")),
        'pendaftaran': dataFrameToJson(_.get_by_kategori("pendaftaran")),
        'images': dataFrameToJson(_.images()),
        'alamat': dataFrameToJson(_.get_by_kategori("alamat")),
        'medsos': dataFrameToJson(_.get_by_kategori("medsos")),
    }
    return render(request, 'home.html', context)

def about(request): 
    _ = Dinformasi()
    # _.updKategori(19,"brandcontent")
    context = {
        'app': dataFrameToJson(_.get_by_kategori("app")),
        'tagline': dataFrameToJson(_.get_by_kategori("tagline")),
        'pendaftaran': dataFrameToJson(_.get_by_kategori("pendaftaran")),
        'images': dataFrameToJson(_.images()),
        'alamat': dataFrameToJson(_.get_by_kategori("alamat")),
        'medsos': dataFrameToJson(_.get_by_kategori("medsos")),
        'visi': dataFrameToJson(_.get_by_kategori("visi")),
        'brandcontent': dataFrameToJson(_.get_by_kategori("brandcontent")),
        'lead': dataFrameToJson(_.get_by_kategori("lead")),
    }
    return render(request, 'about.html', context)

def programs(request): 
    _ = Dinformasi()
    # _.updKategori(30,"program")
    context = {
        'app': dataFrameToJson(_.get_by_kategori("app")),
        'tagline': dataFrameToJson(_.get_by_kategori("tagline")),
        'pendaftaran': dataFrameToJson(_.get_by_kategori("pendaftaran")),
        'images': dataFrameToJson(_.images()),
        'alamat': dataFrameToJson(_.get_by_kategori("alamat")),
        'medsos': dataFrameToJson(_.get_by_kategori("medsos")),
        'program': dataFrameToJson(_.get_by_kategori("program")),
    }
    return render(request, 'programs.html', context)

def faq(request): 
    _ = Dinformasi()
    # _.updKategori(30,"program")
    context = {
        'app': dataFrameToJson(_.get_by_kategori("app")),
        'tagline': dataFrameToJson(_.get_by_kategori("tagline")),
        'pendaftaran': dataFrameToJson(_.get_by_kategori("pendaftaran")),
        'images': dataFrameToJson(_.images()),
        'alamat': dataFrameToJson(_.get_by_kategori("alamat")),
        'medsos': dataFrameToJson(_.get_by_kategori("medsos")),
        'faq': dataFrameToJson(_.get_by_kategori("faq")),
    }
    return render(request, 'faq.html', context)






def contact(request):
    form = ContactForm()

    if request.method == "POST":

        # 🔒 cek spam hanya saat POST
        if is_spam(request):
            messages.error(request, "Terlalu banyak request, coba lagi nanti.")
            return redirect("contact")

        form = ContactForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)

            # simpan IP
            obj.ip_address = get_client_ip(request)
            obj.save()

            messages.success(request, "Pesan berhasil dikirim!")
            return redirect("contact")

        else:
            messages.error(request, "Form tidak valid, cek kembali.")

    # ambil data lain (tetap jalan walau GET / error form)
    _ = Dinformasi()

    context = {
        'form': form,  # 🔥 penting!
        'app': dataFrameToJson(_.get_by_kategori("app")),
        'tagline': dataFrameToJson(_.get_by_kategori("tagline")),
        'pendaftaran': dataFrameToJson(_.get_by_kategori("pendaftaran")),
        'images': dataFrameToJson(_.images()),
        'alamat': dataFrameToJson(_.get_by_kategori("alamat")),
        'medsos': dataFrameToJson(_.get_by_kategori("medsos")),
    }

    return render(request, 'contact.html', context)

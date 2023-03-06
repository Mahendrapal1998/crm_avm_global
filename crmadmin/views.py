from django.shortcuts import render,redirect
from . models import Leads,Accounts,Tasks,Meetings,Products,Quotes,Invoices
from django.http import HttpResponse

def login(req):
    return render(req,'login.html')
def admin(req):
    leads=Leads.objects.all()
    accounts=Accounts.objects.all()
    tasks=Tasks.objects.all()
    meetings=Meetings.objects.all()
    products=Products.objects.all()
    quotes=Quotes.objects.all()
    invoices=Invoices.objects.all()
    return render(req,'admin.html',{"leads":leads,"accounts":accounts,"tasks":tasks,"meetings":meetings,"products":products,"quotes":quotes,"invoices":invoices})
def leads(req):
    leads=Leads.objects.all()
    return render(req,'leads.html',{"leads":leads})
def addlead(req):
    return render(req,'addlead.html')
def leadview(req):
    id=req.GET.get("id")
    leads=Leads.objects.filter(id=id)
    return render(req,'leadview.html',{"leads":leads})
def editlead(req):
    id=req.GET.get("id")
    leads=Leads.objects.filter(id=id)
    return render(req,'editlead.html',{"leads":leads})
def savelead(req):
    save=req.GET.get("save")
    lead_owner=req.GET.get("lead_owner")
    fname=req.GET.get("fname")
    email=req.GET.get("email")
    visa_exp_date=req.GET.get("visa_exp_date")
    lead_source=req.GET.get("lead_source")
    title=req.GET.get("title")
    lname=req.GET.get('lname')
    phone=req.GET.get("phone")
    visa_preference=req.GET.get("visa_preference")
    rating=req.GET.get("rating")
    address=req.GET.get("address")
    city=req.GET.get("city")
    state=req.GET.get("state")
    post_code=req.GET.get("post_code")
    country=req.GET.get("country")
    enquiry_type=req.GET.get("enquiry_type")
    leads=Leads()
    leads.fname=fname
    leads.lname=lname
    leads.email=email
    leads.phone=phone
    leads.title=title
    leads.visa_expiry=visa_exp_date
    leads.lead_owner=lead_owner
    leads.visa_preference=visa_preference
    leads.lead_source=lead_source
    leads.rating=rating
    leads.address=address
    leads.city=city
    leads.state=state
    leads.post_code=post_code
    leads.country=country
    leads.enquiry_type=enquiry_type
    leads.save()
    if save=="savenew":
        return redirect("/crmadmin/addlead")
    elif save=="save":
        return redirect("/crmadmin/leads")
def clients(req):
    clients=Leads.objects.all()
    return render(req,'clients.html',{"clients":clients})
def saveeditlead(req):
    save=req.GET.get("save")
    id=req.GET.get("id")
    lead_owner=req.GET.get("lead_owner")
    fname=req.GET.get("fname")
    email=req.GET.get("email")
    title=req.GET.get("title")
    visa_exp_date=req.GET.get("visa_exp_date")
    lead_source=req.GET.get("lead_source")
    lname=req.GET.get('lname')
    phone=req.GET.get("phone")
    visa_preference=req.GET.get("visa_preference")
    rating=req.GET.get("rating")
    address=req.GET.get("address")
    city=req.GET.get("city")
    state=req.GET.get("state")
    post_code=req.GET.get("post_code")
    country=req.GET.get("country")
    enquiry_type=req.GET.get("enquiry_type")
    leads=Leads.objects.filter(id=id)
    for update in leads:
        update.fname=fname
        update.lname=lname
        update.email=email
        update.phone=phone
        update.title=title
        update.visa_expiry=visa_exp_date
        update.lead_owner=lead_owner
        update.visa_preference=visa_preference
        update.lead_source=lead_source
        update.rating=rating
        update.address=address
        update.city=city
        update.state=state
        update.post_code=post_code
        update.country=country
        update.enquiry_type=enquiry_type
        update.save()
    if save=="savenew":
        return redirect("/crmadmin/addlead")
    elif save=="save":
        return redirect("/crmadmin/leads")
def institute(req):
    return render(req,'institute.html')
def addinstitute(req):
    return render(req,'addinstitute.html')
def courses(req):
    return render(req,'courses.html')
def addcourses(req):
    return render(req,'addcourses.html')
def user(req):
    return render(req,'user.html')
def adduser(req):
    return render(req,'adduser.html')
def task(req):
    tasks=Tasks.objects.all()
    return render(req,'task.html',{"tasks":tasks})
def addtask(req):
    return render(req,'addtask.html')
def products(req):
    products=Products.objects.all()
    return render(req,'products.html',{"products":products})
def addproduct(req):
    return render(req,'addproduct.html')
def newsletter(req):
    return render(req,'newsletter.html')
def accounts(req):
    accounts=Accounts.objects.all()
    return render(req,'accounts.html',{"accounts":accounts})
def meetings(req):
    meetings=Meetings.objects.all()
    return render(req,'meetings.html',{"meetings":meetings})
def quotes(req):
    quotes=Quotes.objects.all()
    return render(req,'quotes.html',{"quotes":quotes})
def invoices(req):
    invoices=Invoices.objects.all()
    return render(req,'invoices.html',{"invoices":invoices})
def upload(req):
    if req.method=="POST":
        file=req.FILES("file")
        document=FilesUpload.object.create(file=file)
        document.save()
        return HttpResponse("file uploaded")
    return render(req,"admin.html")
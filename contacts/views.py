from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views import generic

from .models import Contact


class ContactView(generic.View):

    def post(self, request, *args, **kwargs):
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, 'You have already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name,
                          email=email, phone=phone, message=message, user_id=user_id)
        contact.save()

        # Send email
        send_mail(
            subject='Property Listing Inquiry',
            message='There has been an inquiry for ' + listing +
            '. Sign into the admin panel for more info.',
            from_email='hjchoi_89@naver.com',
            recipient_list=[realtor_email, 'jaychoi1619@gmail.com'],
            fail_silently=False
        )

        messages.success(
            request, 'Your request has been submitted, a realtor will get back to you ASAP')

        return redirect('/listings/'+listing_id)

from urllib.parse import urlencode

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, RedirectView, TemplateView

from .forms import CustomerRegistrationForm, VendorRegistrationForm
from .models import User


class CustomerRegisterView(CreateView):
    model = User
    form_class = CustomerRegistrationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("shop:home")

    def form_valid(self, form):
        response = super().form_valid(form)
        from django.contrib.auth import login

        login(self.request, self.object)
        return response


class VendorRegisterView(CreateView):
    model = User
    form_class = VendorRegistrationForm
    template_name = "accounts/vendor_register.html"
    success_url = reverse_lazy("dashboard:home")

    def form_valid(self, form):
        response = super().form_valid(form)
        from django.contrib.auth import login

        login(self.request, self.object)
        return response


class CustomerLoginView(auth_views.LoginView):
    """
    One login form for everyone.
    - **Users** (shoppers): open Login or Sign up — after login, home / checkout `next`.
    - **Admin** (is_staff): use the Admin link or `/accounts/login/?next=/manage/`.
    Sellers (is_vendor) who sign in without `next` go to the seller dashboard.
    """

    template_name = "accounts/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        redirect_to = super().get_redirect_url()
        user = self.request.user
        if (
            redirect_to
            and "/manage" in redirect_to
            and not user.is_staff
        ):
            messages.warning(
                self.request,
                "That account cannot open Admin. Use an administrator username "
                "(e.g. from createsuperuser), or use User login for shopping.",
            )
            return reverse("shop:home")
        return redirect_to or self.get_default_redirect_url()

    def get_default_redirect_url(self):
        """When `next` is absent: staff → admin panel, sellers → dashboard, others → shop."""
        user = self.request.user
        if user.is_staff:
            return reverse("staff_admin:home")
        if getattr(user, "is_vendor", False):
            return reverse("dashboard:home")
        return reverse("shop:home")


class VendorLoginRedirectView(RedirectView):
    """Old seller URL -> same login page, then redirect to dashboard."""

    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        return f"{reverse('accounts:login')}?{urlencode({'next': reverse('dashboard:home')})}"


class LogoutView(View):
    """
    Log out via GET or POST. Django's built-in LogoutView often returns 405 on GET
    (logout links in the navbar use GET).
    """

    def get(self, request):
        logout(request)
        messages.info(request, "You have been logged out.")
        return redirect(reverse("shop:home"))

    def post(self, request):
        return self.get(request)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"

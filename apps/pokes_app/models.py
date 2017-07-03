from __future__ import unicode_literals
from django.db import models
import bcrypt

class UserManager(models.Manager):
    def validate(self, form_data):
        errors = []

        if len(form_data['first_name']) == 0:
            errors.append("First Name is required.")
        if len(form_data['last_name']) == 0:
            errors.append("Last Name is required.")
        if len(form_data['email']) == 0:
            errors.append("Email is required.")
        if len(form_data['password']) == 0:
            errors.append("Password is required.")
        if form_data['password'] != form_data['password_confirmation']:
            errors.append("Password confirmation must match password.")

        return errors

    def validate_login(self, form_data):
        errors = []

        if len(form_data['email']) == 0:
            errors.append("Email is required.")
        if len(form_data['password']) == 0:
            errors.append("Password is required.")

        return errors

    def login(self, form_data):
        errors = self.validate_login(form_data)

        if not errors:
            user = User.objects.filter(email=form_data['email']).first()

            if user:
                password = str(form_data['password'])
                user_password = str(user.password)

                hashed_pw = bcrypt.hashpw(password, user_password)
                if user.password == hashed_pw:
                    return user

            errors.append('Invalid Account Information')

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    friends = models.ManyToManyField("self", related_name = "befriended")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #Overload User objects attribute
    objects = UserManager()

    #When User in used in string context.
    def __str__(self):
        string_output =  "id: {} first_name: {} last_name: {} email: {} password: {}"

        return string_output.format(
            self.id,
            self.first_name,
            self.last_name,
            self.email,
            self.password,
        )

class Poke(models.Model):
    poker = models.ForeignKey(User, related_name="poked")
    pokee = models.ForeignKey(User, related_name="poked_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #When Poke is used in string context.
    def __str__(self):
        str_output = "Poker: {} Pokee: {}"
        
        return str_output.format(
            self.poker.id,
            self.pokee.id,
        )





from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from Market.models import User


class RegisterForm(FlaskForm):

    def validate_username(self, username_chack):
        # Check if username already exists in the database
        user = User.query.filter_by(username=username_chack.data).first()
        if user:
            raise ValidationError(
                "Username already exists!, Please try Diffrent Username"
            )

    def validate_email(self, email_chack):
        # Check if email already exists in the database
        email = User.query.filter_by(email=email_chack.data).first()
        if email:
            raise ValidationError(
                "Email Address already exists!, Please try Diffrent Email Address"
            )

    username = StringField(
        label="Username :", validators=[Length(min=2, max=30), DataRequired()]
    )
    email = StringField(label="Email :", validators=[Email(), DataRequired()])
    password1 = PasswordField(
        label="Password :", validators=[Length(min=6), DataRequired()]
    )
    password2 = PasswordField(
        label="Confirm Password :", validators=[EqualTo("password1"), DataRequired()]
    )
    submit = SubmitField(label="Create Account")


class LoginForm(FlaskForm):
    username = StringField(label="Username : ", validators=[DataRequired()])
    password = PasswordField(label='Password : ', validators=[DataRequired()])
    submit = SubmitField(label="Sign in")


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label="Perchase Item!")


class SellItemForm(FlaskForm):
    submit = SubmitField(label="Sell Item!")

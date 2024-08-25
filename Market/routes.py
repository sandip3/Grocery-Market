from Market import app, db
from Market.models import Item, User
from flask import render_template, redirect, url_for, flash, request
from Market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
from flask_login import login_user, logout_user, login_required, current_user


@app.route("/")
@app.route("/home")
def Home_Page():
    return render_template("HomePage.html")


@app.route("/market", methods=["GET", "POST"])
@login_required
def market_page():

    purchase_form = PurchaseItemForm()
    selling_form = SellItemForm()

    if request.method == "POST":

        # Purchase Item Logic
        purchase_item = request.form.get("purchase_item")
        purchase_item_object = Item.query.filter_by(name=purchase_item).first()

        if purchase_item_object:
            if current_user.can_purchase(purchase_item_object):

                purchase_item_object.buy(current_user)
                flash(
                    f"Congratulations! You have purchased {purchase_item_object.name} for {purchase_item_object.price}₹",
                    category="success",
                )

            else:
                flash(
                    f"Unfortunately, you don't have enough Balance to Purchase {purchase_item_object.name}",
                    category="danger",
                )
                flash(
                    "Insufficient Balance, Please Recharge Balance", category="danger"
                )

            # Sell Item Logic
        sold_item = request.form.get("sold_item")
        sold_item_object = Item.query.filter_by(name=sold_item).first()

        if sold_item:
            if current_user.can_sell(sold_item_object):
                sold_item_object.sell(current_user)
                flash(
                    f"Congratulations! You have Sold {sold_item_object.name} back to market!",
                    category="success",
                )
            else:
                flash(
                    f"Something want wrong with selling { sold_item_object.name } ", category="danger"
                )

        return redirect(url_for("market_page"))

    if request.method == "GET":
        items = Item.query.filter_by(owner=None)
        owned_items = Item.query.filter_by(owner=current_user.id)
        return render_template(
            "market.html",
            items=items,
            purchase_form=purchase_form,
            owned_items=owned_items,
            selling_form=selling_form,
        )


@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password1.data,
        )
        db.session.add(user_to_create)
        db.session.commit()

        login_user(user_to_create)
        flash("Account created Successfully!! ", category="success")
        flash(f"Welcome {user_to_create.username}", category="success")

        return redirect(url_for("market_page"))
    if form.errors != {}:
        # If Error are Found from validation
        for err_msg in form.errors.values():
            flash(f"Error : {err_msg}", category="danger")
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash("Successfully Login !! ", category="success")
            flash(f"Welcome {attempted_user.username}", category="success")

            return redirect(url_for("market_page"))

        else:
            flash(
                f"Username and Password Does not match! Please try again ",
                category="danger",
            )
    return render_template("login.html", form=form)


@app.route("/logout")
def logout_page():
    logout_user()
    flash(f"You have been logged out!", category="info")
    flash(f"Logout Successfully!", category="info")
    return redirect(url_for("Home_Page"))

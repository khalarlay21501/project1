from flask import Blueprint, render_template,request
from controllers.omikuji_controller import OmikujiController    

main = Blueprint("main", __name__)
@main.route("/")
def index():
    return render_template("index.html")
@main.route("/result",methods=["POST"])
def result():
    if request.method == "POST":
        controller = OmikujiController()  
        today_data = controller.draw()    
        return render_template("result.html", data=today_data)
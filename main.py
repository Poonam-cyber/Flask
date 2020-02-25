from flask import Flask, redirect, url_for,render_template,request
import json
import schedule as sh
app = Flask(__name__)

@app.route('/')
def form():
   return render_template("try.html")

@app.route('/success',methods=["POST"])
def success():
    user=request.form["txt_user"]
    profile=request.form["txt_profile"]
    sd=request.form["txt_sd"]
    ed=request.form["txt_ed"]
    sh.all_operations(user,profile,sd,ed)
    return redirect("/display") 

@app.route('/display',methods=["GET"])
def display():
        with open("dictionary_list.json") as f:
            data=json.load(f)
        return render_template("display.html",data=data)

@app.route('/success2',methods=["POST"])
def success2():
  with open("dictionary_list.json") as f:
        data=json.load(f)
        return render_template("display.html",data=data)
if __name__ == '__main__':
   app.run(debug = True)
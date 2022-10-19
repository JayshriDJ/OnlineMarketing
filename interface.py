import config
from flask import Flask,jsonify,render_template,request
from Project.utils import Online_Marketing

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Online_Market_Profit",methods=["POST","GET"])
def get_market_profit():
    if request.method == "POST":
        data=request.form

        Marketing_Spend=eval(data["Marketing_Spend"])
        Administration=eval(data["Administration"])
        Transport=eval(data["Transport"])
        Area=data["Area"]

        market_profit=Online_Marketing(Marketing_Spend,Administration,Transport,Area)
        profit=market_profit.get_Profit()
        #return jsonify({"Result":f"Predicted Online Market Price is: {profit}"})
        return render_template("index1.html", profit=profit)


    else:

        Marketing_Spend=int(request.args.get("Marketing_Spend"))
        Administration=int(request.args.get("Administration"))
        Transport=int(request.args.get("Transport"))
        Area=request.args.get("Area")

        market_profit=Online_Marketing(Marketing_Spend,Administration,Transport,Area)
        profit=market_profit.get_Profit()
        #return jsonify({"Result":f"Predicted Online Market Price is: {profit}"})
        return render_template("index1.html",profit=profit)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=config.PORT_NO)


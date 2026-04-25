from flask import Flask, render_template, request

app = Flask(__name__)

# chatbot function
def get_reply(text):
    text = text.lower()

    if "admission" in text:
        return "Admissions are currently open. Last date is 30 August."
    
    elif "fee" in text:
        return "The semester fee is around 50,000."
    
    elif "program" in text:
        return "Available programs include BSCS, BBA, BSIT etc."
    
    elif "deadline" in text:
        return "The last date to apply is 30 August."
    
    elif "hi" in text or "hello" in text:
        return "Hi! How may I assist you?"
    
    else:
        return "Sorry, I didn't get that."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reply", methods=["POST"])
def reply():
    user_msg = request.form["msg"]
    return get_reply(user_msg)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template_string, request
‎
‎app = Flask(__name__)
‎
‎html = """
‎<!DOCTYPE html>
‎<html>
‎<head>
‎    <title>System Integration Project</title>
‎    <style>
‎        body {font-family: Arial; text-align: center; padding: 50px; background: #f2f2f2;}
‎        .box {background: white; padding: 30px; border-radius: 10px; width: 400px; margin: auto; box-shadow: 0 0 10px rgba(0,0,0,0.1);}
‎        input, textarea {width: 90%; padding: 10px; margin: 8px 0; border: 1px solid #ccc; border-radius: 5px;}
‎        button {padding: 12px 25px; background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer;}
‎        button:hover {background: #0056b3;}
‎    </style>
‎</head>
‎<body>
‎    <div class="box">
‎        <h2>Contact Form</h2>
‎        <p><b>System Integration and Architecture</b></p>
‎        <p>Submitted by: <b>Norhuda Mindo & Rahima Guiamadel</b></p>
‎        
‎        <form method="POST">
‎            <input type="text" name="name" placeholder="Your Name" required><br>
‎            <input type="email" name="email" placeholder="Your Email" required><br>
‎            <textarea name="message" placeholder="Your Message" rows="4" required></textarea><br>
‎            <button type="submit">Send Message</button>
‎        </form>
‎        
‎        {% if msg %}
‎        <p style="color:green; margin-top: 20px; font-weight: bold;">{{ msg }}</p>
‎        {% endif %}
‎    </div>
‎</body>
‎</html>
‎"""
‎
‎@app.route("/", methods=["GET", "POST"])
‎def home():
‎    msg = ""
‎    if request.method == "POST":
‎        name = request.form["name"]
‎        email = request.form["email"]
‎        message = request.form["message"]
‎        msg = f"Thank you {name}! Your message was received."
‎        print(f"New Message from {name} - {email}: {message}")
‎    return render_template_string(html, msg=msg)
‎
‎if __name__ == "__main__":
‎    app.run(host="0.0.0.0", port=8080)
‎ 

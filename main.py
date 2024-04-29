from flask import Flask, request, redirect, render_template_string
import json

app = Flask(__name__)

# HTML template as a Python multi-line string
HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Screening Form</title>
</head>
<body>
    <h1>Enter Your Information</h1>
    <form action="/submit" method="post">
        <label for="fullName">Full Name (required):</label><br>
        <input type="text" id="fullName" name="fullName" required><br><br>
        <label for="dob">Year of Birth:</label><br>
        <input type="text" id="yob" name="yob"><br><br>
        <label for="location">Location:</label><br>
        <input type="text" id="location" name="location"><br><br>
        <label for="birthLocation">Birth Location:</label><br>
        <input type="text" id="birthLocation" name="birthLocation"><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""

@app.route('/')
def form():
    return render_template_string(HTML)

@app.route('/submit', methods=['POST'])
def submit():
    # Collect data from the form
    data = {
        "Full Name": request.form['fullName'],
        "DOB": request.form['yob'] or None,
        "Location": request.form['location'] or None,
        "Birth Location": request.form['birthLocation'] or None
    }
    
    # Write data to a JSON file
    with open('userdata.json', 'w') as f:
        json.dump(data, f, indent=4)
       
       
    
    return "Data submitted successfully! Check the server directory for userdata.json",  exec(open('requestTest.py').read())


if __name__ == '__main__':
    app.run(debug=True)



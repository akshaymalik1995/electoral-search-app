import requests
from flask import Flask , request, jsonify, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/captcha')
def get_captcha():
    try:
        response = requests.get("https://gateway-voters.eci.gov.in/api/v1/captcha-service/generateCaptcha")
        return response.json()
    except Exception as e:
        print(e)
        return {"error": "Error in fetching captcha"}
    
@app.route("/api/electoral-search", methods=["post"])
def get_electoral_search():
    try:
        data = request.get_json()
        print(data)
        captcha_id = data.get("captchaId")
        epic_no = data.get("epicNumber")
        state_cd = data.get("stateCd")
        captcha_data = data.get("captchaData")
        post_data = {
            "isPortal": "true",
            "epicNumber": epic_no,
            "stateCd": state_cd,
            "captchaId": captcha_id,
            "captchaData": captcha_data,
            "securityKey": "na"
        }
        
        response = requests.post("https://gateway.eci.gov.in/api/v1/elastic/search-by-epic-from-national-display", json=post_data)
        return response.json()
    except Exception as e:
        print(e)
        return {"error": "Error in fetching electoral search"}
    

if __name__ == '__main__':
    app.run(debug=True)
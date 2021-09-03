from flask import Flask, jsonify, render_template
from flask import request
app = Flask(__name__)
# 현재 이 파일(모듈)의 이름에 대한 파일을 플라스크 app 인스턴스로 사용하겠다.
# / 에 대하여 라우팅 된 경우에 대한 데코레이터이다.
@app.route("/")
def index():
# 플라스크의 뷰 함수 이다.
	return render_template("index.html")
# json 화 ( = 딕셔너리 화 ) 하여 반환하겠다.


@app.route("/login_fail")
def loginFail():
	return "<h1>가입에 실패하셨습니다</h1><form action='/login'><input type='submit' value='다시 시도 하시겠습니까?'></form>"


@app.route("/login")
def loginPage():
	return render_template("login.html")

@app.route("/try", methods=['POST'])
def loginTry():
	value = request.form["ID"]
	code = request.form["CODE"]
	if str(code) == "0303":
		name = " %s 로 로그인 되었습니다." % value
		return name
	else:
		return "/login_fail"
	

@app.route("/main")
def main():
	return "main"

@app.route("/json")
def json():
	return jsonify(key = "value")

if __name__ == "__main__":
# 현재 위치가 엔트리 포인트 이면 실행하겠다.
	app.run("0.0.0.0", port=5000)
# 0.0.0.0 은  알 수 없는 대상을 의미하며, 사용되는 대상이나 시점에서 모든 IP 를 의미 할 수도 있다.
# 127.0.0.1 은 기기가 자기 자신에게 메시지를 보내는 목적을 가진다.
# port 설정은  open 될 http 포트를 의미한다.
# 개발 중인 Flask 프레임워크에서 사용하는 포트이다.
# 참고로 
# 80 -> HTTP
# 443 -> HTTPS
# 22 -> SSH
# 3389 -> RDP
# 8000 -> 5000과 비슷
# Azure 와 같은 플랫폼 서버를 사용할 경우 5000이나 8000을 사용자지정 포트로 추가해주어야 할 수도 있다.
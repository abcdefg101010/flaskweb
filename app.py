from flask import Flask, render_template


app = Flask(__name__)

@app.route('/',methods=['GET',])
def index():
    return render_template('index.html')

if __name__=='__main__':
# 다른데에서 불러도 실행하지 말고 여기에서만 해라 = __name__
    app.run(debug=True)


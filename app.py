import os
from Flask import Flask

app = Flask(__name__)

@app.route('/')
def Hello():
    return 'This application is up and running'
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
from flask import Flask
app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return 'Hello World'

@app.route('/hello/<name>')
def hello_world(name):
    #return 'Hello %s!' %name
    return 'Hello {}'.format(name)

@app.route('/multiply/<int:firstvalue>/<int:secondvalue>')
def multiply(firstvalue,secondvalue):
    result = firstvalue * secondvalue
    if result % 2 ==0:
        return "The number {} is an even Number".format(result)
    else:
        return "The number {} is an odd Number".format(result)


if __name__ == '__main__':
    app.run(debug=True)
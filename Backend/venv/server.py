# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
from flask import jsonify
from flask import request
# # from flask_cors import CORS
# # import predict

# # Flask constructor takes the name of 
# # current module (__name__) as argument.
app = Flask(__name__) # Controller of entire project
# cors = CORS(app) # allow CORS for all domains on all routes, policy secure on domains
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # Set max content limit at 16 MB, aka sticky note length. For images, you want your content length to be pretty big

# Difference between POST and GET is POST takes in input and gives output, GET just returns output. POST you need a key sometimes and you can charge people to use, GET open source

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/') # visiting the slash of the endpoint gives you 'hello world'
# # ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

# @app.route('/prediction', methods=["POST"])
# def prediction():
#     if request.method == "POST":
#         request_data = request.get_json()
#         return jsonify(predict.predict(request_data['url']))
    
#     return None

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host='0.0.0.0', port=5050)
    # '0.0.0.0' makes the server accessible
    # from any IP address on your network
    # port=num is the port number 'num' to use

# Hackathon Image APIs
    # pixels API
    # image API
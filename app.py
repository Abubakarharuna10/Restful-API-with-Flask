from flask import Flask, jsonify, request
from flask_restful import Api, Resource






app = Flask(__name__)
api = Api(app)

def checkPostedData(postedDate, functionName):
	if (functionName == 'add' or functionName == 'Subtract' or functionName == 'Multiply' or functionName == 'division'):
		if 'x' not in postedDate or 'y' not in postedDate:
			return 301
		else:
			return 200

	elif (functionName == 'division'):
		if 'x' not in postedDate or 'y' not in postedDate:
			return 301

		elif int(postedDate['y'])==0:
			return 302

		else:
			return 200

class Add(Resource):

	def post(self):

		postedDate = request.get_json()

		status_code = heckPostedData(postedDate, 'add')
		if (status_code !=200):
			retJson = {
				'Massage': 'An error happen',
				'Status code': status_code
			}
			return jsonify(retJson)

		x = postedDate['x']
		y = postedDate['y']
		x = int(x)
		y = int(y)
		ret = x-y
		retmap = {
			'Massage': ret,
			'Status code':200
		}
		return jsonify(retmap)

		# if am here but the Resource add was requested using the method post

	# def get(self):
	#
	# 	# if am here then the Resource add was requested using method get
	#
	# def put(self):
	# 	pass
	#
	# def delete(self):
	# 	pass
	#
	# pass

class Subtract(Resource):
	def post(self):

		postedDate = request.get_json()

		status_code = heckPostedData(postedDate, 'Subtract')
		if (status_code !=200):
			retJson = {
				'Massage': 'An error happen',
				'Status code': status_code
			}
			return jsonify(retJson)

		x = postedDate['x']
		y = postedDate['y']
		x = int(x)
		y = int(y)
		ret = x-y
		retmap = {
			'Massage': ret,
			'Status code':200
		}
		return jsonify(retmap)


class Multiply(Resource):
	def post(self):

		postedDate = request.get_json()

		status_code = heckPostedData(postedDate, 'Multiply')
		if (status_code !=200):
			retJson = {
				'Massage': 'An error happen',
				'Status code': status_code
			}
			return jsonify(retJson)

		x = postedDate['x']
		y = postedDate['y']
		x = int(x)
		y = int(y)
		ret = x*y
		retmap = {
			'Massage': ret,
			'Status code':200
		}
		return jsonify(retmap)


class Divide(Resource):
	def post(self):

		postedDate = request.get_json()

		status_code = heckPostedData(postedDate, 'division')
		if (status_code !=200):
			retJson = {
				'Massage': 'An error happen',
				'Status code': status_code
			}
			return jsonify(retJson)

		x = postedDate['x']
		y = postedDate['y']
		x = int(x)
		y = int(y)
		ret = (x*1.0)/y
		retmap = {
			'Massage': ret,
			'Status code':200
		}
		return jsonify(retmap)

api.add_resource(Add, "/add")
api.add_resource(Subtract, "/Subtract")
api.add_resource(Multiply, "/Multiply")
api.add_resource(Divide, "/division")

@app.route('/')

def hello_world():
	return 'Hello World'

@app.route('/hithere')

def hi():

	return "Hi there"

@app.route('/add_two_nums', methods=['POST'])
def add_two_nums():
	dataDict = request.get_json()
	x = dataDict["x"]
	y = dataDict["y"]
	z = x+y

	retJson = {
		"z":z
	}

	return jsonify(retJson), 200


@app.route('/bye')

def bye():

	Age = 2*5
	#return 'bye'
	retJson = {
	'name': 'Abba',
	'Age': 	Age,
	"phones":[
			{
				"phoneName": "Iphone8",
				"phoneNumber":111,

			},
			{
				"phoneName": "nokia",
				"phoneNumber": 1122,

			}

		]
	}
	return jsonify(retJson)

if __name__=="__main__":
	app.run(debug=True)

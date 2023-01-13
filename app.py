from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convert', methods=['GET'])
def convert():
    # Get the temperature value and the unit of measurement from the query parameters
    temp = request.args.get('temp')
    unit = request.args.get('unit')

    # Check if the temperature and unit values are provided
    if temp is None or unit is None:
        return jsonify(error='Both temperature and unit of measurement are required'), 400

    # Convert the temperature to Celsius if it's in Fahrenheit
    if unit.upper() == 'F':
        temp = (float(temp) - 32) * 5/9

    # Convert the temperature to Fahrenheit if it's in Celsius
    elif unit.upper() == 'C':
        temp = (float(temp) * 9/5) + 32

    # Return the converted temperature
    return jsonify(temp=temp, unit=unit.upper())

if __name__ == '__main__':
    app.run(debug=True)

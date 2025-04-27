import json
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return 'OK', 200

@app.route('/dialogflow', methods=['GET', 'POST'])
def dialogflow():
    data = request.get_json()
    print(json.dumps(data, indent=2))  # Pretty print for easier debugging

    # Correct way to extract fields
    intent = data['intentInfo']['displayName']
    tagg = data['fulfillmentInfo']['tag']
    parameter = data.get('sessionInfo', {}).get('parameters', {})

    print('Intent:', intent)
    print('Tag:', tagg)
    print('Parameters:', parameter)

    return jsonify(
        {
            'fulfillment_response': {
                'messages': [
                    {
                        'text': {
                            'text': ['This is a sample response from webhook.']
                        }
                    }
                ]
            }
        }
    )


if __name__ == '__main__':
    app.run(debug=True)
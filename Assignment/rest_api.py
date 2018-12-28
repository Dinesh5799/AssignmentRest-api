from flask import Flask,jsonify,request
import json
app = Flask(__name__)

users=[
  {
    'sNo': 1,
    'firstName': 'Daniel',
    'lastName': 'Green',
    'email': 'Daniel.Green@test.com'
  },
  {
    'sNo': 2,
    'firstName': 'Rickey',
    'lastName': 'Avant',
    'email': 'Rickey.Avant@test.com'
  },
  {
    'sNo': 3,
    'firstName': 'Pamela',
    'lastName': 'Nash',
    'email': 'Pamela.Nash@test.com'
  },
  {
    'sNo': 4,
    'firstName': 'Juanita',
    'lastName': 'Cole',
    'email': 'Juanita.Cole@test.com'
  },
  {
    'sNo': 5,
    'firstName': 'John',
    'lastName': 'Nolan',
    'email': 'John.Nolan@test.com'
  },
  {
    'sNo': 6,
    'firstName': 'Francisco',
    'lastName': 'Kazee',
    'email': 'Francisco.Kazee@test.com'
  },
  {
    'sNo': 7,
    'firstName': 'Oscar',
    'lastName': 'Huggins',
    'email': 'Oscar.Huggins@test.com'
  },
  {
    'sNo': 8,
    'firstName': 'Micheal',
    'lastName': 'Reynolds',
    'email': 'Micheal.Reynolds@test.com'
  },
  {
    'sNo': 9,
    'firstName': 'Daniel',
    'lastName': 'Gomes',
    'email': 'Daniel.Gomes@test.com'
  },
  {
    'sNo': 10,
    'firstName': 'Julia',
    'lastName': 'Baker',
    'email': 'Julia.Baker@test.com'
  },
  {
    'sNo': 11,
    'firstName': 'Dorothy',
    'lastName': 'Eanes',
    'email': 'Dorothy.Eanes@test.com'
  },
  {
    'sNo': 12,
    'firstName': 'Jose',
    'lastName': 'Stevenson',
    'email': 'Jose.Stevenson@test.com'
  },
  {
    'sNo': 13,
    'firstName': 'Earnestine',
    'lastName': 'Hunt',
    'email': 'Earnestine.Hunt@test.com'
  },
  {
    'sNo': 14,
    'firstName': 'Norman',
    'lastName': 'Mack',
    'email': 'Norman.Mack@test.com'
  },
  {
    'sNo': 15,
    'firstName': 'Patricia',
    'lastName': 'Poling',
    'email': 'Patricia.Poling@test.com'
  },
  {
    'sNo': 16,
    'firstName': 'Stephen',
    'lastName': 'Kym',
    'email': 'Stephen.Kym@test.com'
  },
  {
    'sNo': 17,
    'firstName': 'Earl',
    'lastName': 'Robinson',
    'email': 'Earl.Robinson@test.com'
  },
  {
    'sNo': 18,
    'firstName': 'Jacob',
    'lastName': 'Smith',
    'email': 'Jacob.Smith@test.com'
  },
  {
    'sNo': 19,
    'firstName': 'Terri',
    'lastName': 'Gartrell',
    'email': 'Terri.Gartrell@test.com'
  },
  {
    'sNo': 20,
    'firstName': 'Mamie',
    'lastName': 'Diaz',
    'email': 'Mamie.Diaz@test.com'
  },
  {
    'sNo': 21,
    'firstName': 'Janette',
    'lastName': 'Spring',
    'email': 'Janette.Spring@test.com'
  },
  {
    'sNo': 22,
    'firstName': 'Lisa',
    'lastName': 'Lawler',
    'email': 'Lisa.Lawler@test.com'
  },
  {
    'sNo': 23,
    'firstName': 'James',
    'lastName': 'Martinez',
    'email': 'James.Martinez@test.com'
  },
  {
    'sNo': 24,
    'firstName': 'Thomas',
    'lastName': 'Hockensmith',
    'email': 'Thomas.Hockensmith@test.com'
  }
  ]
    
@app.route("/users",methods=['GET'])
def get_userByEmail():
    param = request.args.get('email')
    param2 = request.args.get('firstName')
    param3 = request.args.get('lastName')
    for i in users:
        if not param == None and i['email'] == param:
            return jsonify(i)
        elif not param2 == None and i['firstName'] == param2:
            return jsonify(i)
        elif not param3 == None and i['lastName'] == param3:
            return jsonify(i)
    return jsonify({'errCode':404,'errMsg':'Record not found'})


@app.route("/users/pages",methods=['GET'])
def get_userByPage():
    page_no = request.args.get('page')
    page_no = int(page_no)
    if len(users) > (page_no-1)*10 or len(users) < page_no*10:
        res_list = users[(page_no-1)*10:page_no*10]
        if len(res_list) > 0:
            return jsonify(res_list)
        else:         
            return jsonify({'errCode':404,'errMsg':'Records Exhausted'})
        
if __name__ == '__main__':
    app.run(debug=True)




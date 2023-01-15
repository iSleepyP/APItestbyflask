from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def hello():
  q = request.args.get('q')
  print(q)
  return { "message": "Hello!" }, 201

books = []
body={}

body= {
    "books":[
        {
            "Authors":"A",
            "Price": 350,
            "title":"Book1"
        },
        {
            "Authors":"B",
            "Price": 250,
            "title":"Book2"
        }
    ]
}

body2= {
    "books2":[
        {
            "Authors":"C",
            "Price": 450,
            "title":"Book3"
        },
        {
            "Authors":"D",
            "Price": 200,
            "title":"Book4"
        }
    ]
}



@app.route('/book', methods=['POST', 'GET','PUT'])
def book():
  if request.method == 'POST':

    books.append(body)
    #books.append(body2)
    return { "message": "Book already add to database", "body": body }, 201
  elif request.method == 'GET':
    return { "books": books }, 200
  
  elif request.method == 'PUT':
    for i, book in enumerate(books):
        if book['id'] == body['id']:
            books[i] = body
    return {"message": "Book has been replace", "body": body}, 200


if __name__ == "__main__":
    app.run(debug=True)
    app.run("0.0.0.0",port = 5000)
from flask import Flask
from primeNumbers import prime

app = Flask(__name__)
primN = prime()


@app.route('/')
def hundred_primes():
    return str(primN.get_primes(100))
    return "hello"


@app.route('/<int:n>', methods=['GET'])
def get_first_n_primes(n):
    return str(primN.get_primes(n))


if __name__ == "__main__":
    app.run(debug=True)

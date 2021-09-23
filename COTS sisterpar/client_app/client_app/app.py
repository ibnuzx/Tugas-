from flask import Flask, render_template, request
import xmlrpc.client

server = xmlrpc.client.ServerProxy('http://127.0.0.1:8080')
app = Flask(__name__)


@app.route('/submit', methods=['post', 'get'])
def submit():
    data = {}
    pesan = [1, 2, 3]
    if request.method == 'POST':
        data['nama'] = request.form.get('nama')
        data['gula_darah'] = request.form.get('gula_darah')
        data['status'] = True
        server.vote(data['nama'])
        print(server.querry())
        data['status'] = server.querry()
    return render_template('submit.html', data=data, n_pesan=len(pesan))


if __name__ == '__main__':
    app.run(debug=True)

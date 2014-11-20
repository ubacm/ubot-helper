import requests
from flask import Flask

import ub_vcf

app = Flask(__name__)

@app.route('/whois/<string:name>')
def whois(name):
  if '@' in name:
    name = name.split('@')[-1]
  resp = requests.get('https://www.buffalo.edu/directory/user/%s.vcf' % name)
  return str(ub_vcf.Vcf(resp.text))

if __name__ == '__main__':
  app.run(debug=True)

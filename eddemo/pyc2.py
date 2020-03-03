import requests

url = 'http://tools-cluster-interface.iedb.org/tools_api/mhci/'
myobj = 'method=smm&sequence_text=SLYNTVATLYCVHQRIDV&allele=HLA-A*01:01&length=9'

x = requests.post(url, data=myobj)
output = [
    print(x.text)]

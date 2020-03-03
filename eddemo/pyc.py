import pycurl
from io import BytesIO
from urllib.parse import urlencode

b_obj = BytesIO()
crl = pycurl.Curl()

# Set URL value
crl.setopt(crl.URL, 'http://tools-cluster-interface.iedb.org/tools_api/mhci/')

post_data = {'field': 'value'}

# OLD #
# Write bytes that are utf-8 encoded
# crl.setopt(crl.WRITEDATA, b_obj)
# End OLD#


# Sets request method to POST,
# Content-Type header to application/x-www-form-urlencoded
# and data to send in request body.
postfields = urlencode(post_data)

# OLD
# crl.setopt_string(crl.data, "method=smm&sequence_text=SLYNTVATLYCVHQRIDV&allele=HLA-A*01:01&length=9")
# Perform a file transfer
# ###OLD##

crl.setopt(crl.POSTFIELDS, postfields)
# End curl session
crl.setopt(crl.WRITEDATA, b_obj.write)
crl.perform()
crl.close()

## OLD
# Get the content stored in the BytesIO object (in byte characters)
# get_body = getvalue()
body = b_obj.getvalue()
# Decode the bytes stored in get_body to HTML and print the result


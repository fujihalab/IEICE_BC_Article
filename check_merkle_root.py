import sys, json, hashlib, pyld

if len(sys.argv) != 2:
  print('usage: $ python3 check_merkle_root.py <certificate (json file)>')
  sys.exit(0)

infilename = sys.argv[1]
with open(infilename, 'r') as json_file:
  json_proof = json.load(json_file)

# remove the 'proof' section 
json_proof.pop('proof')

# canonicalize the json
normalized_proof = pyld.jsonld.normalize(json_proof, {'algorithm': 'URDNA2015', 'format': 'application/nquads'})

# calculate the hash of normalized_proof, 
# which is the tokenHash in the transaction
merkle_root = hashlib.sha256(str.encode(normalized_proof)).hexdigest()
print('Merkle root:', merkle_root)

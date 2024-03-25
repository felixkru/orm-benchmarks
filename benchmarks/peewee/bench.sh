#!/bin/sh

# setup DB
# ../db.sh
python3 -m set_up

# Test A → Insert
python3 -m test_a

# Test B → Transactioned Intsert
python3 -m test_b

# Test C → Bulk Insert
python3 -m test_c

# Test D → Filter on level
python3 -m test_d

# Test E → Filter limit 20
python3 -m test_e

# Test F → Get
python3 -m test_f

# Test G → dict
python3 -m test_g

# Test H → tuple
python3 -m test_h

# Test I → Update full
python3 -m test_i

# Test J → Update partial
python3 -m test_j

# Test K → Delete
python3 -m test_k

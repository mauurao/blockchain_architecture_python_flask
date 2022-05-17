"""
This script is responsible for creating and implementing all the logic of the blockchain services for the supply chain, 
with different roles for the different actors, among other implementations.

Created by Mauro Cardoso, 23 of April 2022, 19:16    
"""

import os, json
from datetime import datetime
import uuid, hashlib, random


# The ledger was used as a file system
blockchain_dir = 'Arquitetura 1/blockchain_ledger/'

# Definition of the starting block function
def genesis_block():
    already_created = os.path.exists(blockchain_dir + '1')
    if already_created == False:
        # Smart contract definition
        data = {
            # transaction and contract information --DUMMY DATA--
            "Transaction":{
                'contracted': 'None',
                'contractor': 'None',
                "amount": 0,       
                'contract certificate': 'None',       
                'production date': 'None',
                'sku':'None',       
                'barcode id': 'None'
            }}
        
        initial_block = {
            "block": {
                'date': (datetime.now()).strftime("%d/%m/%Y %H:%M:%S"),
                'hash': hashlib.md5((str(data['Transaction']).encode('utf-8'))).hexdigest(), 
            }
        }
        
        # Add smart contract to the block
        initial_block.update(data)
        
        counter = 0 # Aux variable
        
        with open (blockchain_dir + str(counter + 1), 'w') as f: # Creation of the file, starting by the count 1
            json.dump(initial_block, f, indent=4, ensure_ascii=False)
            f.write('\n')

# Definition of the previous block function
def get_last_hash(bloco_anterior):
    with open(blockchain_dir + bloco_anterior, 'rb') as f: # opening of the last block file created
        content = json.load(f) # Read and transform to JSON object
        return content['block']['hash'] # Return of the hash value inside

# Definition of the function with the template of the smart contract and creation of the block for the raw material manufacturers
def write_block_sc_raw_material(raw_contracted, raw_contractor, raw_amount):
    
    count_block = len(os.listdir(blockchain_dir)) # Variable that counts and lists all the blocks existing in the filesystem
    prev_bloc = str(count_block) # Variable that takes the last number of the block
    
    # Determine the name of the next block, count the existing blocks and add + 1
    current_block = blockchain_dir + str(len(os.listdir(blockchain_dir)) + 1) 
    
    # Smart contract definition
    sc_raw_material = {
          # transaction and contract information --DUMMY DATA--
        "Transaction":{
            'contracted': raw_contracted,
            'contractor': raw_contractor,
            'amount': int(raw_amount),       
            'contract certificate': str(uuid.uuid1()),       
            'production date': (datetime.now()).strftime("%d/%m/%Y %H:%M:%S"),
            'sku':str(random.randint(100000001,300000001)),       
            'barcode id': str(random.randint(100000,100000000))
        }}

    
    # Writing the block with the contract definition
    block_write = {
        # block information
         "block": {
            'date': (datetime.now()).strftime("%d/%m/%Y %H:%M:%S"),
            'hash': hashlib.md5((str(sc_raw_material['Transaction']).encode('utf-8'))).hexdigest(),
        },      
        "prev_block": {
            "hash": get_last_hash(prev_bloc),
            "block file": prev_bloc
        }
    }
    
    # Add smart contract to the block
    block_write.update(sc_raw_material)
      
    #Create the block with the contract information
    with open (current_block, 'w') as f:
        json.dump(block_write, f, indent=4, ensure_ascii=False)
        f.write('\n')

# Definition of the function with the template of the smart contract and creation of the block for the Pharmaceutical Manufacturers
def write_block_sc_pharma(ph_quantity, ph_drug):
    
    count_block = len(os.listdir(blockchain_dir)) # Variable that counts and lists all the blocks existing in the filesystem
    prev_bloc = str(count_block) # Variable that takes the last number of the block
    
    # Determine the name of the next block, count the existing blocks and add + 1
    current_block = blockchain_dir + str(len(os.listdir(blockchain_dir)) + 1) 
    
    # Smart contract definition
    sc_pharma = {
          # transaction and contract information --DUMMY DATA--
        "Transaction":{  
            'quantity': int(ph_quantity),
            'drug': ph_drug,
            'certificate': str(uuid.uuid1()),
            'approval status': 1,       
            'production date': (datetime.now()).strftime("%d/%m/%Y %H:%M:%S"),
            'sku':str(random.randint(100000001,300000001)),       
            'barcode id': str(random.randint(100000,100000000))
        }}

    
    # Writing the block with the contract definition
    block_write = {
        # block information
         "block": {
            'date': (datetime.now()).strftime("%d/%m/%Y %H:%M:%S"),
            'hash': hashlib.md5((str(sc_pharma['Transaction']).encode('utf-8'))).hexdigest(),
        },      
        "prev_block": {
            "hash": get_last_hash(prev_bloc),
            "block file": prev_bloc
        }
    }
    
    # Add smart contract to the block
    block_write.update(sc_pharma)
      
    #Create the block with the contract information
    with open (current_block, 'w') as f:
        json.dump(block_write, f, indent=4, ensure_ascii=False)
        f.write('\n')       

# Definition of the function with the template of the smart contract and creation of the block for the pharma regulator
def write_block_regulator(r_requester, r_regulator, r_validation):
    
    count_block = len(os.listdir(blockchain_dir)) # Variable that counts and lists all the blocks existing in the filesystem
    prev_bloc = str(count_block) # Variable that takes the last number of the block
    
    # Determine the name of the next block, count the existing blocks and add + 1
    current_block = blockchain_dir + str(len(os.listdir(blockchain_dir)) + 1) 
    
    # Smart contract definition
    sc_regulator = {
          # transaction and contract information --DUMMY DATA--
        "Transaction":{
            'amount': 0,       
            'pharma manufacturer': r_requester,
            'regulator id': r_regulator,
            'validation': bool(r_validation),       
            'certificate': str(uuid.uuid1()),       
            'emission date': (datetime.now()).strftime("%d/%m/%Y %H:%M:%S"),
            'sku': str(random.randint(100000001,300000001))      
        }}

    
    # Writing the block with the contract definition
    block_write = {
        # block information
         "block": {
            'date': (datetime.now()).strftime("%d/%m/%Y %H:%M:%S"),
            'hash': hashlib.md5((str(sc_regulator['Transaction']).encode('utf-8'))).hexdigest(),
        },      
        "prev_block": {
            "hash": get_last_hash(prev_bloc),
            "block file": prev_bloc
        }
    }
    
    # Add smart contract to the block
    block_write.update(sc_regulator)
      
    #Create the block with the contract information
    with open (current_block, 'w') as f:
        json.dump(block_write, f, indent=4, ensure_ascii=False)
        f.write('\n')

# Definition of the function with the template of the smart contract and creation of the block for the warehouses transactions
def write_block_warehouse(wr_contracted, wr_contractor, wr_amount, wr_drug):
    
    count_block = len(os.listdir(blockchain_dir)) # Variable that counts and lists all the blocks existing in the filesystem
    prev_bloc = str(count_block) # Variable that takes the last number of the block
    
    # Determine the name of the next block, count the existing blocks and add + 1
    current_block = blockchain_dir + str(len(os.listdir(blockchain_dir)) + 1) 
    
    # Smart contract definition
    sc_warehouse_to_hospital = {
          # transaction and contract information --DUMMY DATA--
        "Transaction":{
            'contracted': wr_contracted,
            'contractor': wr_contractor,
            'drug': wr_drug,
            'amount': wr_amount, 
            'warehouse id': str(uuid.uuid1()),
            'manufacturer last update date': (datetime.now()).strftime("%d/%m/%Y %H:%M:%S"),
            'hospital last update date': (datetime.now()).strftime("%d/%m/%Y %H:%M:%S"),
            'sku':str(random.randint(100000001,300000001)),       
            'manufacturer warehouse iot temperature': str(random.randint(-90,-60)),
            'manufacturer warehouse iot humidity': str(random.randint(0,60)),
            'hospital warehouse iot temperature': str(random.randint(-90,-60)),
            'hospital warehouse iot humidity': str(random.randint(0,60)),
            'barcode id': str(random.randint(100000,100000000))
        }}

    
    # Writing the block with the contract definition
    block_write = {
        # block information
         "block": {
            'date': (datetime.now()).strftime("%d/%m/%Y %H:%M:%S"),
            'hash': hashlib.md5((str(sc_warehouse_to_hospital['Transaction']).encode('utf-8'))).hexdigest(),
        },      
        "prev_block": {
            "hash": get_last_hash(prev_bloc),
            "block file": prev_bloc
        }
    }
    
    # Add smart contract to the block
    block_write.update(sc_warehouse_to_hospital)
      
    #Create the block with the contract information
    with open (current_block, 'w') as f:
        json.dump(block_write, f, indent=4, ensure_ascii=False)
        f.write('\n')

# Definition of the function with the template of the smart contract and creation of the block for the warehouses transactions
def write_block_distribuitor(dr_sender, dr_receiver, dr_amount, dr_address):
    
    count_block = len(os.listdir(blockchain_dir)) # Variable that counts and lists all the blocks existing in the filesystem
    prev_bloc = str(count_block) # Variable that takes the last number of the block
    
    # Determine the name of the next block, count the existing blocks and add + 1
    current_block = blockchain_dir + str(len(os.listdir(blockchain_dir)) + 1) 
    
    # Smart contract definition
    sc_distribuition = {
          # transaction and contract information --DUMMY DATA--
        "Transaction":{
            'sender': dr_sender,
            'receiver': dr_receiver,
            'receiver address': dr_address,
            'distributor id': str(random.randint(1000,5000)),
            'amount': dr_amount, 
            'distribuition id': str(uuid.uuid1()),
            'status id':str(random.randint(0,2)),
            'last status update date': (datetime.now()).strftime("%d/%m/%Y %H:%M:%S"),
            'iot distribuition temperature': str(random.randint(-90,-60)),
            'iot distribuition humidity': str(random.randint(0,60)),
            'hss code': str(uuid.uuid1()),
        }}

    
    # Writing the block with the contract definition
    block_write = {
        # block information
         "block": {
            'date': (datetime.now()).strftime("%d/%m/%Y %H:%M:%S"),
            'hash': hashlib.md5((str(sc_distribuition['Transaction']).encode('utf-8'))).hexdigest(),
        },      
        "prev_block": {
            "hash": get_last_hash(prev_bloc),
            "block file": prev_bloc
        }
    }
    
    # Add smart contract to the block
    block_write.update(sc_distribuition)
      
    #Create the block with the contract information
    with open (current_block, 'w') as f:
        json.dump(block_write, f, indent=4, ensure_ascii=False)
        f.write('\n')

# Function to check the integrity of the blockchain
def check_integrity():
    
    results = []
    files = sorted(os.listdir(blockchain_dir), key=lambda x: int(x))
    print (files)
    for file in files[1:]:

        with open(blockchain_dir + file) as f:
            block = json.load(f)
              
        prev_hash = block.get('prev_block').get('hash')
        prev_block = block.get('prev_block').get('block file')

        
        file_1 = int(file) - 1
        with open(blockchain_dir + str(file_1)) as f:
            block1 = json.load(f)
            prev_trans = block1.get('Transaction')

        
        actual_hash = hashlib.md5((str(prev_trans).encode('utf-8'))).hexdigest()

        
        if prev_block == '1':
            res = 'First transaction: Integrity ok'
        elif prev_hash == actual_hash:
            res = 'Integrity ok'
        else:
            res = 'Integrity changed'

        print(f'Block {prev_block}: {res}')
        results.append({'block': prev_block, 'result': res})
        
    return results
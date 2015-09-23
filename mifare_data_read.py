import nxppy
import time

mifare = nxppy.Mifare()

while True:
    try:
        # Read 64 bytes starting from block 4 

	uid = mifare.select()
	# (each block is 4 bytes, so technically this reads blocks 4-7)
	block_data = mifare.read_block(4)
        print(block_data)

	block_data = mifare.read_block(8)
        print(block_data)

	block_data = mifare.read_block(12)
        print(block_data)

	block_data = mifare.read_block(16)
        print(block_data)

    except nxppy.SelectError:
	
        # SelectError is raised if no card is in the field.
        pass
		
    time.sleep(1)

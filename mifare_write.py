import nxppy
import time
import sys

mifare = nxppy.Mifare()

#Write to the starting address (OVERWRITE) ----> page 4

print "Make sure the NFC tag is in contact"

#get input
id = raw_input('Enter the ID: ')

while True:
    try:
	uid = mifare.select()

	byte1 = id[0:4]
	byte2 = id[4:8]
	byte3 = id[8:12]

	print (byte1)
	print (byte2)
	print (byte3)

	# Write a single block of 4 bytes
	mifare.write_block(4, byte1)		#OR mifare.write_block(5,b'abcd')
	mifare.write_block(5, byte2)
	mifare.write_block(6, byte3)

	print "Data is Successfully written"	

	break
    except nxppy.SelectError:
        # SelectError is raised if no card is in the field.
        pass

    time.sleep(1)

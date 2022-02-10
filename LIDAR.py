import smbus

# I2C channel 1 is connected to the GPIO pins
channel = 1

#  TOF10120 defaults to I2C bus address 0x52
address = 0x52

# Register address to store data reads
reg_distance = 0x00

# Initialize I2C (SMBus)
bus = smbus.SMBus(channel)

def read_sensor():
    # read two bytes
    val =  bus.read_i2c_block_data(address, reg_distance, 2)
    # form a 16 bit word for the data to produce output in millimeters
    millimeters = val[0] << 8 | val[1]
    # convert to inches
    inches = millimeters * 0.0393701
    # prep for output in inches
    distance = round(inches)

    return distance
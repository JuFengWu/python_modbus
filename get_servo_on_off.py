import serial

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

PORT = "com7"

logger = modbus_tk.utils.create_logger("console")


try:
  #master = modbus_rtu.RtuMaster(serial.Serial(port=PORT, baudrate=38400, bytesize=8, parity='N', stopbits=1)) #old 
  master = modbus_rtu.RtuMaster(serial.Serial(port=PORT, baudrate=19200, bytesize=8, parity='N', stopbits=1)) #new
  master.set_timeout(5.0)
  master.set_verbose(True)
  print("connected")
  value = master.execute(1, cst.READ_HOLDING_REGISTERS, 0x100C, 1)
  print(value)
  #value = master.execute(1, cst.READ_HOLDING_REGISTERS, 0x1025, 1)
  #print(value)
  master.close()
  
except modbus_tk.modbus.ModbusError as exc:
  print("%s- Code=%d", exc, exc.get_exception_code())

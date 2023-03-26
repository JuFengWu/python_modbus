import serial

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

PORT = "com1"

logger = modbus_tk.utils.create_logger("console")

try:
  master = modbus_rtu.RtuMaster(serial.Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0))
  master.set_timeout(5.0)
  master.set_verbose(True)
  logger.info("connected")
  logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0x2042, output_value=[1])) # servo on
  
except modbus_tk.modbus.ModbusError as exc:
  logger.error("%s- Code=%d", exc, exc.get_exception_code())
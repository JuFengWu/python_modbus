import serial
import modbus_tk
from modbus_tk import modbus_rtu
import modbus_tk.defines as cst
PORT = "COM2"

logger = modbus_tk.utils.create_logger("console")

try:
  master = modbus_rtu.RtuMaster(serial.Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1))
  master.set_timeout(5.0)
  master.set_verbose(True) #怕被干擾，是否重發
  value = master.execute(1, cst.READ_HOLDING_REGISTERS, 0x1, 2) 
  #execute(slave,功能,開始地址,長度)
  print("success get data")
  print(value)
  logger.info(value)
  master.close()
except modbus_tk.modbus.ModbusError as exc:
  print("there is error")
  print("%s- Code=%d", exc, exc.get_exception_code())

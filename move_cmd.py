import serial

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

PORT = "com7"

logger = modbus_tk.utils.create_logger("console")

target = 1 #140mm

try:
  #master = modbus_rtu.RtuMaster(serial.Serial(port=PORT, baudrate=38400, bytesize=8, parity='N', stopbits=1))
  master = modbus_rtu.RtuMaster(serial.Serial(port=PORT, baudrate=19200, bytesize=8, parity='N', stopbits=1))
  master.set_timeout(5.0)
  master.set_verbose(True)
  logger.info("connected")
  value = master.execute(1, cst.WRITE_MULTIPLE_REGISTERS , 0x2042, 1 , [1]) # 1 -> set servo on, 0 -> set Servo off
  
  print(value)
  logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0x2044,  1 , [0])) #IN4 start = 0
  logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0x9010,  1 , [1])) # 1 ABS 絕對位置移動 0 INC 相對位置移動, change to 16:ABS-T 絕對位置移動 [ 扭力模式 ]?

  pulse = target * 100
  
  data1 = pulse & 0x0000FFFF
  data2unit = (pulse & 0xFFFF0000) >> 16
  data2 = data2unit & 0x0000FFFF
  logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0x9011,  2 , [data2,data1])) # target in pulse
  logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0x9013,  1 , [10])) # speed 0 is default
  logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0x9014,  1 , [1000])) #max torque
  print("max torque")
  logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0x9016,  2 , [0,0])) # set as 0
  print("set bondary 0 ")
  logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0x9018,  2 , [0,2])) # set as 0
  print("set bondary 0 ")

  logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0x901A,  1 , [500])) # acc
  logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0x901B,  1 , [500])) #dacc
  logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0x901C,  1 , [0])) # stop time
  logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0x901D,  1 , [65535])) # -1 in unit16

  logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0x2045,  1 , [1])) # In5~In11 ->PRGSEL 0 ~PRGSEL6 -> select point 1
  logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0x2046,  1 , [0]))
  logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0x2047,  1 , [0]))
  logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0x2048,  1 , [0]))
  logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0x2049,  1 , [0]))
  logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0x204A,  1 , [0]))
  logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0x204B,  1 , [0])) #IN 4 start = 1

  logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0x2044,  1 , [1]))

  
  master.close()
  
  
except modbus_tk.modbus.ModbusError as exc:
  logger.error("%s- Code=%d", exc, exc.get_exception_code())

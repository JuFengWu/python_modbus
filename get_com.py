import serial.tools.list_ports

def list_all_com_ports():
    ports = serial.tools.list_ports.comports()
    available_ports = []
    for port in ports:
        available_ports.append((port.device))
    return available_ports

def main():
    com_ports = list_all_com_ports()
    if com_ports:
        print("Available COM Ports:")
        for port in com_ports:
            print(f"Port: {port}")
    else:
        print("No COM ports available.")

if __name__ == "__main__":
    main()

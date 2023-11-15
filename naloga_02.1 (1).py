import struct
import serial

# funkcija pack(payload) pakira podatke za posiljanje preko serijske povezave
def pack(payload):
    # glava paketa
    head = (0xAA, 0x55)  
    # dolzina podatkov
    length = len(payload)  
    # format pakiranja podatkov
    string = '!BBB' + 'B' * length
    # pakiranje podatkov
    pack = struct.pack(string, *head, *payload, length)
    return pack

# ustvarjanje serijske povezave na COM6 s hitrostjo 9600 bps
mySerial = serial.Serial("COM6", 9600) # mode

# preveri, ali je serijska povezava odprta, in jo izpise
if mySerial.is_open:
    print("Odpiranje serijskega porta!")

myCommands = {
    "LED_ON": [0x19], "LED_OFF": [0x20],
    "LED_08_ON": [0x01], "LED_08_OFF": [0x011],
    "LED_09_ON": [0x02], "LED_09_OFF": [0x012],
    "LED_10_ON": [0x03], "LED_10_OFF": [0x013],
    "LED_11_ON": [0x04], "LED_11_OFF": [0x014],
    "LED_12_ON": [0x05], "LED_12_OFF": [0x015],
    "LED_13_ON": [0x06], "LED_13_OFF": [0x016],
    "LED_14_ON": [0x07], "LED_14_OFF": [0x017],
    "LED_15_ON": [0x08], "LED_15_OFF": [0x018],
    "ANIMACIJA_ON": [0x21], "ANIMACIJA_OFF": [0x26],
    "HELP": None,
}

myHelp = [
    "LED_ON (Vklopi vse dijode)", "LED_OFF (Izklopi vse dijode)",
    "LED_08_ON (Vklopi dijodo 1)", "LED_08_OFF (Izklopi dijodo 1)",
    "LED_09_ON (Vklopi dijodo 2)", "LED_09_OFF (Izklopi dijodo 2)",
    "LED_10_ON (Vklopi dijodo 3)", "LED_10_OFF (Izklopi dijodo 3)",
    "LED_11_ON (Vklopi dijodo 4)", "LED_11_OFF (Izklopi dijodo 4)",
    "LED_12_ON (Vklopi dijodo 5)", "LED_12_OFF (Izklopi dijodo 5)",
    "LED_13_ON (Vklopi dijodo 6)", "LED_13_OFF (Izklopi dijodo 6)",
    "LED_14_ON (Vklopi dijodo 7)", "LED_14_OFF (Izklopi dijodo 7)",
    "LED_15_ON (Vklopi dijodo 8)", "LED_15_OFF (Izklopi dijodo 8)",
    "ANIMACIJA_ON (Vklopi animacijo)", "ANIMACIJA_OFF (Izklopi oz. ustavi animacijo)"
]

while True:
    commandOut = input("Vnesite želen ukaz: ")

    # preveri, ali je vneseni ukaz veljaven
    if commandOut in myCommands:
        payload = myCommands[commandOut]

        if payload is None:
            print("UKAZI:")
            for cmd in myHelp:
                print(f"{cmd}")
            continue

        if "ANIMACIJA_ON" in commandOut:
            led_config = [0x00] * 8

            # uporabnik lahko izbere diode, ki bodo vkljucene v animacijo
            while True:
                led_number = input("Vnesite stevilko LED (1-8) za vkljucitev v animacijo (0 za zakljucek izbiranja): ")
                if led_number == '0':
                    break
                led_index = int(led_number) - 1
                led_config[led_index] = int(led_number)
                print(led_config)
            payload = payload + led_config

        # pakiranje podatkov in posiljanje prek serijske povezave
        packetOut = pack(payload)
        mySerial.write(packetOut)
        print(f"Podatki: {payload}")
        print(f"Paket za posiljanje: {packetOut}")

    else:
        print("NAPAKA!")

# zapiranje serijske povezave
mySerial.close()

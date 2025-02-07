def on_mqtt_qos_list_qos2(message):
    if message == "1":
        OLED.write_string_new_line("Turn on the light")
    elif message == "2":
        OLED.write_string_new_line("Turn off the light")
    elif message == "3":
        OLED.write_string_new_line("Turn on the fan")
    elif message == "4":
        OLED.write_string_new_line("Turn off the fan")
ESP8266_IoT.mqtt_event("myhome/bedroom/remote-control",
    ESP8266_IoT.QosList.QOS2,
    on_mqtt_qos_list_qos2)

def on_button_pressed_a():
    ESP8266_IoT.publish_mqtt_message(convert_to_text(randint(1, 4)),
        "myhome/bedroom/remote-control",
        ESP8266_IoT.QosList.QOS1)
input.on_button_pressed(Button.A, on_button_pressed_a)

id2 = 0
basic.show_number(0)
huskylens.init_i2c()
basic.show_number(1)
huskylens.init_mode(protocolAlgorithm.ALGORITHM_FACE_RECOGNITION)
basic.show_number(2)
OLED.init(128, 64)
basic.show_number(3)
name = ["Anson Lo", "Lokman", "Edan Lui", "Anson Kong"]
basic.show_number(4)
basic.show_number(0)
ESP8266_IoT.init_wifi(SerialPin.P8, SerialPin.P12, BaudRate.BAUD_RATE115200)
ESP8266_IoT.connect_wifi("ssid", "password")
clientID = randint(0, 99999999)
basic.show_number(1)
ESP8266_IoT.set_mqtt(ESP8266_IoT.SchemeList.TCP,
    convert_to_text(clientID),
    "test",
    "test",
    "")
ESP8266_IoT.connect_mqtt("192.168.0.32", 1884, False)
basic.show_number(2)
OLED.init(128, 64)
basic.show_number(3)
basic.pause(2000)
if ESP8266_IoT.is_mqtt_broker_connected():
    basic.show_icon(IconNames.YES)

def on_forever():
    global id2
    huskylens.request()
    id2 = huskylens.readBox_s(Content3.ID)
    if id2 > 0:
        basic.pause(100)
        basic.show_number(id2)
        OLED.clear()
        OLED.write_string_new_line(name[id2 - 1])
basic.forever(on_forever)

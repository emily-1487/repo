####################匯入模組####################
import socket

####################宣告與設定####################
client_socket = socket.socket()  # 建立socket
client_socket.connect(("192.168.1.103", 5438))  # 連線到伺服器
####################主程式####################
while True:
    msg = input("請輸入訊息:")  # 輸入想要傳送到伺服器的訊息
    client_socket.send(msg.encode("utf8"))  # 將訊息轉換為位元組後傳送到伺服器
    reply = client_socket.recv(128).decode("utf8")  # 接收伺服器回應的訊息並解碼
    if reply == "quit":
        print("Disconnected")
        client_socket.close()
        break
    print(reply)

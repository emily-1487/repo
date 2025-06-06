####################匯入模組####################
import socket

####################宣告與設定####################
HOST = "localhost"  # IP
PORT = 5438  # PORT
server_socket = socket.socket()  # 建立socket
server_socket.bind((HOST, PORT))  # 綁定IP和PORT
server_socket.listen(5)  # 最大連接數量，超過則拒絕連接
print("Serve:{}port:{}start".format(HOST, PORT))  # 顯示伺服器IP和PORT
client, addr = server_socket.accept()  # 接收客戶端連線，返回客戶端socket和地址
print("client address:{},port:{}".format(addr[0], addr[1]))
####################主程式####################
while True:
    msg = client.recv(128).decode(
        "utf8"
    )  # 接收客戶端發送的資料，100為接收訊息最大長度，utf8為解碼方式
    print("Recieve Message:" + msg)
    reply = ""  # 建立伺服器回應文字
    if msg == "Hi":
        reply = "Hello"  # 將文字次轉換為位元組，因為socket只能傳送位元組
    elif msg == "Bye":
        client.send(b"quit")
        break
    else:
        reply = "What??"
        client.send(reply.encode("utf8"))
client.close()  # 關閉與客戶端溝通
server_socket.close()  # 關閉伺服器

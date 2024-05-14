# TCP-client-server
establish a basic client-server communication over TCP/IP.


**server.py**

Description:
This Python script sets up a basic TCP server that listens for incoming connections on a specified IP address and port. When a client connects, it accepts the connection, prints out information about the client, and starts a new thread to handle the client's requests. The server acknowledges each received message with a simple "ACKKK" response.

Usage:
1. Save the code as `server.py` in your preferred directory.
2. Ensure you have Python installed on your system.
3. Open a terminal or command prompt.
4. Navigate to the directory where `server.py` is saved.
5. Run the script using the command: `python server.py`.
6. The server will start listening for incoming connections on IP address `0.0.0.0` and port `9998`.
7. Once a client connects, the server will print out information about the client's address.
8. The server will handle each client connection in a separate thread, allowing it to handle multiple clients simultaneously.
9. You can customize the server's behavior by modifying the `handle_client` function as needed.

---

**client.py**

Description:
This Python script acts as a TCP client that connects to a specified server (host) and port. It sends a simple HTTP GET request to the server and receives the response. In this example, it sends a GET request to `google.com` and prints the response received from the server.

Usage:
1. Save the code as `client.py` in your preferred directory.
2. Ensure you have Python installed on your system.
3. Open a terminal or command prompt.
4. Navigate to the directory where `client.py` is saved.
5. Run the script using the command: `python client.py`.
6. The client will attempt to connect to the server running on `127.0.0.1` (localhost) and port `9998`.
7. It sends a simple HTTP GET request to the server.
8. The client then receives the response from the server and prints it.
9. After executing, the client will close the connection to the server.

---

**Note:** Ensure that the server (`server.py`) is running before executing the client (`client.py`). You can modify the host and port in the client script to connect to a different server if needed. Additionally, remember to handle exceptions and errors appropriately when deploying these scripts in a production environment.

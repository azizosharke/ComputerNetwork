# https://abdesol.medium.com/udp-protocol-with-a-header-implementation-in-python-b3d8dae9a74b
import socket
import tkinter as tk
import time


def transmitFile(hostAddress, fileName):
    socketVar = socket.socket()
    port = 8090
    socketVar.connect((hostAddress, port))


    numOfPackets = int(packetLength / 1024) + 1
    print(packetLength)
    print(fileName)
    print(numOfPackets)

    time.sleep(1)
    stringNumOfPackets = str(numOfPackets)
    encodedStringNumOfPackets = stringNumOfPackets.encode()
    socketVar.send(encodedStringNumOfPackets)

    # loop to keep sending packets and prints the packet number that is being sent
    for x in range(1, numOfPackets + 1):
        numOfPacketsSend_String = f"Sending packet #{x} "
        print(numOfPacketsSend_String)

    # displays that the data has been sent successfully
    print("\nPackets has been sent successfully!")

    return


def closeProgram(event):
    # closes the program
    window.quit()
    return


def forwardMessages(event):

    hostAddress = ent_destination.get()
    fileName = ent_fileName.get()
    window.destroy()
    transmitFile(hostAddress, fileName)

    # Display the confirmation the file sent
    lbl_FileSent = tk.Label(text="The message has been sent.")
    lbl_FileSent.pack()
    btn_confirmExit = tk.Button(text="Click to exit.", width=16, height=2)
    btn_confirmExit.pack()
    btn_confirmExit.bind('<Button-1>', closeProgram)

    return


defaultServerName = socket.gethostname()
window = tk.Tk()


ent_destination = tk.Entry()
ent_destination.pack()
ent_destination.insert(0, defaultServerName)


lbl_getFileName = tk.Label(text="\n Testing forwarders")
ent_fileName = tk.Entry()
lbl_getFileName.pack()
ent_fileName.pack()


window.mainloop()  # GUI loop

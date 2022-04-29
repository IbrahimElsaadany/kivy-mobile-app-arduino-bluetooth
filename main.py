from kivy.app import App
from jnius import autoclass
from kivy.lang.builder import Builder
kv='''
GridLayout:
    size:root.width,root.height
    cols:1
    Button:
        text:'ON'
        font_size:100
        on_press:app.on()
    Button:
        text:'OFF'
        font_size:100
        on_press:app.off()'''
BluetoothAdapter = autoclass('android.bluetooth.BluetoothAdapter')
UUID = autoclass('java.util.UUID')
def get_socket_stream() :
    socket=None
    PairedDevices=BluetoothAdapter.getDefaultAdapter().getBondedDevices().toArray()
    for device in PairedDevices :
        if device.getName()=='HC-05' : # The Default name of your device (even if you changed it on your mobile to other name)
            socket=device.createRfcommSocketToServiceRecord(
                UUID.fromString("00001101-0000-1000-8000-00805F9B34FB"))
            send_stream=socket.getOutputStream()
            # recv_stream=socket.getInputStream() => If you want to recieve
            break
    socket.connect()
    return send_stream
class myApp(App) :
    def build(self) :
        self.send_stream=get_socket_stream()
        return Builder.load_string(kv)
    def on(self) :
        self.send_stream.write(b'1')
        self.send_stream.flush()
    def off(self) :
        self.send_stream.write(b'0')
        self.send_stream.flush()
if __name__=='__main__':
    myApp().run()
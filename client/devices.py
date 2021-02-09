import requests

class Device:
    def __init__(self, device_type, device_name, address, state):
        print('Creating device ' + str(device_name))
        self.address = address
        self.state = state
        self.device_name = device_name
        self.device_type = device_type
        self.url = 'http://127.0.0.1:5000'
        print('Device ' + str(device_name) + ' was created')

    def printDevice(self):
        print('============================')
        print('Device state: ' + str(self.state))
        print('Device type: ' + str(self.device_type))
        print('Device name: ' + str(self.device_name))
        print('Device address: ' + str(self.address))
        print('============================')

    def changeState(self):
        if self.state is not 'OFF':
            self.state = 'OFF'
        else:
            self.state = 'ON'
        print('labadaba')
        self.update()
        self.printDevice()
    def update(self):
        r = requests.put(self.url +'/item/' + self.device_name + ' / put', data ={'state': self.state})
        print(r)
        
class DeviceManager:
    def __init__(self):
        self.url = 'http://127.0.0.1:5000'
        self.devices = self.getDevices()

    def getDevices(self):
        list_of_devices = []
        r = requests.get(url = self.url + '/items')
        data = r.json()
        for device in data['items']:
            list_of_devices.append(Device(device['type'], device['name'],
            device['address'], device['state']))
        for device in list_of_devices:
            device.printDevice()
        return list_of_devices


if __name__ == '__main__':
    device = Device('ESP32', 'ESP1', '192.168.12.11', "OFF")
    device.printDevice()
    device.changeState()
    device.printDevice()
    mgr = DeviceManager()

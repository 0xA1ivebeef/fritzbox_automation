
from fritzconnection import FritzConnection

FRITZBOX_IP = 'xxx.xxx.x.x' # standard '192.168.178.1'
PASSWORD = '' # set device password (!!! NOT WIFI PASSWORD !!!)

def get_ssid_visibility(fc, wlan_service):
    result = fc.call_action(wlan_service, 'GetBeaconAdvertisement')
    # result example: {'NewBeaconAdvertisementEnabled': True} or False
    return result['NewBeaconAdvertisementEnabled']

def set_ssid_visibility(fc, wlan_service, enable):
    fc.call_action(wlan_service, 'SetBeaconAdvertisement', NewBeaconAdvertisementEnabled=enable)

def toggle_ssid():
    fc = FritzConnection(address=FRITZBOX_IP, password=PASSWORD)
    wlan_service = 'WLANConfiguration1'  # or 2 or 3 as needed
    current = get_ssid_visibility(fc, wlan_service)
    print(current)

    set_ssid_visibility(fc, wlan_service, not current)
    print(f"SSID visibility changed from {current} to {not current} on {wlan_service}")

if __name__ == '__main__':
    toggle_ssid()


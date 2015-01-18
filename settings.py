__author__ = 'marion'


# http://cloudbrain.rocks
CLOUDBRAIN_ADDRESS = '127.0.0.1'


#TagID => MuseID
TAGS = {
    "ce9686e5": 5008,
    "5b64d6ec": 5009,
    "a52df735": 5010,
    "3153f935": 5011,
    "9b68d5ec": 5012,
    "82ecf735": 5013,
    "00b2f735": 5014,
    "7385368c": 5015
}


#CoreID => Booth Name
CORES = {
    "53ff6e065067544819260487": "muse-manager",
    "53ff68066667574815362067": "booth-1",
    "54ff6d066667515116121567": "booth-2",
    "54ff68066667515151331467": "booth-3",
    "54ff70066667515149111567": "booth-4",
    "53ff70066667574808432167": "booth-5",
    "53ff6d066667574823302067": "booth-6",
    "50ff6d065077494946390787": "booth-7",
    "54ff6c066667515150321467": "booth-8",
    "53ff6d066667574834382167": "booth-9",
    "53ff76066667574859372167": "booth-10",
    "53ff6a066667574841132167": "booth-11",
    "53ff72066667574858362167": "booth-12"
}

#Booth Name => {"ip" => IP Address, "required_routes" => [[pub_metric, sub_metric], [pub_metric, sub_metric], ...]}
BOOTHS = {
    "muse-manager": {"ip": "10.0.0.2", "required_routes": [["batt", "battery-muse9"],["horseshoe", "horseshoe-muse9"],["touching_forehead", "touching-muse9"]]},
    "booth-1": {"ip": "10.0.0.201", "required_routes": [["eeg", "eeg"], ["mellow", "mellow"], ["concentration", "concentration"]]},
    "booth-2": {"ip": "10.0.0.202", "required_routes": [["eeg", "eeg"], ["mellow", "mellow"], ["concentration", "concentration"]]},
    "booth-3": {"ip": "10.0.0.203", "required_routes": [["eeg", "eeg"], ["mellow", "mellow"], ["concentration", "concentration"]]},
    "booth-4": {"ip": "10.0.0.204", "required_routes": [["eeg", "eeg"], ["mellow", "mellow"], ["concentration", "concentration"]]},
    "booth-5": {"ip": "10.0.0.205", "required_routes": [["eeg", "eeg"], ["mellow", "mellow"], ["concentration", "concentration"]]},
    "booth-6": {"ip": "10.0.0.206", "required_routes": [["eeg", "eeg"], ["mellow", "mellow"], ["concentration", "concentration"]]},
    "booth-7": {"ip": "10.0.0.207", "required_routes": [["eeg", "eeg"], ["mellow", "mellow"], ["concentration", "concentration"]]},
    "booth-8": {"ip": "10.0.0.208", "required_routes": [["eeg", "eeg"], ["mellow", "mellow"], ["concentration", "concentration"]]},
    "booth-9": {"ip": "10.0.0.209", "required_routes": [["eeg", "eeg"], ["mellow", "mellow"], ["concentration", "concentration"]]},
    "booth-10": {"ip": "10.0.0.210", "required_routes":  [["eeg", "eeg"], ["mellow", "mellow"], ["concentration", "concentration"]]},
    "booth-11": {"ip": "10.0.0.211", "required_routes":  [["eeg", "eeg"], ["mellow", "mellow"], ["concentration", "concentration"]]},
    "booth-12": {"ip": "10.0.0.212", "required_routes":  [["eeg", "eeg"], ["mellow", "mellow"], ["concentration", "concentration"]]}
}

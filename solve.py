import yaml
import sys
import argparse
import numpy as np

description = "This program is a solver for finding the electromotive force of coils in a uniform magnetic field of a magnetic monopole."
parser = argparse.ArgumentParser(description=description)

parser.add_argument("-c", "--config", type=str, default="./config.yaml", help="Specify the configuration path.")

args = parser.parse_args()



class Probe:
    def __init__(self, position):
        self.position = np.array(position)

class MagnetField(Probe):
    def __init__(self, js):
        super().__init__(js["pos"])
        self.size = np.array(js["size"])
        self.division_size = np.array(js["div"])

class ReferencePoint(Probe):
    def __init__(self, js):
        super().__init__(js["pos"])



if __name__ == "__main__":
    # loading config.yml
    try:
        with open(args.config, "r", encoding="utf-8") as f:
            js = yaml.safe_load(f)
    except Exception as e:
        print("Exception occured while loading config.yaml", file=sys.stderr)
        print(e, file=sys.stderr)
        sys.exit(1)

    for item in js["probes"]:
        if item["type"] == "magnetic field":
            pass
        elif item["type"] == "reference point":
            pass
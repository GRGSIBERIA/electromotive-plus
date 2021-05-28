import yaml
import sys
import argparse
import numpy as np

description = "This program is a solver for finding the electromotive force of coils in a uniform magnetic field of a magnetic monopole."
parser = argparse.ArgumentParser(description=description)

parser.add_argument("-c", "--config", type=str, default="./config.yaml", help="Specify the configuration path.")

args = parser.parse_args()



class Probe:
    def __init__(self, position: np.ndarray, output_path:str):
        self.position = np.array(position)
        self.output_path = output_path

class MagnetField(Probe):
    def __init__(self, js):
        super().__init__(js["position"], js["output"])
        self.size = np.array(js["size"])
        self.divide = np.array(js["divide"])

class ProbeReferencePoint(Probe):
    def __init__(self, js):
        super().__init__(js["position"], js["output"])



class Coil:
    def __init__(self, position):
        self.position = np.array(position)

class Solenoid(Coil):
    def __init__(self, js):
        super().__init__(js["position"])

        self.radius = float(js["radius"])
        self.wire_resistance = float(js["wire resistance"])
        self.turns = float(js["turns"])
        self.wire_diameter = float(js["wire diameter"])
        self.direction = np.array(js["direction"])
        self.height = float(js["height"])
        
        rounds = 2. * np.pi * self.radius
        self.wire_length = self.turns * rounds    # mm
        self.all_resistance = (4. * self.wire_resistance * self.wire_length) / (np.pi * self.wire_diameter**2.)

        if js["extrude direction"] == "positive":
            self.top_position = self.position
            self.bottom_position = self.position + self.direction * self.height
        elif js["extrude direction"] == "negative":
            self.bottom_position = self.position
            self.top_position = self.position + self.direction * self.height
        elif js["extrude direction"] == "center":
            self.top_position = self.position + self.direction * self.height * 0.5
            self.bottom_position = self.position - self.direction * self.height * 0.5


class Element:
    def __init__(self, js):
        pass

class NodeReferencePoint(Element):
    def __init__(self, js):
        super().__init__(js)


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
    
    for item in js["coils"]:
        if item["type"] == "solenoid":
            pass

    for item in js["elements"]:
        if item["type"] == "ferromagnet":
            pass
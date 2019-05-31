import argparse
import json


def command_line_argument_parser():
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description='Help for Command line arguments')
    parser.add_argument("configFile", help="Name Configuration file")
    command_line_params = parser.parse_args()
    return decode_command_line_params(command_line_params.configFile)


def decode_command_line_params(filename):
    env ={}
    with open(filename) as json_file:
        data = json.load(json_file)

        if "Dataset" in data:
                env["Dataset"] = data["Dataset"]
        else:
            raise Exception(" Error Datset Name not specified in config file")

        if "filename" in data:
                env["filename"] = data["filename"]
        else:
            raise Exception ("Error Dataset File not found")

        if "WindowSize" in data:
                env["WindowSize"] = data["WindowSize"]
        else:
                env["WindowSize"] = 0.01

        if "split_ratio" in data:
                env["split_ratio"] = data["split_ratio"]
        else:
                env["split_ratio"] = 0.3

    return env

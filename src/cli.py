import argparse

# Create the parser
parser = argparse.ArgumentParser(add_help=False)

# Add the arguments
parser.add_argument("-e", "--eg", type=str, help="start−up example")
parser.add_argument("-d", "--dump", type=str, help="on test failure, exit with stack dump")
parser.add_argument("-f", "--file", type=str, help="file with csv data")
parser.add_argument("-h", "--help", type=str, help="show help")
parser.add_argument("-n", "--nums", type=str, help="number of nums to keep")
parser.add_argument("-s", "--seed", type=str, help="random number seed")
parser.add_argument("-S", "--seperator", type=str, help="feild seperator")

args = parser.parse_args()
print(args.eg)
import argparse

parser = argparse.ArgumentParser(description='Launch a render!')

parser.add_argument('show',nargs = 1, type=str, help="helga show name")
parser.add_argument('sequence',nargs = 1, type=str, help='sequence name')
parser.add_argument('shot',nargs = 1, type=str, help='shot name')
#the file argument type maybe should be 'file'
#for testing purposes right now it is 'str'
parser.add_argument('file',nargs=1, type=str, help='file to render')
parser.add_argument('rp', nargs=1, help='render package to use')
#is it once through the whole launch script for each layer or all layers in one run of the script?
parser.add_argument('layer', nargs='+', type=str, help='layer(s) to render')
parser.add_argument('-frange', nargs=1, type=str, required=True, help='REQUIRED: frame range')
parser.add_argument('-scale', nargs=1, type=float, default = 1, help='resolution scale multiplier (default 1)')
parser.add_argument('-service', nargs=1, type=str, help='optional service tag for spool')

args = parser.parse_args()

#and now do we pass this off to our relevant render package scripts?
print args

import pathManager
import Multimedia
from glob import glob

import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input_folder", required=True,
                help="frames folder")
ap.add_argument("-fps", "--frame_rate", required=True,
                help="frame rate")
ap.add_argument("-o", "--output_file", default="./sequence.avi",
                help="Output folder")
args = vars(ap.parse_args())

input_folder= args['input_folder']
output_file = args['output_file']
fps = float(args['frame_rate'])

#files = pathManager.find_paths(input_folder,is_sorted=True)

files = []
files.extend(sorted(glob(input_folder)))

if len(files)!=0:
    Multimedia.video_from_frames(files,output_file,fps)
else:
    print('\n Error: No file found')



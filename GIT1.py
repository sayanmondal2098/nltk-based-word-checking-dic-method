import h5py

import io
import skimage.io

import matplotlib


file_path = "datasets/input_recording.h5"

with h5py.File(file_path, "r") as f:
    for key in f.keys():
        print(key)

prefix = "1517520748.6461143"

with h5py.File(file_path, "r") as f:
    game_buffer_frames = [skimage.io.imread(io.BytesIO(b)) for b in f[f"{prefix}-frames"].value]
    
skimage.io.imshow_collection(game_buffer_frames)


skimage.io.imshow(game_buffer_frames[3])



with h5py.File(file_path, "r") as f:
    for key in f.keys():
        if key.endswith("keyboard-inputs"):  # or keyboard-inputs-active / mouse-inputs
            inputs = f[key].value
            
            if len(inputs):
                print(inputs)


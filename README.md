# Hex Color Extractor

- Extract all hex colors from images

## Usage

1. Download [this repo](https://github.com/VMPYRC/Hex-Color-Extractor/archive/refs/heads/main.zip)
2. Extract the .zip file
3. Open in Terminal
4. Dependencies: `pip install pillow`
5. Place images in the `images` folder
6. Run the script: `python extract_colors.py`
7. Check the files in the `outputs` folder
8. Repeat steps 5 and 6 for new images

## Example Output for 'sample.png`

**TXT**

```
Dimensions: 9 x 9
Total Pixels: 81

Hex | Count | Percentage
Transparent | 17 | 20.99%
#ff7799 | 16 | 19.75%
#7777bb | 16 | 19.75%
#0099cc | 16 | 19.75%
#ffffff | 12 | 14.81%
#000000 | 4 | 4.94%
```

**CSV**

|  Hex Color  | Count | Percentage |
| :---------: | :---: | :--------: |
| Transparent |  17   |   20.99%   |
|   #ff7799   |  16   |   19.75%   |
|   #7777bb   |  16   |   19.75%   |
|   #0099cc   |  16   |   19.75%   |
|   #ffffff   |  12   |   14.81%   |
|   #000000   |   4   |   4.94%    |

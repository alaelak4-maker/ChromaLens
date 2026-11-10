# ChromaLens
# ChromaLens 🎨

A Python tool that names the **approximate color** of a pixel in an image or a live webcam, to help people with color vision deficiency (CVD) identify colors.

> My first personal project as a biomedical engineering student.

## What it does

- **Click mode (`click.py`):** click anywhere on an image and see the approximate name of that color.
- **Live mode (`live.py`):** point your webcam at an object and the circle in the center shows the color's name in real time.

ChromaLens does **not** restore color vision or diagnose anything. It tells you what a color is called. Names are approximate (see Limitations).

## Demo

[Add a screenshot or GIF here: drag an image into this editor]

## How it works

1. A camera frame or image is an array of pixels, each stored as blue, green and red values (BGR) from 0 to 255.
2. The pixel is converted to **HSV** (hue, saturation, value), which separates the color itself from its brightness.
3. A decision ladder in `names.py` picks a name:
   - very dark → Black
   - very low saturation → White or Gray
   - otherwise the hue decides: Red, Orange/Brown, Yellow, Green, Blue, Purple, Pink
4. In live mode, an 11×11 patch of pixels is averaged first, so camera noise doesn't make the label flicker.

It runs in real time because it analyzes only a small patch per frame and relies on fast OpenCV and NumPy operations.

## Installation

Requires Python 3.

```
pip install opencv-python numpy
```

## Usage

**Live webcam:**
```
python live.py
```

**Click on an image:**
1. Put an image in the project folder.
2. Open `click.py` and change the filename on the `cv2.imread(...)` line to your image.
3. Run:
```
python click.py
```

Press `q` (with the window selected) to quit.

If the camera doesn't open on Windows, try `cv2.VideoCapture(0, cv2.CAP_DSHOW)` in `live.py`, and close other apps that use the webcam.

## Files

| File | Purpose |
|---|---|
| `names.py` | The `color_name(b, g, r)` function |
| `click.py` | Click-to-name on an image |
| `live.py` | Live webcam color naming |

## Limitations

- Names are **approximate**. Colors are sorted into about ten categories using thresholds I chose and tuned, so borderline colors (like brown vs. orange) can flip.
- **Lighting** and camera processing change the pixels before the code sees them. For example, white can look yellow under a warm lamp.
- Shiny or patterned surfaces may give unreliable results.
- Not tested with a large group of people with CVD yet. This is a learning project, not a medical device.

## Future ideas

- Screen mode: name the color under the cursor on any window, chart or website
- CVD simulation and color correction modes
- More color names and tuned thresholds
- Feedback

# BSL Interpreter

BSL Interpreter with [OpenCV](https://opencv.org/) and [TensorFlow Object Detection](https://github.com/tensorflow/models/blob/master/research/object_detection/README.md)
<br />
<br />
# Contents
* [About](#about)
* [Setup](#setup)
* [Usage](#usage)
* [Improvements](#improvements)
<br />

* * *

# About

<br />

BSL Interpreter is a project to explore machine learning applications for real time British Sign Language interpretation from video.

<br />
<img src="/images/demo.gif">

<br />

# Setup
* `$ pip install -r requirements.txt`
* Run gui.py


<br />

# Usage
* Cick "Start Interpreter" to begin
* Type "Q" to quit

<br />

### Video Call Integration
To use this interpreter within a video conferencing application such as Zoom, Skype or Google Duo, you must first create a virtual webcam.
One of the easiest ways to do this is with OBS Studio:
* With OBS Studio installed and open, start the sign interpreter
* In sources click '+' and select 'Window Capture'
* You should be able to select 'object detection from the list of window options
* Click 'Start Virtual Camera'. The virtual camera should now start.
* You can then choose this virtual camera in your video conferencing application settings.

<br />

# Improvements
The functionality of this model is still very limited. The model has been trained on photos of BSL signs and while I tried to include a variety of photos at 
different stages of the sign, the model still struggles to identify signs that rely heavily on movement to be understood i.e the model will often categorise 
the letter "J" has an "I" or an "A". The model also performs more poorly with more ambiguous signs, particularly those where facial expression is key such as
the difference between a question and a statement, although I beleive that this could be improved with a larger and more varied dataset.

To improve the model's accuracy/vocabulary you may want to train it yourself. There is more information and instructions on the [TensorFlow website](https://tensorflow-object-detection-api-tutorial.readthedocs.io/). 

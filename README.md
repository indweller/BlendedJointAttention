# Blended Classic Joint Attention Repository

<i> Pull requests from members other than that of Red Hen Labs would not be merged here. This is just a repository for temporary work. If you still believe that there is a threat to humanity which this repo may endure, you may send a mail to agarwalsoumitra1504[at]gmail[dot]com. If you wish to contribute to blended joint attention look at [this](https://github.com/RedHenLab/BlendedJointAttentionClean) repository.</i> 

This repository deals with work done by The Distibuted Red Hen Lab towards classification of different instances of blended classic joint attention in various form of print, audio and video media. For more information visit : https://sites.google.com/site/distributedlittleredhen/home/the-cognitive-core-research-topics-in-red-hen/the-barnyard/blended-classic-joint-attention

## Sub-repositories

### Face detection

Detection of number of human faces, possible extensions to their position and orientation. The files use Voila-Jones Haar classifier to detect human frontal and profile faces with the enhancement of template matching. The results can be seen as follows :

<img src = '/Face Detection/Result_Images/Result5.jpg'>

Template matching is a technique used to find a smaller image in a larger one. It works by sliding the small image accross the big one and it uses math to calculate which part of the bigger image is most likely to be the small image. This algorithm is nice because it always returns a value, unlike Haar cascades which is returns a position only if it finds a face.

<img src = '/Face Detection/Result_Images/img.png'>

### Emotion recognition

Recognising different emotions (sad, happy, surprised, neutral etc.) using a CNN classifier. To see and example run :

```python webcam-emotions.py --displayWebcam --seeFaces --netFile soumitra.p```

To get best results (and tailored for the person who is using the webcam app), you can use the `webcam-emotions.py` script to record data, as follows,(train happy by replacing sad by happy):

```python webcam-emotions.py --displayWebcam --seeFaces --gather_training_data  --recording_emotion sad```

### Gaze direction recognition 

Calculating angle of ones gaze using initial pupil detection and terminal points of eyes. The algorithm used was from the [paper](http://www.inb.uni-luebeck.de/fileadmin/files/PUBPDFS/TiBa11b.pdf) which deals with prediction of centre of the eye via gradients.

The step-wise procedure is as follows :

* Extraction of eyes from the face, via `Voila-Jones` Haar classifier
<img src = '/Gaze Direction/Result_Images/Result2.jpg'>
* Extracting and thresholding the area near the eyes so that the dark part is apparent
* Detection of blobs in the specified area
* Finding centre of the blob via the algorithms<br>
<img src = '/Gaze Direction/Result_Images/thresh_eye.jpg'><img src = '/Gaze Direction/Result_Images/eye1.jpg'><img src = '/Gaze Direction/Result_Images/eye2.jpg'>

Several other algorithms, including use of hough circles are present in `bin` which were descarded as second to the upgiven.

### Context recognition

Recognising what context is a specific scene in using Lucas-Kanade, optical flow. The following were the outputs in accordance to the used algorithms 

* Good features to track <br>
<img src = '/Context/image.jpg'><img src = '/Context/Good_Features.png'>

* Lucas-Kanade <br>
<img src = '/Context/LK.png'>

* Optical flow<br>
<img src = '/Context/Optical_flow.png'>

### Scene continuity 

Detection of a scene change by creating an average image at every new scene and calculating the difference with the newly observed. The following image would give a better insight into how the threshold and mean images were compared

<img src = '/Scene_Continuity/Scene2.png'>

The upgiven image was how the threshold changes at different instances with it being re-initialised once a new frame is detected. The following image is a pictorial representation of how much an image differs from another.

<img src = '/Scene_Continuity/Scene1.png'>

If this difference crosses a certain threshold, scene change is reported.

### Facial Landmark detection

Detecting major facial landmarks, which is useful for Gaze direction and Emotion recognition. Pre-built python library `Dlib` was used to create a mat of human facial features, with a little tweaking. The outputs are as follows 

<img src = '/Facial Features/Features1.png'>

### Head pose

Configuiring head pose to gaze direction and independent head pose estimation, via the features tracked in the Facial landmark repository. 

<img src = '/Head pose/output.gif' loop=10>

### Gesture Recognition

Recognising multimodal gestures. Since this required parsing through ELAN files and reading EAF for different gesture signals combined with video.

### Posture Recognition

Body posture recognition was worked upon using flowing puppets and Histogram of gradients.
Something like the walking posture can be seen here

<img src = '/Posture/result.jpg'>

### Window Size

The size and number of different windows is the giveaway clue to predicting whether Blended Classical Joint Attention exxists or not. Thus contour detection and shape matching techniques were used to predict the number of rectngular shapes.

<img src = '/Window Size/Result_Images/Temp.jpg'>

### Reaction Shots

Analyse reaction shots (of surprise, awe etc.) 


## Required Packages:

<ol>
	<li> Python 2.7.x </li>
	<li> Numpy </li>
	<li> Bob </li>
	<li> Matplotlib </li>
	<li> OpenCV (One must check compatibility with python and OS) </li>
	<li> DLib </li>
	<li> pympi-ling </li>
	<li> PySceneDetect </li>
	<li> Read </li>
</ol>

## Authors:

<ol>
 	<li> Dr.Mark Turner </li>
 	<li> Dr.Francis Steen </li>
	<li> <a href = "https://github.com/SoumitraAgarwal" target="_blank">Soumitra Agarwal</a> :neckbeard: </li>
	<li> Debayan Das </li>
</ol>

# Football Video Analysis with YOLO
## Project Overview
This project was built to detect and track players, referees, footballs, and goalkeepers in a video using YOLO, a state of the art AI object detection model. After extensive training of the model, I built trackers to track and assign players to teams based on the colors of their jerseys using KMeans for clustering and pixel segmmentation. Alongside this, the player closest to the ball is assigned possession, this information gives us a team's ball acquisition percentage throughout the match. 

<img width ="1280" src="https://github.com/EdrisAdel/FootballVisionAnalysis/blob/main/images/footballgithubimg.png">


## Features
- **Object Detection:** Detects players, referees, and the ball in each frame using a custom-trained YOLO model.
- **Tracking:** Assigns consistent IDs to players and the ball across frames for robust tracking.
- **Camera Movement Estimation:** Estimates and compensates for camera motion to improve tracking accuracy.
- **Ball Position Interpolation:** Smooths and fills in missing ball positions for continuous analysis.
- **Team Assignment:** Automatically clusters and assigns team colors to players.
- **Player-Ball Assignment:** Determines which player is in control of the ball at each frame.
- **Video Annotation:** Draws bounding boxes, team colors, and ball control information on output videos.

## Technologies used
- Python 3.8+
- Framework: PyTorch
- Libraries: scikit-learn, supervision, ultralytics, OpenCV, numpy, pandas
- Model: Yolo28X
- Roboflow for annotated dataset image training
# Trained YOLO model results
## Model summary (Training)
<img width ="1280" src="https://github.com/EdrisAdel/FootballVisionAnalysis/blob/main/images/githubtraining.png">

## Model Results
<img width ="1280" src="https://github.com/EdrisAdel/FootballVisionAnalysis/blob/main/images/training.png">

## Requirements
- Python 3.8+
- Docker (for local Roboflow inference server)

## Project Structure
- `main.py` — Main entry point for the analysis pipeline
- `trackers/` — Tracking and detection logic
- `utils/` — Utility functions for video and bounding box processing
- `output_videos/` — Annotated output videos
- `input-videos/` — Raw input videos

## Credits
- Built with [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) and [Roboflow Inference](https://github.com/roboflow/inference)

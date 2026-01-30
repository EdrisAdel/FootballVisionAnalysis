# Football Video Analysis with YOLO


## Features
- **Object Detection:** Detects players, referees, and the ball in each frame using a custom-trained YOLO/Roboflow model.
- **Tracking:** Assigns consistent IDs to players and the ball across frames for robust tracking.
- **Camera Movement Estimation:** Estimates and compensates for camera motion to improve tracking accuracy.
- **Ball Position Interpolation:** Smooths and fills in missing ball positions for continuous analysis.
- **Team Assignment:** Automatically clusters and assigns team colors to players.
- **Player-Ball Assignment:** Determines which player is in control of the ball at each frame.
- **Video Annotation:** Draws bounding boxes, team colors, and ball control information on output videos.

## Usage
1. Place your input videos in the `input-videos/` folder.
2. Run the main pipeline:
   ```bash
   python main.py
   ```
3. Annotated output videos will be saved in the `output_videos/` folder.

## Requirements
- Python 3.8+
- Docker (for local Roboflow inference server)

## Project Structure
- `main.py` — Main entry point for the analysis pipeline
- `trackers/` — Tracking and detection logic
- `utils/` — Utility functions for video and bounding box processing
- `output_videos/` — Annotated output videos
- `input-videos/` — Raw input videos
- `training/` — (gitignored) Training scripts and datasets

## Credits
- Built with [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) and [Roboflow Inference](https://github.com/roboflow/inference)

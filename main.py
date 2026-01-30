from trackers import Tracker
from roboflow import Roboflow
from team_assigner import TeamAssigner
from player_ball_assigner import PlayerBallAssigner
from camera_movement_estimator import CameraMovementEstimator
from dotenv import load_dotenv
from inference import get_model
from utils import read_video, save_video
import numpy as np
import os

load_dotenv()
API_KEY = os.getenv("ROBOFLOW_API_KEY")

def main():
    # Roboflow model used. Make sure to have Roboflow server running locally if using a local model
    rf = Roboflow(api_key=API_KEY)
    project = rf.workspace().project("footballanalysisproject-iczni")
    model = get_model(model_id="footballanalysisproject-iczni/1", api_key=API_KEY, base_url="http://localhost:9001")
    print("Roboflow model loaded.")
    
    #read video -------------- path for an input video
    video_frames = read_video('input-videos/08fd33_4.mp4')
    # Initialize Tracker
    tracker = Tracker(model)
    tracks = tracker.get_object_tracks(video_frames, 
                                    read_from_stub=True, 
                                    stub_path='stubs/track_stubs.pkl')
    
    #Get object positions
    tracker.add_position_to_tracks(tracks)
    #camera movement estimator
    camera_movement_estimator = CameraMovementEstimator(video_frames[0])
    camera_movement_per_frame = camera_movement_estimator.get_camera_movement(video_frames, 
                                                                            read_from_stub=True, 
                                                                            stub_path='stubs/camera_movement_stubs.pkl')
    camera_movement_estimator._adjust_positions_to_tracks(tracks, camera_movement_per_frame)
    #interpolate ball positions
    tracks["ball"] = tracker.interpolate_ball_positions(tracks["ball"])
    # # saved cropped image of a player for color assignment
    # for track_id, player in tracks["players"][0].items():
    #     bbox=player["bbox"]
    #     frame = video_frames[0]
    #     #crop bbox from frame 0
    #     cropped_image = frame[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]
    #     cv2.imwrite(f'output_videos/cropped_img.jpg', cropped_image)
    
    #Assign player teams (clustering)
    team_assigner = TeamAssigner()
    team_assigner.assign_team_color(video_frames[0],
                                    tracks["players"][0]) #tracks of players in the first frame
    for frame_num, player_track in enumerate(tracks["players"]):
        for player_id, track in player_track.items():
            team = team_assigner.get_player_team(video_frames[frame_num], 
                                                track["bbox"], 
                                                player_id)
            tracks["players"][frame_num][player_id]["team"] = team
            tracks["players"][frame_num][player_id]["team_color"] = team_assigner.team_colors[team] #in order to add anything to the tracks we would add a key and then assign a value to it
    #gol: less code in main
    #Assign ball to players
    player_assigner = PlayerBallAssigner()
    team_ball_control=[]
    for frame_num, player_track in enumerate(tracks["players"]):
        ball_bbox = tracks["ball"][frame_num][1]["bbox"]
        assigned_player = player_assigner.assign_ball_to_player(player_track,ball_bbox)
        if assigned_player != -1:
            tracks["players"][frame_num][assigned_player]["has_ball"] = True
            team_ball_control.append(tracks["players"][frame_num][assigned_player]["team"])
        else:
            team_ball_control.append(team_ball_control[-1])
    team_ball_control = np.array(team_ball_control)
    # Draw Annotations
    output_video_frames = tracker.draw_annotations(video_frames, tracks,team_ball_control)
    #Draw cam movement vectors
    output_video_frames = camera_movement_estimator.draw_camera_movement(output_video_frames, camera_movement_per_frame)
    # Save Video
    save_video(output_video_frames, 'output_videos/output_video.avi')

if __name__ == "__main__":
    main()
                                          
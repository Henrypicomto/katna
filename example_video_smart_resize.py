import os
import os.path
import cv2
from Katna.video import Video
import multiprocessing


def main():

    vd = Video()

    # folder to save resized video
    output_folder_resized_video = "resized_video"
    out_dir_path = os.path.join(".", output_folder_resized_video)

    if not os.path.isdir(out_dir_path):
        os.mkdir(out_dir_path)

    # number of images to be returned
    no_of_frames_to_returned = 20
    # VIdeo file path
    video_file_path = os.path.join(".", "tests", "data", "pos_video.mp4")
    print(f"Input video file path = {video_file_path}")

    vd.resize_video(abs_path_to_autoflip_build,
                     file_path,
                     abs_file_path_output,
                     output_aspect_ratio)

    print(f"output resized video file path = {abs_file_path_output}")


if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    main()

from moviepy.editor import VideoFileClip

def cut_reel(video_path, start, duration=30, output_path="reel.mp4"):
    clip = VideoFileClip(video_path).subclip(start, start + duration)
    clip.write_videofile(output_path, codec="libx264")

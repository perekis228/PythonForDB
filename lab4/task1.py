import moviepy.editor as me
import argparse
#lab4/task1.py -fname lab4/Videos/Video.mp4 -start 00:00 -end 00:10 -sname lab4/Videos/Clip.mp4

def main(file_name, start_time, end_time, save_name):
    try:
        start_time = int(start_time.split(':')[0])*60 + int(start_time.split(':')[1])
        end_time = int(end_time.split(':')[0])*60 + int(end_time.split(':')[1])
    except Exception:
        raise Exception("BadTimeErr: the time was entered incorrectly")

    try:
        clip = me.VideoFileClip(file_name)
        clip = clip.subclip(start_time, end_time)
        clip.write_videofile(save_name)
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Thumbnail Viewer")
    parser.add_argument("-fname", "--file_name", type=str, help="Input file name")
    parser.add_argument("-start", "--start_time", type=str, help="Input start time")
    parser.add_argument("-end", "--end_time", type=str, help="Input end time")
    parser.add_argument("-sname", "--save_name", type=str, help="Input save name")
    args = parser.parse_args()

    main(args.file_name, args.start_time, args.end_time, args.save_name)

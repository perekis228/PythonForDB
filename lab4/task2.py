import moviepy.editor as me
import argparse
#lab4/task2.py -fname ../lab4/Videos/Video.mp4 -start 00:00 -end 01:12 -sname ../lab4/Videos -step 30

def main(file_name, start_time, end_time, save_name, step=10):
    try:
        start_time = int(start_time.split(':')[0])*60 + int(start_time.split(':')[1])
        end_time = int(end_time.split(':')[0])*60 + int(end_time.split(':')[1])
        step = int(step)
    except Exception:
        raise Exception("BadTimeErr: the time was entered incorrectly")

    clip = me.VideoFileClip(file_name).resize(height=250)
    duration = clip.duration
    if duration < end_time:
        raise Exception("BadTimeErr: the time was entered incorrectly")

    count = 1
    for i in range(start_time, end_time, step):
        end = i+step
        if end_time < end:
            end = end_time
        subclip = clip.subclip(i, end)
        subclip.write_videofile(save_name+f'/Clip{count}.mp4')
        count += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Thumbnail Viewer")
    parser.add_argument("-fname", "--file_name", type=str, help="Input file name")
    parser.add_argument("-start", "--start_time", type=str, help="Input start time")
    parser.add_argument("-end", "--end_time", type=str, help="Input end time")
    parser.add_argument("-sname", "--save_name", type=str, help="Input save name")
    parser.add_argument("-step", "--step", type=str, help="Input step")
    args = parser.parse_args()

    main(args.file_name, args.start_time, args.end_time, args.save_name, args.step)
    # main('../lab4/Videos/Video.mp4', '00:00', '01:12', '../lab4/Videos', 30)

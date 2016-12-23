#!/usr/bin/python

from sys import argv
from pydub import AudioSegment

file_destination = ""
file_name = ""
file_extension = ""


def ringtone_maker(start, end):
    sound_file = AudioSegment.from_file(file_destination + "/" + file_name + "." + file_extension,
                                        format=file_extension)
    print "Name of ringtone : "
    ringtone_name = raw_input()

    start_s = [int(x) for x in start.split(':')]
    end_s = [int(x) for x in end.split(':')]

    length_start = len(start_s)
    length_end = len(end_s)

    start_t = 0
    end_t = 0
    total_time = len(sound_file)

    for i in range(0, length_start):
        start_t += start_s[i] * (pow(60, length_start - 1 - i))
    start_t *= 1000

    for i in range(0, length_end):
        end_t += end_s[i] * (pow(60, length_end - 1 - i))
    end_t *= 1000

    if end_t > total_time or start_t > total_time or start_t > end_t:
        print "End Time is out of range"
        time_slice()

    # print str(start_t)+" "+str(end_t)

    sliced_audio = sound_file[start_t:end_t]
    sliced_audio.export(file_destination + "/" + ringtone_name + "." + file_extension, format=file_extension,
                        bitrate="320k")
    print "Ringtone Exported"

    pass


def time_slice():
    print "Start the starting time and ending time (prefer min:sec) : "
    start_time = raw_input()
    end_time = raw_input()

    ringtone_maker(start_time, end_time)


if __name__ == "__main__":
    file_destination = argv[1]
    file_name = argv[2]
    file_extension = argv[3]

    print "received file information : \n"
    print file_destination + "/" + file_name + "." + file_extension

    time_slice()

import sys
import os
import datetime as dt

def main():
   file_name = ['20180507.log', '20180508.log', '20180509.log', '20180510.log',
                '20180605.log', '20180609.log', '20180612.log', '20180617.log']
   output_file = "performance_enhancements.txt"
   with open(output_file, 'w') as g:
       for file in file_name:
           g.write("file name: {0}\n".format(file))
           with open(file, 'r') as f:
                for line in f:
                    retrieved_line = line.split()
                    if retrieved_line[2].startswith("Retrieved"):
                        retrieved_time = retrieved_line[0][:8]
                        retrieved_time = dt.datetime.strptime(retrieved_time,'%H:%M:%S')
                        released_line = f.next().split()
                        released_time = released_line[0][:8]
                        released_time = dt.datetime.strptime(released_time,'%H:%M:%S')
                        if released_time < retrieved_time:
                            released_time += dt.timedelta(1)
                        diff = (released_time - retrieved_time)
                        g.write("time diff: {0}, retrieved time: {1}, released time: {2}\n"\
                                .format(diff, dt.datetime.strftime(retrieved_time,'%H:%M:%S'),\
                                   dt.datetime.strftime(released_time, '%H:%M:%S')))


if __name__ == '__main__':
    main()

from deeplab_demo import *
from PIL import Image
import numpy as np


def save_mark(file, row, clo_s, col_e):
    with open(file, mode='a') as file:
        file.write(str(row)+' '+str(clo_s)+' '+str(col_e)+'\n')


if __name__ == '__main__':
    frame_count = 1500
    for f in range(frame_count):
        print('Process '+str(f+1)+'/'+str(frame_count)+' started!')
        file_name = '/Users/lizhaoheng/Dropbox/Work/SRT2/VideoBlur/1/'+str(f)+'_original.jpg'
        resized_file_name = '/Users/lizhaoheng/Dropbox/Work/SRT2/VideoBlur/1/'+str(f)+'_resize.jpg'
        mark_file_name = '/Users/lizhaoheng/Dropbox/Work/SRT2/VideoBlur/1/'+str(f)+'_mark.txt'

        resized_im, seg_map = get_segmentation(file_name)
        resized_im.save(resized_file_name)

        [row, col] = seg_map.shape

        start = False
        row_mark = -1
        col_mark_start = -1
        col_mark_end = -1

        for i in range(row):
            row_mark = i
            for j in range(col):
                if not start and seg_map[i][j] == 15:
                    start = True
                    col_mark_start = j
                if start and not seg_map[i][j] == 15:
                    col_mark_end = j-1
                    save_mark(mark_file_name, row_mark, col_mark_start, col_mark_end)
                    start = False
                if start and j == col-1 and seg_map[i][j] == 15:  # for special case
                    col_mark_end = j
                    save_mark(mark_file_name, row_mark, col_mark_start, col_mark_end)
                    start = False

        print('Process ' + str(f+1) + ' ended!')

#!/usr/bin/env python
import numpy as np

# all dimensions in meters
w = 30.
h = 60.
blue_line_h = 7.14
face_off_neutral_zone_h = 1.5
face_off_w = 7.
face_off_end_zone_h = 10.
goal_crease_h = 4.
curvature_begin_h = 8.

# positive direction - x to right, y to top (see image for ice rink orientation)
ice_rink = np.array(
    [[0, h / 2. - goal_crease_h],  # crease center
     [-w / 2., h / 2. - curvature_begin_h],  # curvature beginning tl, tr
     [+w / 2., h / 2. - curvature_begin_h],
     [-face_off_w, h / 2. - face_off_end_zone_h],  # end zone face off tl, tr
     [+face_off_w, h / 2. - face_off_end_zone_h],
     [-w / 2., blue_line_h],  # blue line tl, tr
     [+w / 2., blue_line_h],
     [-face_off_w, blue_line_h - face_off_neutral_zone_h],  # face off neutral zone tl, tr, bl, br
     [+face_off_w, blue_line_h - face_off_neutral_zone_h],
     [0, 0],  # centre
     [-face_off_w, -blue_line_h + face_off_neutral_zone_h],
     [+face_off_w, -blue_line_h + face_off_neutral_zone_h],
     [-w / 2., -blue_line_h],  # blue line bl br
     [+w / 2., -blue_line_h],
     [-face_off_w, -h / 2. + face_off_end_zone_h],  # end zone face off bl, br
     [+face_off_w, -h / 2. + face_off_end_zone_h],
     [-w / 2., -h / 2. + curvature_begin_h],  # curvature beginning tl, tr
     [+w / 2., -h / 2. + curvature_begin_h],
     [0, -h / 2. + goal_crease_h]])  # crease center


if __name__ == '__main__':
    import cv2

    def visualize_points(image_filename, points, shift, ratio_px_m):
        cv2.namedWindow('out')
        img = cv2.imread(image_filename)
        flip_y = np.array([1, -1])  # flip y axis; in ice rink coodrdinates y goes positive upwards,
                                     # in image coordinates y goes positive downwards
        for i, point in enumerate(points):
            point_img = (point * flip_y * ratio_px_m + shift).astype(int)
            cv2.circle(img, tuple(point_img), 3, (200, 0, 0), -1)
            point_img[1] += 10
            cv2.putText(img, str(i), tuple(point_img), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 0, 0))

        cv2.imshow('out', img)
        cv2.waitKey(0)
        cv2.destroyWindow('out')

    # shift = np.array(img.shape[:2]) / 2.
    shift = np.array([397, 605])
    ratio_px_m = 218 / 14.
    visualize_points('ice_rink_iihf.png',
                     ice_rink, shift, ratio_px_m)

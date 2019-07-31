import cv2
import numpy as np
import cv2.aruco as aruco
import glob

class Tracker:

    @staticmethod
    def calculate_camera_values(path):
        criteria = (cv2.TermCriteria_EPS + cv2.TermCriteria_MAX_ITER, 30, 0.001)

        objp = np.zeros((6 * 7, 3), np.float32)
        objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)

        objpoints = []
        imgpoints = []
        images = glob.glob(path)

        for fname in images:
            img = cv2.imread(fname)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            ret, corners = cv2.findChessboardCorners(gray, (7, 6), None)

            if ret is True:
                objpoints.append(objp)

                corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
                imgpoints.append(corners2)

        return cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    @staticmethod
    def preprocess(img):
        gray_color = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
        params = aruco.DetectorParameters_create()

        return aruco.detectMarkers(gray_color, aruco_dict, parameters=params)

import cv2
import numpy as np 
import cv2.aruco as aruco
import glob

class Tracker:
    display_name = "Frame"
    is_showing_marker_coodrinate_system = False

    @staticmethod
    def calculate_camera_values(path):
        criteria = (cv2.TermCriteria_EPS + cv2.TermCriteria_MAX_ITER, 30, 0.001)

        objp = np.zeros((6 * 7, 3), np.float32)
        objp[:,:2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)

        objpoints = []
        imgpoints = []
        images = glob.glob(path)

        for fname in images:
            img = cv2.imread(fname)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            ret, corners = cv2.findChessboardCorners(gray, (7, 6), None)

            if ret == True:
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


    @staticmethod
    def process_configuration(img, mtx, dist, rvec, tvec):
        if Tracker.is_showing_marker_coodrinate_system:
            aruco.drawAxis(img, mtx, dist, rvec, tvec, 1)

    @staticmethod
    def clean_up(cap):
        cap.release()
        cv2.destroyAllWindows()

    @staticmethod
    def display(img):
        cv2.imshow(Tracker.display_name, img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            return False

        return True

    @staticmethod
    def track(path):
        def decorator(func):
            def wrapped_func(*args, **kwargs):
                cap = cv2.VideoCapture(0)
                ret, mtx, dist, rvecs, tvecs = Tracker.calculate_camera_values(path)

                is_running = True

                while(is_running):
                    ret, img = cap.read()
                    corners, ids, _ = Tracker.preprocess(img)

                    if np.all(ids != None):
                        rvecs, tvecs, _ = aruco.estimatePoseSingleMarkers(corners, 1, mtx, dist)

                        for rvec, tvec in zip(rvecs, tvecs):
                            axis = func(args[0])

                            Tracker.process_configuration(img, mtx, dist, rvec, tvec)

                    is_running = Tracker.display(img)
            return wrapped_func
        return decorator

class Input:
    def __init__(self, address="B8:AE:6E:F1:39:81"):
        self.address = address
       
    
    @Tracker.track('calib_images/*.jpg')
    def process(self):
        return None

if __name__ == "__main__":
    Tracker.is_showing_marker_coodrinate_system = True

    inp = Input()
    inp.process()
    pass
#!/usr/bin/env python3
# coding: utf-8
# code from M.Sc. Hahn Juergen University of Regensburg

from numpy import *
from pylab import *


class ProjectiveTransformation():

    def __init__(self):
        self.identity_to_destination = self.computeIdentityToDestination()

    def computeIdentityToSource(self, scoords):
        A = scoords[0]
        B = scoords[1]
        C = scoords[2]
        D = scoords[3]
        source_points_123 = matrix([[A[0], B[0], C[0]],
                                    [A[1], B[1], C[1]],
                                    [1, 1, 1]])

        source_point_4 = [[D[0]], [D[1]], [1]]

        scale_to_source = solve(source_points_123, source_point_4)

        l, m, t = [float(x) for x in scale_to_source]

        identity_to_source = matrix([[l * A[0], m * B[0], t * C[0]],
                                    [l * A[1], m * B[1], t * C[1]],
                                    [l, m, t]])

        return identity_to_source

    def computeIdentityToDestination(self):
        DESTINATION_SCREEN_WIDTH = 1280
        DESTINATION_SCREEN_HEIGHT = 720

        A2 = 0, DESTINATION_SCREEN_HEIGHT
        B2 = 0, 0
        C2 = DESTINATION_SCREEN_WIDTH, 0
        D2 = DESTINATION_SCREEN_WIDTH, DESTINATION_SCREEN_HEIGHT

        dcoords = [A2, B2, C2, D2]

        dest_points_123 = matrix([[A2[0], B2[0], C2[0]],
                                 [A2[1], B2[1], C2[1]],
                                 [1, 1, 1]])

        dest_point_4 = matrix([[D2[0]],
                               [D2[1]],
                               [1]])

        scale_to_dest = solve(dest_points_123, dest_point_4)
        l, m, t = [float(x) for x in scale_to_dest]

        identity_to_dest = matrix([[l * A2[0], m * B2[0], t * C2[0]],
                                  [l * A2[1], m * B2[1], t * C2[1]],
                                  [l, m, t]])

        return identity_to_dest

    def computeActualCoordinates(self, identity_to_dest, identity_to_source):
        source_to_identity = inv(identity_to_source)

        source_to_dest = identity_to_dest @ source_to_identity

        x, y, z = [float(w) for w in (source_to_dest @ matrix([[512],
                                                              [384],
                                                              [1]]))]
        x = x / z
        y = y / z

        return (x, y)

    def getActualCoordinates(self, input):
        identity_to_source = self.computeIdentityToSource(input)
        return self.computeActualCoordinates(self.identity_to_destination, identity_to_source)

    def getLightPositions(self, state):
        # bubblesort from: https://www.geeksforgeeks.org/python-program-for-bubble-sort/
        n = len(state)
        for i in range(n):
            for j in range(0, n-i-1):
                if state[j]['x'] > state[j+1]['x']:
                    state[j], state[j+1] = state[j+1], state[j]

        # start points from top left corner counter-clockwise
        if state[0]['y'] < state[1]['y']:
            state[0], state[1] = state[1], state[0]

        if state[2]['y'] > state[3]['y']:
            state[2], state[3] = state[3], state[2]

        A = (state[0]['x'], state[0]['y'])
        B = (state[1]['x'], state[1]['y'])
        C = (state[2]['x'], state[2]['y'])
        D = (state[3]['x'], state[3]['y'])

        scoords = [A, B, C, D]
        return scoords

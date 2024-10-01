#/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg._nav_sat_fix import NavSatFix
from math import sin,cos,radians,atan2,atan,degrees,sqrt
from interfaces.msg import Completed

RADIUS = 6365.766
DISH_LAT = 51.42287924341543
DISH_LON = -112.64106837507106

class GpsDistance(Node):

    def __init__(self):
        super().__init__("gps_distance")
        self.pos_subscriber_ = self.create_subscription(NavSatFix, "/GCS", self.pos_callback, 10)
        self.dish_publisher = self.create_publisher(Completed, "/Dish", 10)

    def pos_callback(self, msg: NavSatFix):
        lat1 = radians(msg.latitude)
        lon1 = radians(msg.longitude)
        lat2 = radians(DISH_LAT)
        lon2 = radians(DISH_LON)
        delta_lat = lat2 - lat1
        delta_lon = lon2 - lon1

        heading = get_heading(lat1, lon1, lat2, lon2, delta_lat, delta_lon)
        distance = get_distance(lat1, lon1, lat2, lon2, delta_lat, delta_lon)

        returnMsg = Completed()
        returnMsg.latitude = msg.latitude
        returnMsg.longitude = msg.longitude
        returnMsg.distance = round(distance, 1)
        returnMsg.heading = round(heading, 1)

        self.dish_publisher.publish(returnMsg)

def get_distance(lat1, lon1, lat2, lon2, delta_lat, delta_lon):
    randicand = (sin(delta_lat/2)**2) + cos(lat1)*cos(lat2)*(sin(delta_lon/2)**2)
    return 2*RADIUS*atan2(sqrt(randicand),sqrt(1-randicand))*1000

def get_heading(lat1, lon1, lat2, lon2, delta_lat, delta_lon):
    y = sin(delta_lon) * cos(lat2)
    x = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(delta_lon)
    bearing = atan2(y, x)
    bearing = degrees(bearing)
    bearing = (bearing + 360) % 360
    heading = round(bearing, 1)
    return heading

def main(args=None):
    rclpy.init(args=args)
    node = GpsDistance()
    rclpy.spin(node)
    rclpy.shutdown()
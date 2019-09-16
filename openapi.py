#！ /usr/bin/env python3
import requests
import json

SVR_PREFIX = "https://ac.aimall-tech.com/openapi"
APP_CODE = "your app code"

HEADER = {
    "Authorization":"APPCODE "+APP_CODE
}

#项目列表
def list_projects():
    resp = requests.get(SVR_PREFIX  + "/projects"  ,headers=HEADER)
    print(resp.text)

#新建项目
def create_project():
    resp = requests.post(SVR_PREFIX + "/projects", data = {"name":"new project"}, headers=HEADER)
    print(resp.text)

#更新项目
def update_project():
    resp = requests.put(SVR_PREFIX + "/projects/60", data = {"name":"new project","remark":"remark"}, headers=HEADER)
    print(resp.text)

#删除项目
def delete_project():
    resp = requests.delete(SVR_PREFIX + "/projects/60",headers=HEADER)
    print(resp.text)

#常驻访问记录数量
def count_permanent_records():
    resp = requests.get(SVR_PREFIX + "/permanent/records.count", headers = HEADER)
    print(resp.text)

#常驻访问列表
def list_permanent_records():
    resp = requests.get(SVR_PREFIX + "/permanent/records?page_offset=0&&page_size=10", headers = HEADER)
    print(resp.text)

#访客访问记录数量
def count_visitor_records():
    resp = requests.get(SVR_PREFIX + "/visitor/records.count", headers = HEADER)
    print(resp.text)

#访客访问列表
def list_visitor_records():
    resp = requests.get(SVR_PREFIX + "/visitor/records?page_offset=0&&page_size=10", headers = HEADER)
    print(resp.text)

#黑名单访问记录数量
def count_blacklist_records():
    resp = requests.get(SVR_PREFIX + "/blacklist/records.count", headers = HEADER)
    print(resp.text)

#黑名单访问列表
def list_blacklist_records():
    resp = requests.get(SVR_PREFIX + "/blacklist/records?page_offset=0&&page_size=10", headers = HEADER)
    print(resp.text)

#项目空间列表
def list_project_locations():
    resp = requests.get(SVR_PREFIX + "/locations?project_id=59", headers= HEADER)
    print(resp.text)

#新建项目空间
def create_project_location():
    resp = requests.post(SVR_PREFIX + "/locations", data = {"project_id":59,"name":"new location","parent_token":"115"},headers=HEADER)
    print(resp.text)

#删除项目空间
def delete_project_location():
    resp = requests.delete(SVR_PREFIX + "/locations/117", headers=HEADER)
    print(resp.text)

#设备数量
def count_devices():
    resp = requests.get(SVR_PREFIX + "/devices.count", headers=HEADER)
    print(resp.text)

#设备列表
def list_devices():
    resp = requests.get(SVR_PREFIX + "/devices?page_offset=0&&page_size=10", headers = HEADER)
    print(resp.text)

#批量修改设备位置
def modify_devices_location():
    resp = requests.put(SVR_PREFIX + "/devices.location", data = {"location_token":"115"},headers=HEADER)
    print(resp.text)

#修改设备工作模式
def switch_work_mode():
    resp = requests.put(SVR_PREFIX + "/devices/TEST190603000001/mode",data = {"mode":0},headers = HEADER)
    print(resp.text)

#脉冲开门
def trigger_opne():
    resp = requests.post(SVR_PREFIX + "/devices/TEST190603000001/trigger_open", headers = HEADER)
    print(resp.text)

#常驻人脸数量
def count_permanent_faces():
    resp = requests.get(SVR_PREFIX + "/permanent/faces.count", headers=HEADER)
    print(resp.text)

#常驻人脸列表
def list_permanent_faces():
    resp = requests.get(SVR_PREFIX + "/permanent/faces?page_offset=0&&page_size=10", headers = HEADER)
    print(resp.text)

#创建常驻人脸
def add_permanent_face():
    data = {
        "name":"new face",
    }
    files = {
         "image":open("./Downloads/webwxgetmsgimg.jpeg","rb"),
    }
    resp = requests.post(SVR_PREFIX + "/permanent/faces", files = files, data = data, headers=HEADER)
    print(resp.text)

#更新常驻人脸
def update_permanent_face():
    resp = requests.patch(SVR_PREFIX + "/permanent/faces/7", data = {"name":"update new name","remark":"remark"},headers=HEADER)
    print(resp.text)

#批量修改常驻人脸位置
def swtich_permanent_faces_location():
    resp = requests.put(SVR_PREFIX + "/permanent/faces.location", data = {"location_tokens":"114,115"}, headers = HEADER)
    print(resp.text)

#批量删除常驻人脸
def delete_permanent_faces():
    resp = requests.delete(SVR_PREFIX + "/permanent/faces?face_tokens=6",headers = HEADER)
    print(resp.text)

#访客人脸列表
def list_visitor_faces():
    resp = requests.get(SVR_PREFIX + "/visitor/faces?page_offset=0&&page_size=10", headers = HEADER)
    print(resp.text)

#创建访客人脸
def add_visitor_face():
    data = {
        "name":"new face",
        "expired_at":1575129600,
    }
    files = {
         "image":open("./Downloads/webwxgetmsgimg.jpeg","rb"),
    }
    resp = requests.post(SVR_PREFIX + "/visitor/faces", files = files, data = data, headers=HEADER)
    print(resp.text)

#更新访客人脸
def update_visitor_face():
    resp = requests.patch(SVR_PREFIX + "/visitor/faces/7", data = {"name":"update new name","remark":"remark"},headers=HEADER)
    print(resp.text)

#批量修改访客人脸位置
def swtich_visitor_faces_location():
    resp = requests.put(SVR_PREFIX + "/visitor/faces.location", data = {"location_tokens":"114,115"}, headers = HEADER)
    print(resp.text)

#批量删除访客人脸
def delete_visitor_faces():
    resp = requests.delete(SVR_PREFIX + "/visitor/faces?face_tokens=2,3",headers = HEADER)
    print(resp.text)

#黑名单人脸列表
def list_blacklist_faces():
    resp = requests.get(SVR_PREFIX + "/blacklist/faces?page_offset=0&&page_size=10", headers = HEADER)
    print(resp.text)

#创建黑名单人脸
def add_blacklist_face():
    data = {
        "name":"new face",
    }
    files = {
         "image":open("./Downloads/webwxgetmsgimg.jpeg","rb"),
    }
    resp = requests.post(SVR_PREFIX + "/blacklist/faces", files = files, data = data, headers=HEADER)
    print(resp.text)

#更新黑名单人脸
def update_blacklist_face():
    resp = requests.patch(SVR_PREFIX + "/blacklist/faces/2", data = {"name":"update new name","remark":"remark"},headers=HEADER)
    print(resp.text)

#批量修改黑名单人脸位置
def switch_blacklist_faces_location():
    resp = requests.put(SVR_PREFIX + "/blacklist/faces.location", data = {"location_tokens":"114,115"}, headers = HEADER)
    print(resp.text)

#批量删除黑名单人脸
def delete_blacklist_faces():
    resp = requests.delete(SVR_PREFIX + "/blacklist/faces?face_tokens=2,5",headers = HEADER)
    print(resp.text)

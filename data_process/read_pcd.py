import pyntcloud

# Load PCD file
cloud = pyntcloud.PyntCloud.from_file("/home/liuyang/uuv_ws/bag_files/pcd/36.889000000.pcd")

# Print basic information about the point cloud
print(cloud)
# This package requires open3d; use this command to install it: pip install open3d
import open3d as o3d

# This line calls read_point_cloud() to get the data from the exemplary.py file (for a separate project) and stores it in the pcd variable.
pcd = o3d.t.io.read_point_cloud("exemplary.ply")
# This will print the summary of the point cloud
print(pcd)

# OUTPUT:
# If you don't have open3d installed, this is the exact output of this script:
# PointCloud on CPU:0 [86357 points (Float64)].
# Attributes: colors (dtype = UInt8, shape = {86357, 3}).
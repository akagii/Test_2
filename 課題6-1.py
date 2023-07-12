import json

json_file = open('kabeposter/kabeposter_000000000000_keypoints.json', "r")

load = json.load(json_file)

pose_a = load["people"][0]["pose_keypoints_2d"]
pose_b = load["people"][1]["pose_keypoints_2d"]

print(pose_a[0], pose_a[1], pose_a[2], pose_a[3], pose_a[4], pose_a[5])
print(pose_b[0], pose_b[1], pose_b[2], pose_b[3], pose_b[4], pose_b[5])
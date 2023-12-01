human parsing:
input: ảnh người
chia ảnh thành các bộ phận như chân, tay, đầu, thân,.. dùng để loại bỏ phần quần áo khi chạy mô hình pre-trained, bố trí hợp lí quần áo khi chạy VITON, 
output: file .png ảnh hình người đã được chia thành các bộ phận theo màu (Segmentation map)

pose estimation:
input: ảnh người
sử dụng hệ thống openpose để detect ra khung dáng người mẫu
output:
- file .png khung dáng người, với các đoạn là từng bộ phận của khung xương(Pose map)
- file .json lưu vị trí từng phần, bộ phận, định vị gần đúng các bộ phận
hai file này dùng để ép lại dáng của quần áo, lưu thông tin vị trí từng bộ phận của người mẫu
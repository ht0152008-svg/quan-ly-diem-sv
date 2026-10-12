import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Tiêu đề ứng dụng
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# 1. Bảng dữ liệu ban đầu
data = {
    'Họ và tên': [
        'Nguyễn Văn An', 'Trần Thị Bình', 'Lê Hoàng Cường',
        'Phạm Thị Dung', 'Hoàng Văn Em', 'Ngô Thị Phương',
        'Bùi Văn Giang', 'Đỗ Thị Hoa', 'Vũ Minh Khang', 'Phan Thị Linh'
    ],
    'Điểm chuyên cần': [9.0, 10.0, 5.0, 9.5, 6.0, 10.0, 8.5, 9.0, 4.0, 10.0],
    'Điểm giữa kỳ': [7.5, 8.0, 4.0, 9.0, 3.5, 8.5, 7.0, 8.0, 3.0, 9.5],
    'Điểm cuối kỳ': [8.0, 8.5, 3.5, 9.2, 4.0, 9.0, 7.5, 8.2, 2.5, 9.8]
}

df = pd.DataFrame(data)
st.subheader("Bảng dữ liệu ban đầu")
st.dataframe(df)

# 2. Tính điểm tổng kết và Xếp loại sinh viên
df['Tong_ket'] = (df['Điểm chuyên cần'] * 0.2) + (df['Điểm giữa kỳ'] * 0.3) + (df['Điểm cuối kỳ'] * 0.5)
df['Tong_ket'] = df['Tong_ket'].round(2)

def xep_loai(diem):
    if diem >= 8.5:
        return 'Giỏi'
    elif diem >= 7.0:
        return 'Khá'
    elif diem >= 5.0:
        return 'Trung bình'
    else:
        return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

st.subheader("Bảng tổng kết và xếp loại")
st.dataframe(df)

# 3. Thống kê cơ bản
dtb_lop = df['Tong_ket'].mean()
sv_max = df.loc[df['Tong_ket'].idxmax()]
sv_min = df.loc[df['Tong_ket'].idxmin()]
so_sv_dat = (df['Tong_ket'] >= 5.0).sum()

st.subheader("THỐNG KÊ CƠ BẢN")
st.write(f"- Điểm tổng kết trung bình của lớp: **{dtb_lop:.2f}**")
st.write(f"- Sinh viên cao điểm nhất: **{sv_max['Họ và tên']}** ({sv_max['Tong_ket']:.2f})")
st.write(f"- Sinh viên thấp điểm nhất: **{sv_min['Họ và tên']}** ({sv_min['Tong_ket']:.2f})")
st.write(f"- Số sinh viên đạt (>= 5.0 điểm): **{so_sv_dat}** sinh viên")

# Thêm hộp chọn tra cứu sinh viên theo yêu cầu đề bài
st.subheader("Tra cứu thông tin sinh viên")
ten_chon = st.selectbox("Chọn sinh viên:", df['Họ and tên'] if 'Họ and tên' in df else df['Họ và tên'])
sv_chon = df[df['Họ và tên'] == ten_chon].iloc[0]
st.write(f"Điểm tổng kết của **{ten_chon}**: `{sv_chon['Tong_ket']}` - Xếp loại: **{sv_chon['Xep_loai']}**")

# 4. Biểu đồ cột
st.subheader("BIỂU ĐỒ ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN")
fig, ax = plt.subplots(figsize=(10, 5))
ax.barh(df['Họ và tên'], df['Tong_ket'], color='skyblue')
ax.set_xlabel('Điểm Tổng Kết')
ax.set_ylabel('Họ và tên sinh viên')
plt.tight_layout()
st.pyplot(fig)

# 5. Tên người tạo ở cuối trang
st.markdown("---")
st.caption("Ứng dụng được tạo bởi: [Hồ Thanh Trung] - MSSV: [051208008834]")
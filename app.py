import streamlit as st

st.set_page_config(
    page_title="Tính lãi gửi tiết kiệm - Trần Nguyễn Anh Thư",
    page_icon="💰",
    layout="centered"
)

st.title("💰 TÍNH LÃI GỬI TIẾT KIỆM")
st.subheader("Trần Nguyễn Anh Thư")

st.write("Nhập thông tin khoản tiền gửi:")

# Nhập dữ liệu
so_tien_gui = st.number_input(
    "Số tiền gửi (VNĐ)",
    min_value=0.0,
    value=100000000.0,
    step=1000000.0,
    format="%.0f"
)

ky_han = st.number_input(
    "Kỳ hạn (tháng)",
    min_value=1,
    max_value=120,
    value=12,
    step=1
)

lai_suat = st.number_input(
    "Lãi suất (%/năm)",
    min_value=0.0,
    max_value=100.0,
    value=6.0,
    step=0.01,
    format="%.2f"
)

hinh_thuc = st.selectbox(
    "Hình thức nhận lãi",
    ["Cuối kỳ", "Hàng tháng", "Hàng quý"]
)


# Hàm định dạng tiền
def format_money(value):
    return f"{value:,.0f}".replace(",", ".") + " VNĐ"


# Nút tính lãi
if st.button("🧮 TÍNH LÃI", use_container_width=True):

    if so_tien_gui <= 0:
        st.error("Số tiền gửi phải lớn hơn 0.")
        st.stop()

    if lai_suat < 0:
        st.error("Lãi suất không được nhỏ hơn 0.")
        st.stop()

    # Đổi lãi suất % sang số thập phân
    lai_suat_nam = lai_suat / 100

    # Tính tổng tiền lãi
    tong_tien_lai = (
        so_tien_gui
        * lai_suat_nam
        * ky_han
        / 12
    )

    # Tính tiền lãi định kỳ
    if hinh_thuc == "Cuối kỳ":
        tien_lai_dinh_ky = tong_tien_lai
       

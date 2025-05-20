import streamlit as st
import time 
from utils.db import get_all_volunteers, get_volunteer_by_id

def search_volunteer_page():
    st.title("ค้นหาอาสาสมัคร")

    volunteers = get_all_volunteers()
    if not volunteers:
        st.warning("ไม่พบข้อมูลอาสาสมัครในระบบ")
        return

    options = [f"{v['volunteer_id']} - {v['first_name']} {v['last_name']}" for v in volunteers]
    selected = st.selectbox("ระบุเลขประจำตัวหรือชื่อของอาสาสมัคร", options)

    if st.button("ค้นหา"):
        volunteer_id = int(selected.split(" - ")[0])
        volunteer = get_volunteer_by_id(volunteer_id)

        if volunteer:
            st.success("เข้าสู่หน้ากรอกข้อมูล ...")
            st.session_state.selected_volunteer = volunteer
            st.session_state.page = "กรอกข้อมูล"
            time.sleep(0.3)
            st.rerun()
        else:
            st.error("❌ ไม่พบข้อมูลอาสาสมัครในระบบ")
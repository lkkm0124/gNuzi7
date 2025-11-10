import streamlit as st

st.title("BMI 계산기")

# 사용자 입력
weight = st.number_input("몸무게(kg)를 입력하세요:", min_value=0.0, max_value=1000.0, value=0.0)
height = st.number_input("키(cm)를 입력하세요:", min_value=0.0, max_value=1000.0, value=0.0)

if st.button("BMI 계산"):
    height_m = height / 100  # cm -> m 변환
    bmi = weight / (height_m ** 2)
    bmi = round(bmi, 2)
    
    # BMI 상태 판정
    if bmi < 18.5:
        status = "저체중입니다.dyyuuuiuuerre35433343433"
    elif 18.5 <= bmi < 24.9:
        status = "정상입니다"
    elif 25 <= bmi < 29.9:
        status = "과체중입니다."
    else:
        status = "비만입니다."

    st.write(f"당신의 BMI는 **{bmi}** 입니다.")
    st.write(f"체중 상태: **{status}**")

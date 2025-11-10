import streamlit as st

st.title("☆BMI 계산기☆")


weight = st.number_input("몸무게(kg)를 입력하세요:", min_value=0.0, max_value=1000.0, value=0.0)
height = st.number_input("키(cm)를 입력하세요:", min_value=0.0, max_value=1000.0, value=0.0)

if st.button("BMI 계산"):
    height_m = height / 100  # cm -> m 변환
    bmi = weight / (height_m ** 2)
    bmi = round(bmi, 2)
    
    # BMI 상태 판정
    if bmi < 18.5:
        status = "저체중"
        advice = "영양 섭취를 늘리고 근력 운동을 병행하세요."
    elif 18.5 <= bmi < 24.9:
        status = "정상"
        advice = "현재 상태를 유지하세요! 규칙적인 운동과 균형 잡힌 식사 추천."
    elif 25 <= bmi < 29.9:
        status = "과체중"
        advice = "규칙적인 운동과 식사 조절로 건강한 체중을 유지하세요."
    else:
        status = "비만"
        advice = "전문의 상담과 식이요법, 운동 병행이 필요합니다."

    st.write(f"당신의 BMI는 **{bmi}** 입니다.")
    st.write(f"체중 상태: **{status}**")
    st.write(f"💡 권장 조치: {advice}")

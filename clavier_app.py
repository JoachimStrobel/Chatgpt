import streamlit as st
st.set_page_config(initial_sidebar_state="expanded")
def calculate_rt(cec, m, m_star, rw, rho_clay):
    BQv = cec * rho_clay
    F = BQv / (1 + BQv)
    F_star = F * (1 + BQv)**(m_star - m)
    rt = F_star * rw
    return rt

st.title("Clavier Dual-Water Rt Calculator (Sw = 1)")

st.sidebar.header("Input Parameters")
cec = st.sidebar.slider("CEC (meq/g)", min_value=0.001, max_value=0.1, value=0.03, step=0.001)
m = st.sidebar.slider("m (cementation exponent)", min_value=1.5, max_value=3.0, value=2.0, step=0.05)
m_star = st.sidebar.slider("m* (adjusted exponent)", min_value=1.5, max_value=3.5, value=2.2, step=0.05)
rw = st.sidebar.slider("Rw (ohm·m)", min_value=0.01, max_value=0.5, value=0.05, step=0.01)
rho_clay = st.sidebar.slider("Clay grain density (g/cm³)", min_value=2.4, max_value=3.0, value=2.7, step=0.01)

rt = calculate_rt(cec, m, m_star, rw, rho_clay)

st.markdown(f"### Calculated Rt for Sw = 1: **{rt:.3f} ohm·m**")
st.caption("Model: F* = F × (1 + BQv)^(m* - m)")

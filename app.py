import streamlit as st

st.set_page_config(page_title='Skylink - Mayday Daily Jobs', page_icon="SkylinkLogo.png")
# Hide the Streamlit menu
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    
    </style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

def calculate_price(mileage, rate):

    if mileage <= 50:
        return mileage * 2
    else:
        additional_miles = mileage - 50
        return ((50 * 2) + (additional_miles * 1.70)) * rate
    

def main():
    col1, col2 = st.columns([2, 0.5])
    with col1:
        st.title('Skylink Price Calculator')
    with col2:
        st.image("SkylinkLogo.png")
    

    mileage = st.number_input('Enter the mileage of the vehicle (in miles):', min_value=1, value=1)

    saloon_base_rate = 1
    seater6_base_rate = 1.15
    seater8_base_rate = 1.25

    if st.button('Calculate Prices'):
        saloon_price = calculate_price(mileage, saloon_base_rate)
        seater6_price = calculate_price(mileage, seater6_base_rate)
        seater8_price = calculate_price(mileage, seater8_base_rate)

        st.markdown("""
        #### Prices (£) :
        <span style='font-size: 18px;'>**🚘 Saloon:**      £{:,.2f}</span>  
                    
        <span style='font-size: 18px;'>**🚐 6-Seater:**       £{:,.2f}</span>  
                    
        <span style='font-size: 18px;'>**🚌 8-Seater:**        £{:,.2f}</span>  
        """.format(saloon_price, seater6_price, seater8_price), unsafe_allow_html=True)


if __name__ == '__main__':
    main()

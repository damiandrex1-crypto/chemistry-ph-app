# creating a chemistry ph app
import streamlit as st
st.set_page_config(page_title='Chemistry Toolkit', layout="centered")
st.title('Chemistry toolkit')
st.write('A simple tool for pH, pOH, and Molarity calculations.')
st. divider()
# pH SECTION
st.header('pH Analyzer')
pH = st.number_input('Enter pH value (0-14):', min_value=0.0, max_value=14.0)
if st.button ('Analyze pH'):
    col1, col2 =st. columns(2)
    with col1:
        if pH < 7:
            st.error('ACID')
        elif pH ==7:
            st.info('NEUTRAL')
        else:
            st.success('BASE')
            with col2:
                pOH =14- pH
                st.metric('pOH',pOH)
                st. subheader('Likely substance')
                if pH <=1:
                    st.write('Hydrochloric Acid(HCL)')
                elif pH >=13:
                    st.write('Sodium Hydroxide(NaOH)')
                else:
                    st.write('weak or neutral solution')
                    st. divider()
                    # MOLARITY SECTION
                    st. header('Molarity calculator')
                    col3, col4 =st.columns(2)
                    with col3:
                        moles=st.number_input('Moles of solution',min_value=0.0, key='moles')
                        with col4:
                            volume=st.number_input('Volume(L)', min_value=0.0, key='volume')
                            if volume > 0:
                                molarity =moles/volume
                                st.success(f'Molarity={molarity} M')





import pandas as pd
import streamlit as st
import calculation

# Set-up
st.set_page_config(page_title='Calculator')
st.header('RAFT Polymerization Homopolymer Synthesis Calculator')
st.subheader('Input Values')

# Inputs
# input1 = st.number_input('Molar Mass of Monomer (g/mol)')
# input2 = st.number_input('Molar Mass of CTA (g/mol)')
# input3 = st.number_input('Molar Mass of Initiator (g/mol)')
# input4 = st.number_input('Initiator Ratio (to CTA)')
# input5 = st.number_input('Length of Polymer (# units)')
# input6 = st.number_input('Desired total mass of polymer (g)')
# input7 = st.number_input('Expected Conversion (%)')

# Gathering Input
col1, col2, col3 = st.columns(3)

with col1:
    input1 = st.number_input('Molar Mass of Monomer (g/mol)', min_value=0.001)
    input2 = st.number_input('Molar Mass of CTA (g/mol)', min_value=0.001)
    input3 = st.number_input('Molar Mass of Initiator (g/mol)', min_value=0.001)

with col2:
    input5 = st.number_input('Desired Length of Polymer (# of units)', min_value=0.001)
    input6 = st.number_input('Desired total mass of polymer (g)', min_value=0.001)

with col3:
    input4 = st.number_input('Initiator Ratio (to CTA)', min_value=0.001)
    input7 = st.number_input('Expected Conversion (%)', min_value=0.001)

# Empty sub-header for spacing reasons
st.subheader("")

# Button to kickstart calculation process
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

with col3:
    ispressed = st.button('Calculate')

st.subheader('Results')

# Display Results
if ispressed:
    # Calculate using Excel Sheet
    results, result = calculation.calculation(input1, input2, input3, input4, input5, input6,
                                              input7)

    df = pd.DataFrame.from_dict(results)
    df.index = ['(g)', '(mg)']
    print(df)
    df2 = pd.DataFrame(result, index=['g/mol'])

    st.table(df)
    st.table(df2)

else:
    st.write('Press Calculate to see results')

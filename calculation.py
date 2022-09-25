# Reference:
# input1 = st.number_input('Molar Mass of Monomer (g/mol)')
# input2 = st.number_input('Molar Mass of CTA (g/mol)')
# input3 = st.number_input('Molar Mass of Initiator (g/mol)')
# input4 = st.number_input('Initiator Ratio (to CTA)')
# input5 = st.number_input('Length of Polymer (# units)')
# input6 = st.number_input('Desired total mass of polymer (g)')
# input7 = st.number_input('Expected Conversion (%)')

def calculation(input1, input2, input3, input4, input5, input6, input7):
    molar_mass_of_polymer = input5 * input1
    molar_ratio_monomer = input5
    molar_ratio_cta = input5 / input5
    mass_monomer_one_mol_polymer = molar_ratio_monomer * input1
    mass_cta_one_mol_polymer = molar_ratio_cta * input2
    actual_mol_polymer = input6 / molar_mass_of_polymer
    actual_mol_monomer_mol = actual_mol_polymer * input5
    conversion_decimal = input7 / 100
    conversion_inverse = 1 / conversion_decimal
    mol_monomer_conversion_accounted_mol = actual_mol_monomer_mol * conversion_inverse

    actual_mol_cta_mol = actual_mol_monomer_mol / molar_ratio_monomer
    moles_of_initiator = molar_ratio_cta * input4
    actual_mol_initiator_mol = actual_mol_cta_mol * moles_of_initiator

    # Calculations:
    actual_mass_of_monomer_g = input1 * mol_monomer_conversion_accounted_mol
    actual_mass_of_monomer_mg = actual_mass_of_monomer_g * 1000

    actual_mass_of_cta_g = input2 * actual_mol_cta_mol
    actual_mass_of_cta_mg = actual_mass_of_cta_g * 1000

    actual_mass_of_initiator_g = input3 * actual_mol_initiator_mol
    actual_mass_of_initiator_mg = actual_mass_of_initiator_g * 1000

    # Selecting data from
    # a single cell
    results = {'Actual Mass of Monomer': [actual_mass_of_monomer_g, actual_mass_of_monomer_mg],
               'Actual Mass of CTA': [actual_mass_of_cta_g, actual_mass_of_cta_mg],
               'Actual Mass of Initiator': [actual_mass_of_initiator_g,
                                            actual_mass_of_initiator_mg]}
    result = {'Molar Mass of Polymer (g/mol)': molar_mass_of_polymer}
    return (results, result)

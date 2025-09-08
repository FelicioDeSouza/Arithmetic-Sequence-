import streamlit as st

def generate_arithmetic_sequence(first_term, common_difference, num_terms):
    """
    Generate an arithmetic sequence given the first term, common difference, and number of terms.
    
    Args:
        first_term (float): The first term of the sequence
        common_difference (float): The common difference between consecutive terms
        num_terms (int): The number of terms to generate
    
    Returns:
        list: A list containing the arithmetic sequence
    """
    sequence = []
    for i in range(num_terms):
        term = first_term + (i * common_difference)
        sequence.append(term)
    return sequence

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Arithmetic Sequence Generator",
        page_icon="🔢",
        layout="centered"
    )
    
    # Main title
    st.title("🔢 Arithmetic Sequence Generator")
    st.markdown("Generate arithmetic sequences by specifying the first term, common difference, and number of terms.")
    
    # Create input section
    st.header("Input Parameters")
    
    # Create three columns for better layout
    col1, col2, col3 = st.columns(3)
    
    with col1:
        first_term = st.number_input(
            "First Term (a₁)",
            value=1.0,
            step=1.0,
            help="The first term of the arithmetic sequence"
        )
    
    with col2:
        common_difference = st.number_input(
            "Common Difference (d)",
            value=1.0,
            step=1.0,
            help="The constant difference between consecutive terms"
        )
    
    with col3:
        num_terms = st.number_input(
            "Number of Terms (n)",
            min_value=1,
            max_value=1000,
            value=10,
            step=1,
            help="How many terms to generate (maximum 1000)"
        )
    
    # Input validation and error handling
    if num_terms <= 0:
        st.error("❌ Number of terms must be a positive integer!")
        return
    
    if num_terms > 1000:
        st.error("❌ Number of terms cannot exceed 1000!")
        return
    
    # Generate sequence button (optional - sequence updates automatically)
    st.header("Generated Sequence")
    
    try:
        # Generate the arithmetic sequence
        sequence = generate_arithmetic_sequence(first_term, common_difference, num_terms)
        
        # Display sequence information
        st.success(f"✅ Successfully generated {num_terms} terms!")
        
        # Show sequence formula
        st.markdown("### Formula")
        st.latex(f"a_n = {first_term} + (n-1) \\times {common_difference}")
        
        # Display the sequence in a nice format
        st.markdown("### Sequence Terms")
        
        # For better display, show terms in rows of 10
        terms_per_row = 10
        
        for i in range(0, len(sequence), terms_per_row):
            row_terms = sequence[i:i + terms_per_row]
            
            # Create columns for each term in the row
            cols = st.columns(len(row_terms))
            
            for j, term in enumerate(row_terms):
                with cols[j]:
                    # Format the term nicely
                    if term == int(term):
                        term_str = str(int(term))
                    else:
                        term_str = f"{term:.2f}"
                    
                    st.metric(
                        label=f"a₍₍{i + j + 1}₎₎",
                        value=term_str
                    )
        
        # Show sequence as a list for easy copying
        st.markdown("### Complete Sequence")
        sequence_str = ", ".join([str(int(term)) if term == int(term) else f"{term:.2f}" for term in sequence])
        st.code(f"[{sequence_str}]", language="python")
        
        # Additional information
        st.markdown("### Sequence Information")
        info_col1, info_col2, info_col3 = st.columns(3)
        
        with info_col1:
            st.metric("First Term", first_term)
        
        with info_col2:
            st.metric("Last Term", sequence[-1])
        
        with info_col3:
            sequence_sum = sum(sequence)
            st.metric("Sum of Terms", f"{sequence_sum:.2f}" if sequence_sum != int(sequence_sum) else int(sequence_sum))
        
        # Sum formula
        st.markdown("### Sum Formula")
        st.latex(f"S_n = \\frac{{n}}{{2}} \\times (2a_1 + (n-1)d) = \\frac{{{num_terms}}}{{2}} \\times (2 \\times {first_term} + ({num_terms}-1) \\times {common_difference})")
        
    except Exception as e:
        st.error(f"❌ An error occurred while generating the sequence: {str(e)}")
    
    # Footer with additional information
    st.markdown("---")
    st.markdown("""
    **About Arithmetic Sequences:**
    - An arithmetic sequence is a sequence where the difference between consecutive terms is constant
    - General term formula: aₙ = a₁ + (n-1)d
    - Sum formula: Sₙ = n/2 × (2a₁ + (n-1)d)
    
    **Tips:**
    - Use positive common difference for increasing sequences
    - Use negative common difference for decreasing sequences
    - Use decimal values for non-integer sequences
    """)

if __name__ == "__main__":
    main()

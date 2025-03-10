import re
import streamlit as st

class FARBARContractBotWeb:
    def __init__(self):
        self.contract_data = {}
        self.steps = [
            ("property_address", "Enter the full property address:"),
            ("legal_description", "Enter the legal description of the property:"),
            ("buyer_name", "Enter the Buyer's full name(s):"),
            ("seller_name", "Enter the Seller's full name(s):"),
            ("buyer_address", "Enter the Buyer's address:"),
            ("seller_address", "Enter the Seller's address:"),
            ("purchase_price", "Enter the purchase price:"),
            ("initial_earnest_money", "Enter the initial deposit amount:"),
            ("additional_deposit", "Enter the additional deposit amount (if any):"),
            ("deposit_due_date", "Enter the due date for additional deposit (YYYY-MM-DD):"),
            ("financing_option", "Is the purchase cash or financed? (Enter 'cash' or 'financed'):"),
            ("loan_amount", "Enter the loan amount:"),
            ("loan_type", "Enter the type of loan (Conventional, FHA, VA, etc.):"),
            ("financing_contingency_days", "Enter the number of days for financing contingency:"),
            ("inspection_period_days", "Enter the number of days for the inspection period:"),
            ("who_pays_inspection", "Who is responsible for paying for inspections? (Buyer/Seller):"),
            ("closing_date", "Enter the agreed-upon closing date (YYYY-MM-DD):"),
            ("closing_agent", "Enter the name of the closing agent/title company:"),
            ("closing_agent_address", "Enter the closing agent's address:"),
            ("personal_property_included", "List any personal property included in the sale (appliances, fixtures, etc.):"),
            ("hoa_disclosure", "Is the property part of an HOA? (Yes/No):"),
            ("special_terms", "Enter any special terms or contingencies (or type 'None'):")
        ]
        self.current_step = 0
    
    def start(self):
        st.title("FARBAR Contract Assistant")
        st.write("Welcome! This tool will guide you through filling out the FARBAR Residential Contract for Sale and Purchase.")
        
        if "contract_data" not in st.session_state:
            st.session_state.contract_data = {}
            st.session_state.current_step = 0
        
        self.display_step()
    
    def display_step(self):
        step_key, step_prompt = self.steps[st.session_state.current_step]
        response = st.text_input(step_prompt, key=step_key)
        
        if st.button("Next"):
            if response.strip():
                st.session_state.contract_data[step_key] = response.strip()
                st.session_state.current_step += 1
                st.experimental_rerun()
            else:
                st.warning("Please enter a response before proceeding.")
        
        if st.session_state.current_step >= len(self.steps):
            self.finalize_contract()
    
    def finalize_contract(self):
        st.subheader("Review Your Contract Details")
        for key, value in st.session_state.contract_data.items():
            st.write(f"**{key.replace('_', ' ').title()}**: {value}")
        st.success("Your FARBAR contract details have been collected. You can now proceed to fill out the official document.")

if __name__ == "__main__":
    bot = FARBARContractBotWeb()
    bot.start()

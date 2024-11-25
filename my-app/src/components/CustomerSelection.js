import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom'; // Use useNavigate instead of useHistory

const CustomerSelection = ({ toggleNewCustomerForm }) => {
  const [customers, setCustomers] = useState([]);  // State to hold fetched customer data
  const [selectedCustomer, setSelectedCustomer] = useState('');
  const navigate = useNavigate(); // useNavigate replaces useHistory

  // Fetch customer data from the API
  useEffect(() => {
    const fetchCustomers = async () => {
      try {
        const response = await fetch('http://localhost:8000/customers/');
        if (!response.ok) {
          throw new Error('Failed to fetch customers');
        }
        const data = await response.json();
        setCustomers(data); // Store fetched customer data in state
      } catch (error) {
        console.error('Error fetching customers:', error);
      }
    };

    fetchCustomers(); // Call the function to fetch data
  }, []);

  // Handle customer selection
  const handleCustomerChange = (event) => {
    const customerName = event.target.value;
    setSelectedCustomer(customerName);

    if (customerName !== 'Search...') {
      // Redirect to the customer details page
      navigate(`/customer/${customerName}`); // Use navigate instead of history.push
    }
  };

  return (
    <div className="customer-box">
      <label htmlFor="existing-customer" className="select-label">
        Select Existing Customer
      </label>
      <select
        id="existing-customer"
        className="select-customer"
        value={selectedCustomer}
        onChange={handleCustomerChange}
      >
        <option>Search...</option>
        {customers.map((customer) => (
          <option key={customer.name} value={customer.name}>
            {customer.name}
          </option>
        ))}
      </select>
      <div className="or-divider">
        <span>or</span>
      </div>
      <button className="add-customer-btn" onClick={toggleNewCustomerForm}>
        Add a new customer
      </button>
    </div>
  );
};

export default CustomerSelection;

import React, { useState } from 'react';
import './Dashboard.css'; // Import CSS for styling
import companyLogo from './images/cadmax.png'; // Path to the company logo
import CustomerSelection from './components/CustomerSelection';
import NewCustomerForm from './components/NewCustomerForm';
import ConfirmationPopup from './components/ConfirmationPopup';
import WorkingTab from './components/WorkingTab';
import ProfileDropdown from './components/ProfileDropdown'; // Import ProfileDropdown component\
import AttendanceTab from './components/AttendanceTab';  // Import the AttendancePage

// import FormComponent from './components/FormComponent';


const CustomerDashboard = () => {
  const [activeTab, setActiveTab] = useState('customer'); // State to track active tab
  const [showNewCustomerForm, setShowNewCustomerForm] = useState(false); // State to toggle new customer form
  const [selectedDepartment, setSelectedDepartment] = useState(''); // State to track the selected department

  const [showConfirmationPopup, setShowConfirmationPopup] = useState(false); // State for showing confirmation popup


  // State to store new customer form data
  const [customerData, setCustomerData] = useState({
    name: '',
    company: '',
    contact: '',
    address: ''
  });

  const [authToken, setAuthToken] = useState(localStorage.getItem('token') || ''); // Token stored in localStorage

  // Function to handle tab change
  const handleTabChange = (tab) => {
    setActiveTab(tab);
    setShowNewCustomerForm(false); // Ensure the new customer form is hidden when changing tabs
    setSelectedDepartment(''); // Reset department selection
  };

  // Toggle between customer selection and new customer form
  const toggleNewCustomerForm = () => {
    setShowNewCustomerForm(!showNewCustomerForm);
  };

  // Handle department selection for the "Working" tab
  const handleDepartmentChange = (event) => {
    setSelectedDepartment(event.target.value);
  };

  // Handle customer form input changes
  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setCustomerData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

 // Handle form submission with authorization
 const handleSubmit = async (e) => {
  e.preventDefault();
  setShowConfirmationPopup(true);

  if (!authToken) {
    alert('User is not authenticated. Please login first.');
    return;
  }

  try {
    const response = await fetch('http://localhost:8000/customer_register/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authToken}`, // Adding token to the header
      },
      body: JSON.stringify(customerData),
    });

    if (response.ok) {
      const data = await response.json();
      setShowConfirmationPopup(false);
      console.log('Customer created:', data);
      // Optionally, clear the form or show success message
    } else {
      const errorData = await response.json();
      console.error('Error:', errorData.detail);
    }
  } catch (error) {
    console.error('Error submitting form:', error);
  }
};

  // Handle the action when user confirms the submission
  const handleConfirmSubmit = () => {
    setShowConfirmationPopup(false); // Close the confirmation popup
    alert('Customer submitted successfully!'); // You can replace this with actual form submission logic
  };

  // Handle the action when user cancels the submission
  const handleCancelSubmit = () => {
    setShowConfirmationPopup(false); // Close the confirmation popup
  };


  return (

    
    <div className="dashboard-layout">
      {/* Sidebar */}
      <div className="sidebar">
        <div className="logo-container">
          <img src={companyLogo} alt="Company Logo" className="company-logo" />
        </div>
        <nav className="nav-links">
          <a
            href="#customer"
            className={`nav-link ${activeTab === 'customer' ? 'active' : ''}`}
            onClick={() => handleTabChange('customer')}
          >
            Customer
          </a>
          <a
            href="#working"
            className={`nav-link ${activeTab === 'working' ? 'active' : ''}`}
            onClick={() => handleTabChange('working')}
          >
            Working
          </a>
          <a
            href="#attendance"
            className={`nav-link ${activeTab === 'attendance' ? 'active' : ''}`}
            onClick={() => handleTabChange('attendance')}
          >
            Attendance
          </a>
        </nav>
      </div>

      {/* Main Content */}
      <div className="main-content">
        <header className="header">
          <h1 className="company-title">CadMax Projects Pvt. Ltd.</h1>
         <ProfileDropdown /> {/* Profile Dropdown Component */}
        </header>

        {/* Conditionally Render Content based on activeTab */}
        <div className="content-container">
          {/* Customer Tab */}
          {activeTab === 'customer' && !showNewCustomerForm && (
            <CustomerSelection toggleNewCustomerForm={toggleNewCustomerForm} />

          )}

          {/* New Customer Form */}
          {showNewCustomerForm && (
            <NewCustomerForm
              customerData={customerData}
              handleInputChange={handleInputChange}
              handleSubmit={handleSubmit}
              toggleNewCustomerForm={toggleNewCustomerForm}
            />
          )}

          {/* Confirmation Popup */}
          {showConfirmationPopup && (
            <ConfirmationPopup
            customerData={customerData}
            handleConfirmSubmit={handleConfirmSubmit}
            handleCancelSubmit={handleCancelSubmit}
            />
          )}


          {/* Working Tab */}
          {activeTab === 'working' && (
            <WorkingTab
              selectedDepartment={selectedDepartment}
              handleDepartmentChange={handleDepartmentChange}
            />
          )}

          {/* Working Tab */}
          {activeTab === 'attendance' && (
            <AttendanceTab/>
          )}

          

        </div>

      </div>


    </div>
    
  );
};

export default CustomerDashboard;

import React, { useState } from 'react';
import Popup from './Popup';
// import '../../Dashboard.css';
import './WorkingDept.css';

const UrbanForm = () => {
    const [formData, setFormData] = useState({
        ClientName: '',
        Area: '',
        KhasraNo: '',
        Demarcation: '',
        TotalCost: '',
        remarks: ''
    });

    const [showPopup, setShowPopup] = useState(false);
    const [isSubmitting, setIsSubmitting] = useState(false); 
    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({
            ...prevData,
            [name]: value
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setShowPopup(true); // Show popup with form data
    
        try {
            setIsSubmitting(true); // Set submitting state to disable the button
            
            // Retrieve token from localStorage
            const tk = localStorage.getItem('token');
            
            // Log the token to the console for debugging
            // console.log('Token retrieved:', tk);
            
            // Check if the token exists
            if (!tk) {
                console.error('No token found');
                alert('No token found. Please login again.');
                return;
            }
    
            // Proceed with the fetch request using the token
            const response = await fetch('http://127.0.0.1:8000/UrbanPlanning/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${tk}`, // Add authorization header
                },
                body: JSON.stringify(formData), // Send form data as JSON
            });
    
            const data = await response.json();
    
            if (response.ok) {
                console.log('UrbanPlanning submitted:', data);
                setShowPopup(false); // Hide popup after successful submission
                alert('UrbanPlanning submitted successfully!');
            } else {
                console.error('Submission failed:', data);
                alert('Error submitting UrbanPlanning. Please try again.');
            }
        } catch (error) {
            console.error('Error during submission:', error);
            alert('Network error. Please try again.');
        } finally {
            setIsSubmitting(false); // Reset submitting state
        }
    };

    const handleConfirm = () => {
        alert('Form Submitted!');
        setShowPopup(false);
    };

    const handleCancel = () => {
        setShowPopup(false);
    };


    return (
        <div>
            <form onSubmit={handleSubmit}>
                <div className="urban-form">
                    <div className="form-group">
                        <label>Client Name</label>
                        <input type="text" name="ClientName"
                            value={formData.ClientName} onChange={handleChange} className="form-input" placeholder="Enter Name" />
                    </div>
                    <div className="form-group">
                        <label>Area</label>
                        <input type="text" name="Area"
                            value={formData.Area} onChange={handleChange} className="form-input" placeholder="Enter Area" />
                    </div>
                    <div className="form-group">
                        <label>Khasra No.</label>
                        <input type="text" name="KhasraNo"
                            value={formData.KhasraNo} onChange={handleChange} className="form-input" placeholder="Enter Khasra No." />
                    </div>
                    <div className="form-group">
                        <label>Demarcation</label>
                        <input type="text" name="Demarcation"
                            value={formData.Demarcation} onChange={handleChange} className="form-input" placeholder="Enter Demarcation" />
                    </div>
                    <div className="form-group">
                        <label>Total Cost</label>
                        <input type="text" name="TotalCost"
                            value={formData.TotalCost} onChange={handleChange} className="form-input" placeholder="Enter Total Cost" />
                    </div>
                    <div className="form-group final-field">
                        <label>Remarks</label>
                        <input type="text" name="remarks"
                            value={formData.remarks} onChange={handleChange} className="form-input" placeholder="Enter Remarks" />
                    </div>
                    <button className="submit-btn">Submit</button>
                </div>

            </form>

            {showPopup && (
                <Popup
                    formData={formData}
                    onConfirm={handleConfirm}
                    onCancel={handleCancel}
                />
            )}
        </div>
    );
};

export default UrbanForm;
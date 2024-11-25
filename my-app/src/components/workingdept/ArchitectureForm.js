import React, { useState } from 'react';
import Popup from './Popup';
// import '../../Dashboard.css';
import './WorkingDept.css';
const ArchitectureForm = () => {
    const [formData, setFormData] = useState({
        ClientName: '',
        BuildingType: '',
        Location: '',
        TotalArea: '',
        TotalCost: '',
        DesignStyle: '',
        Remarks: ''
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
            const response = await fetch('http://127.0.0.1:8000/Architecture/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${tk}`, // Add authorization header
                },
                body: JSON.stringify(formData), // Send form data as JSON
            });
    
            const data = await response.json();
    
            if (response.ok) {
                console.log('Architecture submitted:', data);
                setShowPopup(false); // Hide popup after successful submission
                alert('Architecture submitted successfully!');
            } else {
                console.error('Submission failed:', data);
                alert('Error submitting Architecture. Please try again.');
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
                <div className="architecture-form">
                    <div className="form-group">
                        <label>Client Name</label>
                        <input
                            type="text"
                            name="ClientName"
                            value={formData.ClientName}
                            className='form-input'
                            onChange={handleChange}
                            placeholder="Enter Name"
                        />
                    </div>
                    <div className="form-group">
                        <label>Building Type</label>
                        <input
                            type="text"
                            name="BuildingType"
                            value={formData.BuildingType}
                            className='form-input'
                            onChange={handleChange}
                            placeholder="Enter Building type"
                        />
                    </div>
                    <div className="form-group">
                        <label>Location</label>
                        <input
                            type="text"
                            name="Location"
                            value={formData.Location}
                            className='form-input'
                            onChange={handleChange}
                            placeholder="Enter Location"
                        />
                    </div>
                    <div className="form-group">
                        <label>Area</label>
                        <input
                            type="number"
                            name="TotalArea"
                            value={formData.TotalArea}
                            className='form-input'
                            onChange={handleChange}
                            placeholder="Enter Area"
                        />
                    </div>
                    <div className="form-group">
                        <label>Total Cost</label>
                        <input
                            type="number"
                            name="TotalCost"
                            value={formData.TotalCost}
                            className='form-input'
                            onChange={handleChange}
                            placeholder="Enter Total cost"
                        />
                    </div>
                    <div className="form-group">
                        <label>Design Style</label>
                        <input
                            type="text"
                            name="DesignStyle"
                            value={formData.DesignStyle}
                            className='form-input'
                            onChange={handleChange}
                            placeholder="Enter Design style"
                        />
                    </div>
                    <div className="form-group">
                        <label>Remarks</label>
                        <input
                            type="text"
                            name="Remarks"
                            value={formData.Remarks}
                            className='form-input'
                            onChange={handleChange}
                            placeholder="Enter remarks"
                        />
                    </div>
                    <button type="submit" className="submit-btn">Submit</button>
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

export default ArchitectureForm;

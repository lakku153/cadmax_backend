import React, { useState } from 'react';
import Popup from './Popup';
// import '../../Dashboard.css';
import './WorkingDept.css';


const PrintForm = () => {

    const [formData, setFormData] = useState({
        ClientName: '',
        TypeOfPrint: '',
        KhasraNo: '',
        PaperSize: '',
        TotalArea: '',
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
            const response = await fetch('http://127.0.0.1:8000/Print/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${tk}`, // Add authorization header
                },
                body: JSON.stringify(formData), // Send form data as JSON
            });
    
            const data = await response.json();
    
            if (response.ok) {
                console.log('Print submitted:', data);
                setShowPopup(false); // Hide popup after successful submission
                alert('Print submitted successfully!');
            } else {
                console.error('Submission failed:', data);
                alert('Error submitting Print. Please try again.');
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

                <div className="print-form">
                    <div className="form-group">
                        <label>Client Name</label>
                        <input type="text" className="form-input" name="ClientName"
                            value={formData.ClientName} onChange={handleChange} placeholder="Enter Name" />
                    </div>
                    <div className="form-group">
                        <label>Type Of Print</label>
                        <input type="text" className="form-input" name="TypeOfPrint"
                            value={formData.TypeOfPrint} onChange={handleChange} placeholder="Enter Type of Print" />
                    </div>
                    <div className="form-group">
                        <label>Khasra No.</label>
                        <input type="text" className="form-input" name="KhasraNo"
                            value={formData.KhasraNo} onChange={handleChange} placeholder="Enter Khasra No." />
                    </div>
                    <div className="form-group">
                        <label>Paper Size</label>
                        <input type="text" className="form-input" name="PaperSize"
                            value={formData.PaperSize} onChange={handleChange} placeholder="Enter Paper Size" />
                    </div>
                    <div className="form-group">
                        <label>TotalArea</label>
                        <input type="text" className="form-input" name="TotalArea"
                            value={formData.TotalArea} onChange={handleChange} placeholder="Enter Total Area" />
                    </div>
                    <div className="form-group">
                        <label>Total Cost</label>
                        <input type="text" className="form-input" name="TotalCost"
                            value={formData.TotalCost} onChange={handleChange} placeholder="Enter Total Cost" />
                    </div>
                    <div className="form-group final-field">
                        <label>Remarks</label>
                        <input type="text" className="form-input" name="Remarks"
                            value={formData.remarks} onChange={handleChange} placeholder="Enter Remarks" />
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

export default PrintForm;
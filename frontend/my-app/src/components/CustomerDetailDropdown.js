import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';  // For handling dynamic routes
import './WorkingDataDropdowns.css';
import axios from 'axios';
import { jsPDF } from 'jspdf'; // Import jsPDF

const CustomerDetailDropdown = () => {
    const { name } = useParams();  // Extract the customer name from URL
    const [taskData, setTaskData] = useState({});  // Store task data for the last 7 days, using an object with date keys
    const [showAllData, setShowAllData] = useState(false);  // Toggle for "Show More" button
    const [allTaskData, setAllTaskData] = useState([]);  // Store full task data when "Show More" is clicked
    const [openDropdown, setOpenDropdown] = useState(null);  // To track the open/close state of each dropdown
    // const { clientName } = useClient() || {};

    // Retrieve the authentication token from localStorage or context
    const authToken = localStorage.getItem('token'); // Adjust this if you're using Context or Redux

    // Fetch task data for a specific date when it's selected from dropdown
    const fetchTaskData = async (date) => {
        if (!authToken) {
            console.error('User is not authenticated. Token is missing.');
            return;
        }

        try {
            const response = await axios.get(`http://127.0.0.1:8000/customer_working/?date=${date}&name=${name}`, {
                headers: {
                    'Authorization': `Bearer ${authToken}`, // Attach token to the request header
                }
            });
            console.log('Fetched task data:', response.data); // Check the API response

            const { Department,  ...taskWithoutClient } = response.data;
            
            // Update taskData for the specific date
            setTaskData((prevData) => ({
                ...prevData,
                [date]: response.data, // Update data for the selected date
            }));
        } catch (error) {
            console.error('Error fetching task data:', error);
        }
    };

    // Fetch all task data (full history) with authorization
    const fetchAllTaskData = async () => {
        if (!authToken) {
            console.error('User is not authenticated. Token is missing.');
            return;
        }

        try {
            const response = await axios.get(`http://127.0.0.1:8000/customer_working/ClientName=${name}`, {
                headers: {
                    'Authorization': `Bearer ${authToken}`, // Attach token to the request header
                }
            });
            console.log('Fetched all task data:', response.data);
            setAllTaskData(response.data.tasks);  // Set full task history
            setShowAllData(true);  // Update state to show full data
        } catch (error) {
            console.error('Error fetching all task data:', error);
        }
    };

    // Function to format the date
    const formatDate = (date) => {
        return date.toLocaleDateString('en-US', {
            weekday: 'short',
            month: 'short',
            day: 'numeric',
        });
    };

    // Calculate "Today", "Yesterday", and the last 5 days
    const getDateLabels = () => {
        const dates = [];
        const today = new Date();
        const yesterday = new Date(today);
        yesterday.setDate(today.getDate() - 1);

        dates.push('Today', 'Yesterday');

        // Add the last 5 days before yesterday
        for (let i = 2; i <= 6; i++) {
            const previousDay = new Date(yesterday);
            previousDay.setDate(yesterday.getDate() - i + 1);
            dates.push(formatDate(previousDay));
        }

        return dates;
    };

    // Handle dropdown toggle and fetch task data for the selected date
    const handleDropdownToggle = (day) => {
        setOpenDropdown(openDropdown === day ? null : day);  // Toggle open/close for each dropdown

        // Fetch data for the selected date if not already fetched
        if (!taskData[day]) {
            fetchTaskData(day);  // Fetch data for this date
        }
    };

    // Generate bill PDF for the specific day
    const generateBill = (day) => {
        const task = taskData[day];
        if (task) {
            const doc = new jsPDF();

            // Set up PDF title
            doc.setFontSize(20);
            doc.text('Customer Bill', 14, 20);

            // Set up body content
            let yPosition = 30;
            doc.setFontSize(12);

            // Add task details to PDF
            doc.text(`Date: ${day}`, 14, yPosition);
            yPosition += 10;

            doc.text(`Department: ${task.Department || 'N/A'}`, 14, yPosition);
            yPosition += 10;

            doc.text(`Cost: $${task.TotalCost || 'N/A'}`, 14, yPosition);
            yPosition += 10;

            doc.text(`Working: ${task.Working || 'N/A'}`, 14, yPosition);
            yPosition += 10;

            doc.text(`Staff: ${task.Staff || 'N/A'}`, 14, yPosition);
            yPosition += 10;

            doc.text(`Area: ${task.TotalArea || 'N/A'}`, 14, yPosition);
            yPosition += 10;

            // Add a footer for the bill
            doc.text('Thank you for your business!', 14, yPosition + 10);

            // Save the PDF as a file
            doc.save(`customer_bill_${day}.pdf`);
        } else {
            alert('No task data available for this day to generate the bill.');
        }
    };

    const dateLabels = getDateLabels();

    return (
        <div className="working-data-container">
            <h2 className="working-data-header">Select Customer Data for the Last 7 Days</h2>
            <div className="dropdowns-wrapper">
                {dateLabels.map((label) => {
                    const task = taskData[label] || {}; // Get the task for the selected day

                    return (
                        <div key={label} className="dropdown-container">
                            <label htmlFor={label} className="dropdown-label">{label}</label>
                            <select
                                id={label}
                                value={openDropdown === label ? label : ''} // Show the label when it's open
                                onChange={() => handleDropdownToggle(label)} // Toggle open/close on change
                                className="dropdown"
                            >
                                <option value="">Select a day</option>
                                <option value={label}>{label}</option>
                            </select>

                            {/* Only show task details when the corresponding dropdown is open */}
                            {openDropdown === label && task && (
                                <div className="task-details">
                                    <div><strong>Department:</strong> {task.Department }</div>
                                    <div><strong>Cost:</strong> {task.TotalCost || 'N/A'}</div>
                                    <div><strong>Working:</strong> {task.Working || 'N/A'}</div>
                                    <div><strong>Staff:</strong> {task.Staff || 'N/A'}</div>
                                    <div><strong>Area:</strong> {task.TotalArea || 'N/A'}</div>

                                     {/* Generate Bill button inside the task details */}
                                     <button 
                                        onClick={() => generateBill(label)} 
                                        className="generate-bill-button"
                                    >
                                        Generate Bill
                                    </button>
                                </div>
                            )}

                            {/* Display message if no task is available for the selected day */}
                            {openDropdown === label && !task && (
                                <div className="no-task">
                                    No task available for this day.
                                </div>
                            )}
                        </div>
                    );
                })}
            </div>

            {/* Show More Button */}
            {!showAllData && (
                <button onClick={fetchAllTaskData} className="show-more-button">
                    Show More History
                </button>
            )}

            {/* Display all task history */}
            {showAllData && allTaskData.length > 0 && (
                <div className="all-task-history">
                    <h3>Full Task History:</h3>
                    <ul>
                        {allTaskData.map((task) => (
                            <li key={task.id}>
                                <div><strong>Department:</strong> {task.Department || 'N/A'}</div>
                                <div><strong>Cost:</strong> {task.cost || 'N/A'}</div>
                                <div><strong>Working:</strong> {task.working || 'N/A'}</div>
                                <div><strong>Staff:</strong> {task.staff || 'N/A'}</div>
                                <div><strong>Area:</strong> {task.area || 'N/A'}</div>
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
};

export default CustomerDetailDropdown;

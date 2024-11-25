import React, { useState, useEffect } from 'react';
import './WorkingDataDropdowns.css';
import axios from 'axios';

const CustomerDetailDropdown = () => {
    const [taskData, setTaskData] = useState([]);  // Store task data for the last 7 days
    const [selectedDay, setSelectedDay] = useState(null);  // Store selected day
    const [showAllData, setShowAllData] = useState(false);  // Toggle for "Show More" button
    const [allTaskData, setAllTaskData] = useState([]);  // Store full task data when "Show More" is clicked

    // Fetch task data from API
    useEffect(() => {
        const fetchTaskData = async () => {
            try {
                const response = await axios.get('/api/tasks');
                console.log('Fetched task data:', response.data); // Check the API response
                setTaskData(response.data.tasks);  // Set the task data for the last 7 days
            } catch (error) {
                console.error('Error fetching task data:', error);
            }
        };

        fetchTaskData();
    }, []);

    // Fetch all task data (full history)
    const fetchAllTaskData = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/');  // API endpoint for full task history
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

    // Find the task for a specific day
    const getTaskForDate = (date) => {
        const task = taskData.find(task => {
            const taskDate = new Date(task.date);
            const formattedTaskDate = formatDate(taskDate);
            return formattedTaskDate === date;
        });

        return task || {};  // Return an empty object if no task is found
    };

    const dateLabels = getDateLabels();

    // Handle dropdown value change
    const handleDropdownChange = (day) => {
        setSelectedDay(day);
    };

    return (
        <div className="working-data-container">
            <h2 className="working-data-header">Select Customer Data for the Last 7 Days</h2>
            <div className="dropdowns-wrapper">
                {dateLabels.map((label) => {
                    const task = getTaskForDate(label); // Get the task for the selected day

                    return (
                        <div key={label} className="dropdown-container">
                            <label htmlFor={label} className="dropdown-label">{label}</label>
                            <select
                                id={label}
                                value={selectedDay === label ? label : ''}
                                onChange={() => handleDropdownChange(label)} // Change the selected day
                                className="dropdown"
                            >
                                <option value="">Select a day</option>
                                <option value={label}>{label}</option>
                            </select>

                            {/* Only show task details when a day is selected and task data is available */}
                            {selectedDay === label && (
                                <div className="task-details">
                                    <div><strong>Department:</strong> {task.department || 'N/A'}</div>
                                    <div><strong>Cost:</strong> {task.cost || 'N/A'}</div>
                                    <div><strong>Working:</strong> {task.working || 'N/A'}</div>
                                    <div><strong>Staff:</strong> {task.staff || 'N/A'}</div>
                                    <div><strong>Area:</strong> {task.area || 'N/A'}</div>
                                </div>
                            )}

                            {/* Display message if no task is available for the selected day */}
                            {selectedDay === label && !task && (
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
                                <div><strong>Department:</strong> {task.department || 'N/A'}</div>
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

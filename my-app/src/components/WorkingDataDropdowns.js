import React, { useState, useEffect } from 'react';
import './WorkingDataDropdowns.css';
import axios from 'axios';

const WorkingDataDropdowns = () => {
  const [taskData, setTaskData] = useState([]);
  const [selectedDay, setSelectedDay] = useState(null); // Store selected day

  // Fetch task data from API
  useEffect(() => {
    const fetchTaskData = async () => {
      try {
        const response = await axios.get('/api/tasks');
        console.log('Fetched task data:', response.data); // Check the API response
        setTaskData(response.data.tasks);
      } catch (error) {
        console.error('Error fetching task data:', error);
      }
    };

    fetchTaskData();
  }, []);

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

    return task; // Returns the task if found, or undefined if no task is found
  };

  const dateLabels = getDateLabels();

  // Handle dropdown value change
  const handleDropdownChange = (day) => {
    setSelectedDay(day);
  };

  return (
    <div className="working-data-container">
      <h2 className="working-data-header">Select Working Data for the Last 7 Days</h2>
      <div className="dropdowns-wrapper">
        {dateLabels.map((label, index) => {
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

              {/* Display task details directly if a task exists for the day */}
              {selectedDay === label && task && (
                <div className="task-details">
                  <div><strong>ID:</strong> {task.id}</div>
                  <div><strong>Department:</strong> {task.department}</div>
                  <div><strong>Area:</strong> {task.area}</div>
                  <div><strong>Cost:</strong> {task.cost}</div>
                  <div><strong>Client Name:</strong> {task.clientName}</div>
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
    </div>
  );
};

export default WorkingDataDropdowns;

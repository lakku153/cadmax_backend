import React, { useState } from 'react';
import './AttendanceTab.css';  // Import the CSS for styling
import mapLogo from '../images/maplogo.png';  // Import the map logo

const AttendanceTab = () => {
  const [Address, setAddress] = useState('');  // State for employee ID
  const [locationAccessRequested, setLocationAccessRequested] = useState(false); // Track if location is requested
  const [location, setLocation] = useState(null); // Store the fetched location
  const [popupVisible, setPopupVisible] = useState(false);  // Control visibility of the attendance popup
  const [attendanceLocation, setAttendanceLocation] = useState('');  // Location for attendance
  const [attendanceDateTime, setAttendanceDateTime] = useState('');  // Date/Time for attendance

  // Handle form input change
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    if (name === 'Address') {
      setAddress(value);
    }
  };

  // Handle form submit
  const handleSubmit = (e) => {
    e.preventDefault();
    setPopupVisible(true); // Show the popup when the button is clicked
    // Here you would typically send the data to the backend for saving
    setAddress('');  // Reset the field after submitting
  };

  // Handle click on the map logo to request location
  const handleLocationClick = () => {
    setLocationAccessRequested(true); // Trigger the popup
  };

  // Handle "Allow" location access
  const handleAllowLocation = () => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          setLocation({
            latitude: position.coords.latitude,
            longitude: position.coords.longitude
          });
          setAttendanceLocation(`Lat: ${position.coords.latitude}, Lon: ${position.coords.longitude}`);
          alert('Location Access Granted!');
        },
        (error) => {
          alert('Location Access Denied or Error: ' + error.message);
        }
      );
    } else {
      alert('Geolocation is not supported by this browser.');
    }
    setLocationAccessRequested(false); // Hide the location popup
  };

  // Handle "Deny" location access
  const handleDenyLocation = () => {
    alert('Location Access Denied.');
    setLocationAccessRequested(false); // Hide the popup
  };

  // Handle "Confirm" button on the popup
  const handleConfirmAttendance = () => {
    alert(`Attendance Recorded! Location: ${attendanceLocation}, DateTime: ${attendanceDateTime}`);
    // Here, you can send the data to the backend for saving
    setPopupVisible(false); // Hide the popup after confirming
  };

  // Handle "Cancel" button on the popup
  const handleCancelAttendance = () => {
    setPopupVisible(false); // Close the popup without saving
  };

  // Set Date/Time when popup is opened
  React.useEffect(() => {
    if (popupVisible) {
      setAttendanceDateTime(new Date().toLocaleString()); // Set current date/time when popup is visible
    }
  }, [popupVisible]);


  return (
    <div className="attendance-page">
      <h2 className="attendance-header">Employee Attendance</h2>



      {/* Attendance Form */}
      <form onSubmit={handleSubmit} className="attendance-form">
        <div className="form-group">
          <div className="input-container">
            <input
              type="text"
              id="Address"
              name="Address"
              placeholder="Enter Address"
              value={Address}
              onChange={handleInputChange}
              required
            />
            {/* Map logo image */}
            <img src={mapLogo} alt="Map Logo" className="map-logo" onClick={handleLocationClick} />     {/* // Trigger location access request on click/>   */}
          </div>
        </div>

        <button type="submit" className="submit-btn">Record Attendance</button>
      </form>

      {/* Location Access Popup */}
      {locationAccessRequested && (
        <div className="location-popup">
          <div className="popup-content">
            <h3>Access Your Location</h3>
            <div className="popup-buttons">
              <button onClick={handleAllowLocation} className="allow-btn">Allow</button>
              <button onClick={handleDenyLocation} className="deny-btn">Deny</button>
            </div>
          </div>
        </div>
      )}

      {/* Attendance Confirmation Popup */}
      {popupVisible && (
        <div className="attendance-popup">
          <div className="popup-content">
            <h3>Confirm Attendance</h3>
            <div className="popup-fields">
              <div><strong>Location:</strong> {attendanceLocation || 'Not Available'}</div>
              <div><strong>Date/Time:</strong> {attendanceDateTime}</div>
            </div>
            <div className="popup-buttons">
              <button onClick={handleConfirmAttendance} className="confirm-btn">Confirm</button>
              <button onClick={handleCancelAttendance} className="cancel-btn">Cancel</button>
            </div>
          </div>
        </div>
      )}

    </div>
  );
};

export default AttendanceTab;

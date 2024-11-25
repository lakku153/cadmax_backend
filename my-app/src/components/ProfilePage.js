import React, { useEffect, useState } from 'react';
import './ProfilePage.css'; // Importing CSS for styling
import WorkingDataDropdowns from './WorkingDataDropdowns'; // Import the WorkingDataDropdowns component

function ProfilePage() {
    // State to store the user data
    const [userData, setUserData] = useState({ username: 'Loading...', jobRole: 'Loading...' });

    // Fetch user data from API once the component mounts
    useEffect(() => {
        const fetchUserData = async () => {
            try {
                // Replace with your actual API endpoint
                const response = await fetch('http://localhost:8000/profile/'); // Change this as per your backend API

                // Check if response is OK
                if (!response.ok) {
                    throw new Error(`Failed to fetch user data. Status: ${response.status}`);
                }

                const data = await response.json();

                // Set user data once it's fetched
                setUserData({
                    username: data.username,
                    jobRole: data.jobRole
                });
            } catch (err) {
                console.error("Error fetching user data:", err);
            }
        };

        fetchUserData();
    }, []); // Empty dependency array ensures this runs once when the component mounts

    return (
        <div className="profile-page">
            <div className="profile-header">
                <div className="profile-info">
                    <div className="username-container">
                        <div className="avatar"></div> {/* Optional avatar */}
                        <h1 className="username">{userData.username}</h1>
                        <p className="job-role">{userData.jobRole}</p>
                    </div>
                </div>
            </div>

            {/* Container for last 7 days working data */}
            <WorkingDataDropdowns />
        </div>
    );
}

export default ProfilePage;

import React, { useState, useEffect } from "react";
import axios from "axios";
import BaseLayout from "../BaseLayout";

function AdminDashboard() {
  const [users, setUsers] = useState([]);
  const [error, setError] = useState(null);


  useEffect(() => {
    axios
      .get(`${process.env.REACT_APP_API_URL}/admin/users`)
      .then((response) => {
        setUsers(response.data);
      })
      .catch((err) => {
        setError("Error fetching users: " + err.message);
      });
  }, []);

  return (
    <BaseLayout>
      <h2 className="text-2xl font-semibold">List Users</h2>
      {error && <p className="text-red-500">{error}</p>}
      {users.length === 0 ? (
        <p className="text-gray-600 mt-2">No users found.</p>
      ) : (
        <ul className="mt-4">
          {users.map((user) => (
            <li key={user.user_id} className="bg-white p-2 mb-2 shadow rounded">
              {user.username} - {user.role}
            </li>
          ))}
        </ul>
      )}
    </BaseLayout>
  );
}

export default AdminDashboard;

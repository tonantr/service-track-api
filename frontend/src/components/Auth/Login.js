import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState(null);

    const navigate = useNavigate();

    const login = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.post(`${process.env.REACT_APP_API_URL}/`, {
                username,
                password,
            });

            if (response.status === 200) {
                setError(null);
                localStorage.setItem('access_token', response.data.access_token);
                navigate("/admin");
            }
        } catch (err) {
            setError('Invalid credentials');
            console.error(err);
        }
    };

    return (
        <div className="login-container">
            <h2>Login</h2>
            <form onSubmit={login}>
                <div style={{ marginBottom: '10px' }}>
                    <div>
                        <label htmlFor="username">Username:</label>
                    </div>
                    <input
                        id="username"
                        type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                </div>
                <div style={{ marginBottom: '10px' }}>
                    <div>
                        <label htmlFor="password">Password:</label>
                    </div>
                    <input
                        id="password"
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <button type="submit" style={{ marginTop: '10px' }}>Login</button>
            </form>

            {error && <p className="error">{error}</p>}
        </div>
    );
}

export default Login;
